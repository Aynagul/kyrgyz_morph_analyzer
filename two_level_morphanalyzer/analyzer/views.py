import markdown, sys, os
import markdown
import time
from django.views.generic import ListView
from django.shortcuts import render, redirect
from analyzer.forms import *
from .models import *
from django.http import JsonResponse

from .backend.analyzer.main_analyzer import Word
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import mimetypes
from django.http.response import HttpResponse

sys.path.append('analyzer/backend/analyzer/main_analyzer.py')

navbar = [{'title': 'Биз жөнүндө', 'url': 'about'},
          {'title': 'Нускама', 'url': 'instruction'},
          {'title': 'Маалымдама', 'url': 'handbook'},
          {'title': 'Сөз анализатор', 'url': 'word_analyzer'},
          {'title': 'Текст анализатор', 'url': 'text_analyzer'},
          ]

context = {}

file_result = ''
def text_reader(text):
    title = 'Текст анализатор'
    context = {
        'title': title,
        'navbar': navbar,
    }
    all_text = ''
    text = " ".join(text.split())
    words_list = text.split(' ')
    number_of_analyzed_word = 0
    number_of_not_analyzed_word = 0
    word_number = 0
    start = time.time()

    for word in words_list:
        word_number = word_number + 1
        word = str(word).strip()
        obj = Word(word)
        result = obj.search_word_db_for_text(obj)
        if obj.result_text == obj.first_punctuation_mark+ '[' + str(obj.word_without_punctuation) + ']' + obj.last_punctuation_mark:
            number_of_not_analyzed_word = number_of_not_analyzed_word + 1
        else:
            number_of_analyzed_word = number_of_analyzed_word + 1
        all_text = all_text + str(obj.result_text) + ' '

    with open('result.txt', mode='w') as file:
        file_result = file.write(all_text)


    symbol_counter = len(text)
    end = time.time() - start
    word_counter = len(words_list)
    context['text'] = text
    context['symbol_counter'] = symbol_counter
    context['word_counter'] = word_counter
    context['time'] = round(end, 3)
    context['all_text'] = all_text
    return context


def home(request):
    title = 'Башкы бет'
    context = {
        'title': title,
        'navbar': navbar,
        'cat_selected': 0,
    }
    return render(request, 'analyzer/home.html', context=context)

def about(request):
    title = 'Биз жөнүндө'

    with open("analyzer/about.md", "r", encoding="utf-8") as md_file:
        html = markdown.markdown(md_file.read(), extensions=["fenced_code"])
    context = {
        'title': title,
        'navbar': navbar,
        'html': html,
    }
    return render(request, 'analyzer/about.html', context=context)



def instruction(request):
        title = 'Нускама'

        with open("analyzer/instruction.md", "r", encoding="utf-8") as md_file:
            html = markdown.markdown(md_file.read(), extensions=["fenced_code"])
        context = {
            'title': title,
            'navbar': navbar,
            'html': html,
        }
        return render(request, 'analyzer/instruction.html', context=context)


def handbook(request):
    title = 'Маалымдама'

    with open("analyzer/handbook.md", "r", encoding="utf-8") as md_file:
        html = markdown.markdown(md_file.read(), extensions=["fenced_code"])
    context = {
        'title': title,
        'navbar': navbar,
        'html': html,
    }
    return render(request, 'analyzer/handbook.html', context=context)


def word_analyzer(request):
    title = 'Сөз анализатор'
    names = list(Tags.objects.values_list('tag', flat=True))
    partof_speech = list(PartOfSpeech.objects.values_list('part_of_speech', flat=True))
    print(names)
    dict = {}
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['parameter_word']
            ans = Word(word)
            res = ans.search_word_db_for_word(ans)
            print(ans.symbols_list_str)
            if not ans.symbols and not ans.symbols_list_str:
                dict = {
                    'word': word,
                    'root': ans.root,
                    'part_of_speech': ans.part_of_speech,
                    'all_symbols': ans.symbols_list_str,
                    'all_endings': '',
                    'text': ans.result_text,
                    'names': names,
                    'partof_speech': partof_speech
                }

                context = {
                    'title': title,
                    'navbar': navbar,
                    'form': form,
                    'dict': dict,
                }
                return render(request, 'analyzer/word_analyzer.html', context=context)
            else:
                dict = {
                    'word': word,
                    'root': ans.root,
                    'part_of_speech': ans.part_of_speech,
                    'all_symbols': ans.symbols_list_str,
                    'all_endings': ans.symbols_str,
                    'text': ans.result_text,
                    'names': names,
                    'partof_speech': partof_speech
                }
    else:
        form = WordForm()

    context = {
        'title': title,
        'navbar': navbar,
        'form': form,
        'dict': dict,
    }
    return render(request, 'analyzer/word_analyzer.html', context=context)


def text_analyzer(request):
    title = 'Текст анализатор'
    context = {
        'title': title,
        'navbar': navbar,
    }
    if request.method == 'POST':
        text = request.POST.get('text', '')
        file = request.FILES.get('upload_file')
        if file is None:
            text = str(text).strip()
            context = text_reader(text)
        else:
            text = file.read().decode('utf-8', errors='ignore')
            context = text_reader(text)

    return render(request, 'analyzer/text_analyzer.html', context=context)



def my_form_submission(request):
    if request.method == 'POST':
        # Получаем данные из формы
        input_word = request.POST['input_word']
        print('dddd', input_word)
        root = request.POST['root']
        print(root)
        endings = request.POST['endings']
        print(endings)
        partof_speech = request.POST['partof_speech']
        print(partof_speech)
        tags = request.POST['tags']
        print(tags)

        all_tags = partof_speech + ',' + tags
        print(all_tags)



        my_model = NewRoot(word=input_word, root=root, tags=all_tags, endings=endings)
        print(my_model)
        my_model.save()
        return redirect('word_analyzer')

    else:
        # Если запрос не типа POST, возвращаем форму
        return redirect('word_analyzer')


def download_file(request):
    filename = 'result.txt'
    filepath = filename
    path = open(filepath, 'r', encoding='UTF8')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
