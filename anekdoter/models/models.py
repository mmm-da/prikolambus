from django.db import models
from django.contrib.auth.models import User

class Anekdot(models.Model):
    # Текст анекдота
    text = models.CharField(max_length=1000)
    # ТТСный хэш, по которому получаем ссылку на звук
    tts_hash = models.CharField(max_length=500)

    # Рейтинг, постить можно -1 или 1
    rating = models.IntegerField(default=0)

    model_name = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField()

    t = models.FloatField(blank=True, default=0.9)
    k = models.IntegerField(blank=True, default=0)
    p = models.FloatField(blank=True, default=0.92)
    rep_penalty = models.FloatField(blank=True, default=1)
    rated_by = models.ManyToManyField(User, blank=True)

class Invite(models.Model):
    code = models.CharField(max_length=10)
    is_given = models.BooleanField(default=False)