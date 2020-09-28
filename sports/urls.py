from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("chess",views.chess,name="chess"),
    path("carrom",views.carrom,name="carrom"),
    path("chess/addgame",views.chessgame,name="chessgame"),
    path("carrom/addgame",views.carromgame,name="carromgame"),
    path("carrom/eventreports",views.carromeventreport,name="carromreport"),
    path("chess/eventreports",views.chesseventreport,name="chessreport")
]