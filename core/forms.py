from django.forms import ModelForm
from .models import Deck, Flashcard

class DeckForm(ModelForm):

    class Meta:
        model = Deck
        fields = ('title',)

class FlashcardForm(ModelForm):

    class Meta:
        model = Flashcard
        fields = ('deck','side1', 'side2')