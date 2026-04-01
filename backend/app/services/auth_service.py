from __future__ import annotations

import hashlib
import hmac
import secrets
from typing import Tuple

from fastapi import Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import User, UserSession


def _hash_password(password: str, salt: str) -> str:
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 120_000)
    return digest.hex()


def create_password_hash(password: str) -> str:
    salt = secrets.token_hex(16)
    return f"{salt}${_hash_password(password, salt)}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt, hashed = stored_hash.split("$", 1)
    except ValueError:
        return False
    candidate = _hash_password(password, salt)
    return hmac.compare_digest(candidate, hashed)


def _hash_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_user(db: Session, full_name: str, email: str, password: str) -> User:
    existing = db.scalar(select(User).where(User.email == email.lower()))
    if existing:
        raise ValueError("An account with this email already exists.")

    user = User(full_name=full_name.strip(), email=email.lower(), password_hash=create_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> User:
    user = db.scalar(select(User).where(User.email == email.lower()))
    if not user or not verify_password(password, user.password_hash):
        raise ValueError("Invalid email or password.")
    return user


def create_session_token(db: Session, user: User) -> str:
    raw_token = secrets.token_urlsafe(32)
    session = UserSession(user_id=user.id, token_hash=_hash_token(raw_token))
    db.add(session)
    db.commit()
    return raw_token


def delete_session_token(db: Session, token: str) -> None:
    session = db.scalar(select(UserSession).where(UserSession.token_hash == _hash_token(token)))
    if session:
        db.delete(session)
        db.commit()


def get_user_by_token(db: Session, token: str) -> User | None:
    session = db.scalar(select(UserSession).where(UserSession.token_hash == _hash_token(token)))
    if not session:
        return None
    return db.get(User, session.user_id)


def _extract_bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Authentication required.")
    return authorization.split(" ", 1)[1].strip()


def get_current_user(
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db),
) -> User:
    token = _extract_bearer_token(authorization)
    user = get_user_by_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Session expired or invalid. Please log in again.")
    return user


def get_current_user_and_token(
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db),
) -> Tuple[User, str]:
    token = _extract_bearer_token(authorization)
    user = get_user_by_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Session expired or invalid. Please log in again.")
    return user, token
