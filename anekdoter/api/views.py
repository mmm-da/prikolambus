from django.core.exceptions import ObjectDoesNotExist
from drf_yasg import openapi
import requests
from datetime import datetime
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema

from models.models import *
from .serializers import *

from .invite import generate_invite


class AnekdotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AnekdotSerializer

    def get_queryset(self):
        if self.action == 'list':
            count = self.request.query_params.get('count')
            if count:
                return Anekdot.objects.all().order_by('-rating')[:int(count)]
        return Anekdot.objects.all().order_by('-rating')


class NextAnekdotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AnekdotNextSerializer

    def get_queryset(self):
        count = self.request.query_params.get('count')
        if not count:
            count = 1
        user = User.objects.get(username=self.request.user)
        q = Anekdot.objects.all()
        return q.exclude(rated_by=user)[:count]
 

class AnekdotGeneratorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=AnekdotGenerationSerializer,
                         responses={201: AnekdotSerializer})
    def create(self, requst):
        model_name = requst.data['model_name']
        t = requst.data['t']
        p = requst.data['p']
        k = requst.data['k']
        r_p = requst.data['rep_penalty']
        anek = requests.get('http://generator-api:8000/anekdot', params={
            # 'model_name': model_name,
            't': t,
            'p': p,
            'k': k,
            'repetition_penalty': r_p,
        })
        text = anek.json()['anekdot'][0]
        tts_resp = requests.post(
            'http://tts-proxy-api:8000/tts', json={'text': text})
        print(tts_resp.text)
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
        serialized = AnekdotSerializer(new_anek)
        return Response(serialized.data, status=201)


class AnekdotRatingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={201: ""},
                         request_body=AnekdotRatingSerializer)
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


class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('invite', description='Инвайт-код',
                          in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
    ], responses={201: "Учетная запись создана", 400: "Инвайт-код не годится"})
    def create(self, request):
        invite = request.query_params.get('invite')
        if invite:
            try:
                i = Invite.objects.get(code=invite)
            except ObjectDoesNotExist:
                return Response(status=400)
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
            i.delete()
            return Response(serialized.data, status=201)
        else:
            return Response(serialized._errors, status=400)

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

class InviteViewSet(viewsets.ViewSet):
    @swagger_auto_schema(responses={201: InviteSerializer})
    def list(self, request):
        invite = Invite.objects.create(code=generate_invite(), is_given=True)
        invite.save()
        serialized = InviteSerializer(invite)
        return Response(serialized.data, status=201)

