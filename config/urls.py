"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.deck_list, name='decklist'),
    path('create/deck/', views.create_deck, name="create-deck"),
    path('create/flashcard/', views.create_flashcard, name="create-flashcard"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('edit/<int:pk>/deck/', views.edit_deck, name='edit-deck'),
    # path('deck/detail', views.deck_details, name="deck-details"),
    path('delete/<int:pk>/deck', views.delete_deck, name="delete-deck"),
    path('flashcards/list', views.flashcard_list, name="flashcard-list")
    path('delete/<int:pk>/flashcard', views.delete_deck, name="delete-flashcard"),
    path('edit/<int:pk>/flashcard/', views.edit_deck, name='edit-flashcard'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
