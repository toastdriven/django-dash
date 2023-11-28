import json

from django.http import JsonResponse
from django.views.generic.base import View


class ApiError(Exception):
    pass


class DataValidationError(ApiError):
    pass


class ApiView(View):
    """
    Just a bit of sugar on top of plain ol' `View`.

    I don't want (or feel the need for) an API framework here.
    """

    bubble_exceptions = False
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
    ]

    def dispatch(self, request, *args, **kwargs):
        """
        Light override to the built-in `dispatch`, to allow for automatic
        JSON serialization of errors (as opposed to HTML).

        If you need the Django debug error, you can set the `bubble_exceptions`
        attribute on the class to `True`.

        Args:
            request (HttpRequest): The provided request.
            *args (list): The unnamed view arguments from the URLconf.
            **kwargs (dict): The named view arguments from the URLconf.

        Returns:
            HttpResponse: Typically, a JSON-encoded response.
        """
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as err:
            if self.bubble_exceptions:
                raise

            return self.render_error(str(err))

    def read_json(self, request):
        """
        Reads the request body & returns the decoded JSON.

        Args:
            request (HttpRequest): The received request

        Returns:
            dict: The decoded JSON body
        """
        # TODO: Probably should check the Content-Type.
        try:
            return json.loads(request.body.read())
        except ValueError:
            raise ApiError("Invalid JSON payload provided.")

    def render(self, data, status_code=200):
        """
        Creates a JSON response.

        Args:
            data (dict): The data to return as JSON
            status_code (int): The desired HTTP status code. Default is `200`.

        Returns:
            JsonResponse: The response for Django to provide to the user
        """
        return JsonResponse(data, status=status_code)

    def render_error(self, msgs, status_code=500):
        """
        Creates an error JSON response.

        Args:
            msgs (list|str): A list of message(s) to provide to the user. If a
                single string is provided, this will automatically get turned
                into a list.
            status_code (int): The desired HTTP status code. Default is `500`.

        Returns:
            JsonResponse: The error response for Django to provide to the user
        """
        if not isinstance(msgs, (list, tuple)):
            # In case of a single string.
            msgs = [msgs]

        return self.render(
            {
                "success": False,
                "errors": msgs,
            },
            status_code=status_code,
        )

    def validate(self, data):
        """
        A method for standardizing validation. Not automatically called
        anywhere.

        Expected behavior is to return the validated data on success, or to
        call `render_error` with failures.

        This **MUST** be implemented in the subclass by the user.

        Args:
            data (dict): The data provided by the user.

        Returns:
            dict: The validated data
        """
        raise NotImplementedError("Subclass must implement the 'validate' method.")

    def serialize(self, obj):
        """
        A method for standardizing serialization.

        A "rich" object (like a `Model`) is provided, & turned into a dict that
        is ready for JSON serialization.

        This **MUST** be implemented in the subclass by the user.

        Args:
            obj (Model): The object to serialize.

        Returns:
            dict: The data
        """
        raise NotImplementedError("Subclass must implement the 'validate' method.")

    def serialize_many(self, objs):
        """
        Like `serialize`, but handles serialization for many objects.

        Args:
            objs (iterable): An iterable of the objects to serialize.

        Returns:
            list: A list of serialized objects
        """
        data = []

        for obj in objs:
            data.append(self.serialize(obj))

        return data
