from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
import jwt, json, os
from .models import User

@csrf_exempt
def index(request):
    print("DEBUG minapp index was requested")
    # print(request.body)
    signupDecoded = json.loads(request.body)

    print(signupDecoded)

    newUser = User(
        email     = signupDecoded['email'],
        username  = signupDecoded['username'],
        password  = signupDecoded['pass'],
        firstname = signupDecoded['firstname'],
        animal    = signupDecoded['animal'],
    )
    try:
        newUser.save()
    except:
        print("Error during save. likely duplicate record. TODO: handle this error better.")
        return HttpResponse(status=500)
    
    # TODO: use an environment secret that is not also the db password.
    encoded = jwt.encode({'realuser': 'true'}, os.environ['DJANGOPGPASS']+"EXTRASAUCE", algorithm='HS256')
    resp = HttpResponse("Success. See x-auth-jwt header for your token.")
    resp['x-auth-jwt'] = encoded
    return resp

