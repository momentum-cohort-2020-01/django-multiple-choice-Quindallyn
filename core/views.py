from django.shortcuts import render

from .models import Deck, Flashcard

def deck_list (request):
    decks=Deck.objects.all()
    context = {"decks":decks}
    return render(request, 'core/decklist.html', context=context) 

# def flascard_runthrough (request):
#     return render(request, 'core/flashcardrunthrough.html')
