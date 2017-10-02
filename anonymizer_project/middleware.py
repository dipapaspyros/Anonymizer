from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class AuthRequiredMiddleware(object):

    def process_request(self, request):
        if request.path.startswith('/admin/'):
            return None

        if request.path == reverse('login'):
            return None

        if request.path.startswith('/anonymizer/api/'):
            return None

        if not request.user.is_authenticated():
            return redirect(reverse('login'))

        return None

    def process_response(self, request, response):
        if request.path.startswith('/admin/'):
            return response

        if request.path == reverse('login'):
            return response

        if request.path.startswith('/anonymizer/api/'):
            return response

        if not request.user.is_authenticated():
            return redirect(reverse('login'))

        return response
