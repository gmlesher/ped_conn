import base64

from django.core.exceptions import MiddlewareNotUsed 
from django.http import HttpResponse 
from django.conf import settings

AUTH_TEMPLATE = """
    <html>
        <title>Authentication Required</title> 
        <body> 
            Login credentials required. </br> 
            Please contact the site admin if unable to access.
        </body> 
    </html> """

class BasicAuthMiddleware(object): 
    def __init__(self, get_response): 
        self.get_response = get_response

    # If DEBUG is true, we're in dev. Raise MiddlewareNotUsed to remove
    # this middleware from the list.
    # TODO: This should probably be based off of the QA env once we hit
    # production
    if settings.DEBUG:
        raise MiddlewareNotUsed

    def _unauthed(self):
        response = HttpResponse(AUTH_TEMPLATE, content_type="text/html")
        response['WWW-Authenticate'] = 'Basic realm="Development"'
        response.status_code = 401
        return response

    def __call__(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return self._unauthed()
        else:
            authentication = request.META['HTTP_AUTHORIZATION']
            (auth_method, auth) = authentication.split(' ', 1)
            if 'basic' != auth_method.lower():
                return self._unauthed()
            auth = base64.b64decode(auth.strip()).decode('utf-8')
            username, password = auth.split(':', 1)
            if (
                username == settings.BASICAUTH_USERNAME and
                password == settings.BASICAUTH_PASSWORD
            ):
                return self.get_response(request)

            return self._unauthed()