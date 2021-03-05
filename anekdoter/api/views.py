import requests
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema

from models.models import *
from .serializers import *


class AnekdotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AnekdotSerializer

    def get_queryset(self):
        if self.action == 'list':
            count = self.request.query_params.get('count')
            if (count):
                return Anekdot.objects.all().order_by('-rating')[:int(count)]
        return Anekdot.objects.all().order_by('-rating')


class AnekdotGeneratorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=AnekdotGenerationSerializer,
                         responses={201: AnekdotSerializer})
    def create(self, requst):
        model = requst.data['model_name']
        t = requst.data['t']
        p = requst.data['p']
        k = requst.data['k']
        r_p = requst.data['rep_penalty']
        anek = requests.get('http://127.0.0.1:8000/anekdot', json={
            'model': model,
            't': t,
            'p': p,
            'k': k,
            'r_p': r_p,
        })
        texts = anek.json()['anekdot']
        new_aneks = []
        result = []
        for text in texts:
            tts_resp = requests.post(
                'http://127.0.0.1:8001/tts/', json={'text': text})
            tts_hash = tts_resp.json()['hash']
            new_anek = Anekdot(
                tts_hash=tts_hash,
                text=text,
                created_at=datetime.now(),
                t=t,
                p=p,
                k=k,
                rep_penalty=r_p
            )
            new_anek.save()
            new_aneks.append(new_anek)
            serializer = AnekdotSerializer(new_anek)
            result.append(serializer.data)
        return Response(data=result, status=201)


class AnekdotRatingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=AnekdotRatingSerializer, responses={201: ""})
    def create(self, request):
        anek_id = request.data['id']
        rating = request.data['rating']
        user = User.objects.get(username=request.user)
        if (rating != 1 and rating != -1):
            return Response(data={"error": "wrong rating"}, status=400)
        anek = Anekdot.objects.get(id=anek_id)

        if user in anek.rated_by.all():
            return Response(data={"error": "already rated"}, status=400)

        anek.rating = anek.rating + int(rating)
        anek.rated_by.add(user)
        anek.save()
        return Response(status=201)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserSerializer)
    def create(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=400)
