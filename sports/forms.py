from django import forms
from .models import ChessGame

class GameForm(forms.ModelForm):
    Game_Number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Game Number'}))
    Player1_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player1 Name'}))
    Player2_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Player2 Name'}))
    winners_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Name of the Winner'}))

    class Meta:
        model = ChessGame
        fields = [
            'Game_Number',
            'winners_Name',
        ]
