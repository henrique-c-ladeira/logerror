
import json
from django.http.response import JsonResponse


def getRequestBody(body):
    body_unicode = body.decode('utf-8')
    body = json.loads(body_unicode)
    return body


def internalError(*args):
    return JsonResponse({
        'error': 'Internal Server Error.',
        'message': ' '.join([f'{x}' for x in args])
    }, status=500)


def badRequest(*args):
    return JsonResponse({
        'error': 'Invalid or missing params:',
        'message': ' '.join([f'{x}' for x in args])
    }, status=400)


def methodNotAllowed():
    return JsonResponse({}, status=405)


def ok():
    return JsonResponse({}, status=201)
