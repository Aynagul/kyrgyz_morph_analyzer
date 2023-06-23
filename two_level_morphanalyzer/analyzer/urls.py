from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('instruction/', instruction, name='instruction'),
    path('handbook/', handbook, name='handbook'),
    path('word_analyzer/', word_analyzer, name='word_analyzer'),
    path('text_analyzer/', text_analyzer, name='text_analyzer'),
    path('word_analyzer/form', my_form_submission, name='my_form_submission'),
    path('text_analyzer/download_file/', download_file, name='download_file')
]
