from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
import db


def role_required(required_role):
    """
    Decorator to restrict routes based on user role
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):

            # Verify JWT token
            verify_jwt_in_request()

            # Get logged in user
            current_user = get_jwt_identity()

            # Fetch user from DB
            user = db.get_user(current_user)

            if not user:
                return jsonify({"error": "User not found"}), 404

            # Check role
            if user["role"] != required_role:
                return jsonify({"error": "Access denied"}), 403

            return fn(*args, **kwargs)

        return wrapper

    return decorator
