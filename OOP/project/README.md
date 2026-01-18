# 🔐 Flask Authentication API  
### *Secure • Scalable • Production-style Backend*

A **modern authentication system** built using **Flask**, **JWT**, and **SQLite**.  
This project implements **secure login, token-based authentication, role-based authorization, and blacklist logout system**.

> ⚡ Designed following **real-world backend architecture** and security practices.

---

## 🌟 Highlights

- ✔ **JWT Authentication** (Access & Refresh Tokens)  
- ✔ **Role-Based Access Control**  
- ✔ **Secure Password Hashing (bcrypt)**  
- ✔ **Token Blacklist Logout**  
- ✔ **Protected Routes**  
- ✔ **Resume-ready Backend Project**

---

## 🚀 Features

- 🔐 **JWT Authentication**
- 👤 **User Signup & Login**
- ♻ **Access & Refresh Tokens**
- 🛡 **Role-Based Authorization (Admin/User)**
- 🚪 **Logout using Token Blacklist**
- 🔒 **Protected Routes**
- 🗃 **SQLite Database**
- 🧪 **API Testing (Postman / Terminal)**

---

## 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| **Backend** | Flask (Python) |
| **Authentication** | Flask-JWT-Extended |
| **Database** | SQLite |
| **Security** | bcrypt |
| **Testing** | Postman, curl |

---

## 📁 Project Structure

```text
flask_auth_api/
│
├── app.py              # Main Flask application
├── auth.py             # Authentication logic
├── db.py               # Database operations
├── decorators.py       # Role-based decorators
├── blacklist.py        # Token blacklist logic
├── users.db            # SQLite database
├── test_login.py       # Login test script
├── test_logout.py      # Logout test script
├── requirements.txt
└── README.md
⚙️ Setup & Run
1️⃣ Clone repository
git clone https://github.com/your-username/flask-auth-api.git
cd flask-auth-api

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run server
python app.py


Server runs at:

http://127.0.0.1:5000

🔑 API Endpoints
🏠 Home
GET /

📝 Signup
POST /signup


Request Body

{
  "username": "khyati",
  "password": "1234",
  "role": "admin"
}

🔐 Login
POST /login


Request Body

{
  "username": "khyati",
  "password": "1234"
}


Response

{
  "access_token": "...",
  "refresh_token": "...",
  "user": {
    "username": "khyati",
    "role": "admin"
  }
}

🔒 Protected Route
GET /dashboard


Headers

Authorization: Bearer <access_token>

♻ Refresh Token
POST /refresh


Headers

Authorization: Bearer <refresh_token>

🚪 Logout
POST /logout


Headers

Authorization: Bearer <access_token>

🔐 Security

✔ Passwords hashed using bcrypt

✔ JWT token expiry implemented

✔ Refresh token system

✔ Blacklist logout mechanism

✔ Role-based permissions

✔ Protected routes

📚 What I Learned

REST API development with Flask

JWT authentication workflow

Secure password storage using bcrypt

Token-based authorization

Role-based access control

Debugging backend systems

Clean project architecture

📝 Resume Summary

Built a secure authentication API using Flask with JWT-based authorization, refresh tokens, role-based access control, and token blacklist logout system. Implemented bcrypt password hashing with SQLite integration.

👩‍💻 Author

Khyati Sharma
🎓 B.Tech AI Student
💻 Backend & ML Enthusiast

🚀 Future Enhancements

📧 Email verification

🔑 Password reset system

🧪 Unit testing

📜 Swagger API documentation

🐳 Docker deployment

☁ Cloud hosting

⭐ Support

If you liked this project, give it a ⭐ star
It motivates me to build more!


---

### 🔥 Now your README has:
✔ **Bold text**  
✔ Proper **headings**  
✔ Tables  
✔ Code blocks  
✔ Clean spacing  
✔ GitHub-friendly layout  

---

