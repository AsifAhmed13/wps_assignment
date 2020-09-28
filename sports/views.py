from django.shortcuts import render
from .forms import GameForm
from django.http import HttpResponse
from .models import ChessGame,CarromGame
# Create your views here.
def index(request):
    return render(request,"sports/index.html")

def chess(request):
    return render(request,"sports/chess.html")

def carrom(request):
    return render(request,"sports/carrom.html")

def chessgame(request):
    if(request.method=="POST"):
        form = GameForm(request.POST)
        if(form.is_valid()):
            Game_Number = form.cleaned_data.get("Game_Number")
            winners_Name = form.cleaned_data.get("winners_Name")
            g = ChessGame()
            g.Game_Number = Game_Number
            g.winners_Name = winners_Name
            g.save()
            return render(request,"sports/success.html")
    return render(request,"sports/chessadd.html",{
        "forms": GameForm
    })

def carromgame(request):
    if(request.method=="POST"):
        form = GameForm(request.POST)
        if(form.is_valid()):
            Game_Number = form.cleaned_data.get("Game_Number")
            winners_Name = form.cleaned_data.get("winners_Name")
            g = CarromGame()
            g.Game_Number = Game_Number
            g.winners_Name = winners_Name
            g.save()
            return render(request,"sports/success.html")
    return render(request,"sports/carromadd.html",{
        "forms":GameForm
    })

def carromeventreport(request):
    c = CarromGame()
    objs = c.__class__.objects.all()
    return render(request,"sports/carromreport.html",{
        "objects_list": objs
    })

def chesseventreport(request):
    c = ChessGame()
    objs = c.__class__.objects.all()
    return render(request,"sports/chessreport.html",{
        "objects_list" : objs
    })



