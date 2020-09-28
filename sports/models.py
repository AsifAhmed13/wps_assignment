from django.db import models

# Create your models here.
class ChessGame(models.Model):
    Game_Number = models.IntegerField()
    winners_Name = models.TextField()

class CarromGame(models.Model):
    Game_Number = models.IntegerField()
    winners_Name = models.TextField()
