import bcrypt
import db


def hash_password(password: str) -> bytes:
    """
    Hashes plain password using bcrypt
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def verify_password(password: str, hashed: bytes) -> bool:
    """
    Compares plain password with hashed password
    """

    if isinstance(hashed, str):
        hashed = hashed.encode()

    return bcrypt.checkpw(password.encode(), hashed)


def signup_user(username: str, password: str, role: str):
    """
    Registers new user
    """

    if db.get_user(username):
        return {"error": "User already exists"}

    hashed_password = hash_password(password)

    db.add_user(username, hashed_password, role)

    return {"message": "User registered successfully"}


def login_user(username: str, password: str):
    """
    Authenticates user credentials
    """

    user = db.get_user(username)

    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return {
        "username": user["username"],
        "role": user["role"]
    }
