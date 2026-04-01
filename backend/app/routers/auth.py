from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import AuthResponse, LoginRequest, MessageResponse, RegisterRequest, UserProfile
from app.services.auth_service import (
    authenticate_user,
    create_session_token,
    create_user,
    delete_session_token,
    get_current_user,
    get_current_user_and_token,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = create_user(db, payload.full_name, payload.email, payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    token = create_session_token(db, user)
    return {
        "token": token,
        "user": UserProfile.model_validate(user, from_attributes=True),
    }


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(db, payload.email, payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc

    token = create_session_token(db, user)
    return {
        "token": token,
        "user": UserProfile.model_validate(user, from_attributes=True),
    }


@router.get("/me", response_model=UserProfile)
def me(user=Depends(get_current_user)):
    return UserProfile.model_validate(user, from_attributes=True)


@router.post("/logout", response_model=MessageResponse)
def logout(auth_context=Depends(get_current_user_and_token), db: Session = Depends(get_db)):
    _, token = auth_context
    delete_session_token(db, token)
    return {"message": "Logged out successfully."}
