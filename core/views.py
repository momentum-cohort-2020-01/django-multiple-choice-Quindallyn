from django.shortcuts import render

def deck_list (request):
    return render(request, 'core/decklist.html') 

# def flascard_runthrough (request):
#     return render(request, 'core/flashcardrunthrough.html')
