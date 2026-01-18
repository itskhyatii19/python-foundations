from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from datetime import timedelta
import os

import auth
import db
import blacklist


def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

    jwt = JWTManager(app)

    db.init_db()

    # Swagger setup
    api = Api(
        app,
        title="Flask Auth API",
        version="1.0",
        description="Secure authentication API with JWT"
    )

    auth_ns = api.namespace("auth", description="Authentication operations")

    signup_model = api.model("Signup", {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "role": fields.String
    })

    login_model = api.model("Login", {
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    })

    # ----------- SWAGGER ROUTES -----------

    @auth_ns.route("/signup")
    class Signup(Resource):

        @auth_ns.expect(signup_model)
        def post(self):
            data = request.json
            return auth.signup_user(
                data["username"],
                data["password"],
                data.get("role", "user")
            )


    @auth_ns.route("/login")
    class Login(Resource):

        @auth_ns.expect(login_model)
        def post(self):
            data = request.json

            user = auth.login_user(
                data["username"],
                data["password"]
            )

            if not user:
                return {"error": "Invalid credentials"}, 401

            access_token = create_access_token(identity=user["username"])
            refresh_token = create_refresh_token(identity=user["username"])

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": user
            }


    @auth_ns.route("/logout")
    class Logout(Resource):

        @jwt_required()
        def post(self):
            jti = get_jwt()["jti"]
            blacklist.add_token(jti)
            return {"message": "Logged out"}


    @auth_ns.route("/dashboard")
    class Dashboard(Resource):

        @jwt_required()
        def get(self):
            return {"message": "Protected route"}


    # Blacklist check
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        return blacklist.is_blacklisted(jwt_payload["jti"])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
