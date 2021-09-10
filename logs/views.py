from django.shortcuts import render
from logs.models import ErrorLog
from .helpers import internalError, badRequest, getRequestBody, methodNotAllowed, ok
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

# Create your views here.


@csrf_exempt
def log(request):
    if (request.method != 'POST'):
        return methodNotAllowed()
    try:
        body = getRequestBody(request.body)
        error_log = ErrorLog.create(**body)
        error_log.save()
        return ok()
    except (ValidationError, TypeError) as error:
        return badRequest(error)
    except Exception as error:
        return internalError(error)
