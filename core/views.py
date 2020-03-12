from django.shortcuts import render, redirect

from .models import Deck, Flashcard
from .forms import DeckForm, FlashcardForm

def deck_list (request):
    flashcards=Flashcard.objects.all()
    decks=Deck.objects.all()
    context = {"decks":decks, "flashcards":flashcards}
    return render(request, 'core/decklist.html', context=context) 

def create_deck (request):
    if request.method =="POST":
        form=DeckForm(request.POST)
        if form.is_valid():
            deck=form.save(commit=False)
            deck.user=request.user
            deck.save()
            return redirect('/')
    else:
        form=DeckForm()
        context= {'form':form}
        return render(request, 'core/render-form.html', context=context)

def create_flashcard (request):
    if request.method =="POST":
        form=FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=FlashcardForm()
        context= {'form':form}
        return render(request, 'core/render-form.html', context=context)

def deck_details (request):
    pass

# def flascard_runthrough (request):
#     return render(request, 'core/flashcardrunthrough.html')
