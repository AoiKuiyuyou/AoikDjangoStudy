# coding: utf-8
from __future__ import absolute_import

# External imports
from django.http import HttpResponse


def CustomRequestHandler(request):
    """
    This request handler echoes request body in response body.

    :param request: Request object.

    :return: Response object.
    """
    # Read request body
    request_body = request.body

    # Return response
    return HttpResponse(request_body)
