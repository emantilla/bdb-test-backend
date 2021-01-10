
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import Event, Category, Tipology
from django.http import JsonResponse
from event.serializers import CategorySerializer, EventSerializer, TipologySerializer

import json

# Create your views here.

@csrf_exempt
def add_user_view(request):
    message = ""
    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=email, password=password)
        user_model.email = email
        user_model.save()
        message = 'Usuario Registrado'

    return JsonResponse({'message':message})

@csrf_exempt
def login_user_view(request):
    message = ""
    status_code = status.HTTP_200_OK
    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser['email']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = 'usuario logeado: ' + str(user.pk)
        else:
            message = 'Usuario o contrasenia incorrectos.'
            status_code = status.HTTP_401_UNAUTHORIZED

    return JsonResponse({'message': message, 'id':user.pk}, status=status_code)


@csrf_exempt
def all_events_view(request):
    if request.method == 'GET':
        user = request.GET.get('userId')
        event_list = Event.objects.filter(creation_user=user).order_by('-creation_date')
        serializer = EventSerializer(event_list, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def add_event_view(request):
    if request.method == 'POST':
        jsonEvent = json.loads(request.body.decode('utf-8'))
        name = jsonEvent['name']
        detail = jsonEvent['detail']
        place = jsonEvent['place']
        address = jsonEvent['address']
        start_date = jsonEvent['start_date']
        end_date = jsonEvent['end_date']
        category_type = jsonEvent['category_type']
        event_type = jsonEvent['event_type']
        creation_user = jsonEvent['creation_user']

        category_model = Category.objects.get(pk=category_type)
        tipology_model = Tipology.objects.get(pk=event_type)
        user_model = User.objects.get(pk=creation_user)

        event_model = Event()
        event_model.name = name
        event_model.detail = detail
        event_model.place = place
        event_model.address = address
        event_model.start_date = start_date
        event_model.end_date = end_date
        event_model.category_type = category_model
        event_model.event_type = tipology_model
        event_model.creation_user = user_model
        event_model.save()
        message = 'Evento Registrado'

    return JsonResponse({'message': message})


@csrf_exempt
def edit_event_view(request):
    message = ""
    if request.method == 'POST':
        jsonEvent = json.loads(request.body.decode('utf-8'))
        id= jsonEvent['id']
        name = jsonEvent['name']
        detail = jsonEvent['detail']
        place = jsonEvent['place']
        address = jsonEvent['address']
        start_date = jsonEvent['start_date']
        end_date = jsonEvent['end_date']
        category_type = jsonEvent['category_type']
        event_type = jsonEvent['event_type']
        creation_user = jsonEvent['creation_user']

        category_model = Category.objects.get(pk=category_type)
        tipology_model = Tipology.objects.get(pk=event_type)
        user_model = User.objects.get(pk=creation_user)

        event_model = Event.objects.get(pk=id)
        event_model.name = name
        event_model.detail = detail
        event_model.place = place
        event_model.address = address
        event_model.start_date = start_date
        event_model.end_date = end_date
        event_model.category_type = category_model
        event_model.event_type = tipology_model
        event_model.creation_user = user_model
        event_model.save()
        message = 'Evento: ' + str(event_model.pk) + ' actualizado'

    return JsonResponse({'message': message})


@csrf_exempt
def delete_event_view(request):
    message = ""
    if request.method == 'POST':
        jsonEvent = json.loads(request.body.decode('utf-8'))
        id = jsonEvent['id']
        event_model = Event.objects.get(pk=id).delete()
        message = 'Evento:' + id + ' eliminado'

    return JsonResponse({'message': message})


@csrf_exempt
def category_event_view(request):
    if request.method == 'GET':
        category_model = Category.objects.all()
        serializer = CategorySerializer(category_model, many=True)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def tipology_event_view(request):
    if request.method == 'GET':
        typology_model = Category.objects.all()
        serializer = TipologySerializer(typology_model, many=True)

    return JsonResponse(serializer.data, safe=False)


