from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from microapi import (
    ApiView,
    DataValidationError,
)


User = get_user_model()


class LoginView(ApiView):
    def validate(self, data):
        if "username" not in data:
            raise DataValidationError("Missing username")

        if "password" not in data:
            raise DataValidationError("Missing password")

        return data

    def post(self, request, *args, **kwargs):
        data = self.read_json(request)
        validated = self.validate(data)
        user = authenticate(validated["username"], validated["password"])

        if user is None:
            return self.render_error("Invalid credentials.")

        login(request, user)
        return self.render(
            {
                "success": True,
            }
        )


class SignUpView(ApiView):
    def post(self, request, *args, **kwargs):
        # FIXME: Implement this!
        # data = self.read_json(request)
        # validated = self.validate(data)
        return self.render({})


class ResetPasswordView(ApiView):
    def post(self, request, *args, **kwargs):
        # FIXME: Implement this!
        # data = self.read_json(request)
        # validated = self.validate(data)
        return self.render({})


class LogoutView(ApiView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return self.render(
            {
                "success": True,
            }
        )
