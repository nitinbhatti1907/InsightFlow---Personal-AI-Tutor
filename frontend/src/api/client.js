const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api';

function getStoredToken() {
  return localStorage.getItem('learning_assistant_token') || '';
}

export function storeAuthSession(token, user) {
  localStorage.setItem('learning_assistant_token', token);
  localStorage.setItem('learning_assistant_user', JSON.stringify(user));
}

export function clearAuthSession() {
  localStorage.removeItem('learning_assistant_token');
  localStorage.removeItem('learning_assistant_user');
}

export function getStoredUser() {
  const value = localStorage.getItem('learning_assistant_user');
  if (!value) return null;
  try {
    return JSON.parse(value);
  } catch {
    return null;
  }
}

async function request(path, options = {}) {
  const token = getStoredToken();
  const response = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    const contentType = response.headers.get('content-type') || '';

    if (contentType.includes('application/json')) {
      const errorPayload = await response.json();
      throw new Error(errorPayload.detail || errorPayload.message || 'Request failed');
    }

    const text = await response.text();
    throw new Error(text || 'Request failed');
  }

  return response.json();
}

export const api = {
  getOverview: () => request('/course/overview'),
  getTopics: () => request('/course/topics'),
  register: (payload) => request('/auth/register', { method: 'POST', body: JSON.stringify(payload) }),
  login: (payload) => request('/auth/login', { method: 'POST', body: JSON.stringify(payload) }),
  me: () => request('/auth/me'),
  logout: () => request('/auth/logout', { method: 'POST' }),
  getDashboard: () => request('/learning/dashboard'),
  getLearnerOverview: () => request('/learning/my-overview'),
  generateContent: (payload) => request('/learning/generate', { method: 'POST', body: JSON.stringify(payload) }),
  learnMore: (payload) => request('/learning/learn-more', { method: 'POST', body: JSON.stringify(payload) }),
  evaluateQuiz: (payload) => request('/learning/evaluate-quiz', { method: 'POST', body: JSON.stringify(payload) }),
  markTopicRead: (payload) => request('/learning/mark-read', { method: 'POST', body: JSON.stringify(payload) }),
  submitFeedback: (payload) => request('/learning/feedback', { method: 'POST', body: JSON.stringify(payload) }),
};