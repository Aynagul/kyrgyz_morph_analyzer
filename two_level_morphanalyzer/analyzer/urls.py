from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', AboutListView.as_view(), name='about'),
    path('instruction/', instruction, name='instruction'),
    path('handbook/', handbook, name='handbook'),
    path('word_analyzer/', word_analyzer, name='word_analyzer'),
    path('text_analyzer/', text_analyzer, name='text_analyzer'),
]
