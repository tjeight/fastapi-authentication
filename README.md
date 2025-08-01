# 🔐 FastAPI Authentication System with JWT & Cookies

This project implements a secure authentication system using FastAPI, JSON Web Tokens (JWT), and HttpOnly Cookies for session management.

---

## 📦 Features

- 🔒 Password hashing with salt
- 🛡️ JWT access token creation and validation
- 🍪 Secure Cookie-based storage for JWT
- 🚪 Login with token generation
- ✅ FastAPI-based route protection

---

## 🧠 Concepts Covered

### 1. ✅ User Login Flow

- User sends `username` and `password`
- Server validates user
- On success, generates JWT with user info
- JWT is **stored inside an HttpOnly Cookie**

### 2. 🔐 JWT Token Structure

JWT consists of:

- **Header**: Algorithm & Token Type
- **Payload**: User data (like `sub=username`) + Expiry
- **Signature**: Signed with secret key

Example Payload:

```json
{
  "sub": "tejas",
  "exp": "2025-07-29T18:00:00Z"
}
```

### 3. 📤 How Cookie is Set

### Using FastAPI's set_cookie method:

```
response.set_cookie(
    key="access_token",
    value=jwt_token,
    httponly=True,   # Cannot be accessed via JS
    samesite="lax",  # Prevent CSRF
    secure=True      # Only via HTTPS
)
```

---

### Implementation

```
def create_token(data: dict, exp_time: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + exp_time
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


```

### 🍪 Set Cookie Function

```
def set_cookie_token(response: Response, token: str):
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=True
    )
```

### 👨‍💻 Author

### 😎Tejas Jagdale😎

### Developer, Dreamer, and Doer — Building the future one line at a time.

### Loves tech, emojis, Hindi slang, and a poetic code life.

### 🌐 Pune | 🧠 AI Explorer | ⚙️ Full-Stack Dev
