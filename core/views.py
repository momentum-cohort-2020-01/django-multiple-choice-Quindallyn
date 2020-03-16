from django.shortcuts import render, redirect, get_object_or_404

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

def edit_deck (request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return redirect('decklist')
    else:
        form=DeckForm(instance=deck)
        context= {'form':form}
        return render(request, 'core/render-form.html', context=context)

def delete_deck (request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    deck.delete()
    return redirect('decklist')

def flashcard_list (request):
    flashcards=Flashcard.objects.all()
    context = {"flashcards":flashcards}
    return render(request, 'core/flashcard-list.html', context=context) 
