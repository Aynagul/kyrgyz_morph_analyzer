import markdown, sys, os

import time
from django.views.generic import ListView
from django.shortcuts import render
from analyzer.forms import *
from .models import *
from .backend.analyzer.main_analyzer import Word
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
        result = obj.search_word_db_for_word(obj)
        if obj.result_text == '[' + str(obj.word_without_punctuation) + ']' + obj.last_punctuation_mark:
            number_of_not_analyzed_word = number_of_not_analyzed_word + 1
        else:
            number_of_analyzed_word = number_of_analyzed_word + 1
        all_text = all_text + str(obj.result_text) + ' '
    print('all world number:')
    print(word_number)
    print('not analyzed number:')
    print(number_of_not_analyzed_word)
    print('analyzed number:')
    print(number_of_analyzed_word)
    symbol_counter = len(text)
    end = time.time() - start  ## собственно время работы программы
    print(end)  ## вывод времени
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


class AboutListView(ListView):
    context_object_name = 'posts'
    template_name = 'analyzer/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = navbar
        context['title'] = 'Биз жөнүндө'
        context['cat_selected'] = 0
        return context


def instruction(request):
    with open('analyzer/instruction.md', 'r') as f:
        md_file = f.read()
        md = markdown.Markdown(extensions=['toc'])
        html = md.convert(md_file)
        toc_html = md.toc
        headings = md.toc_tokens
        print(headings)

    headings_with_slugs = []
    for heading in headings:
        headings_with_slugs.append({'text': heading['name'], 'children': heading['children']})
        # print(headings_with_slugs)

    title = 'Нускама'
    context = {
        'title': title,
        'navbar': navbar,
        'content': html,
        'headings': headings_with_slugs,
    }
    return render(request, 'analyzer/instruction.html', context=context)


def handbook(request):
    title = 'Маалымдама'
    context = {
        'title': title,
        'navbar': navbar,
    }
    return render(request, 'analyzer/handbook.html', context=context)


def word_analyzer(request):
    title = 'Сөз анализатор'
    dict = {}
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['parameter_word']
            ans = Word(word)
            res = ans.search_word_db_for_word(ans)
            if not ans.symbols:
                dict = {
                    'word': word,
                    'root': ans.root,
                    'part_of_speech': ans.part_of_speech,
                    'all_symbols': ans.symbols_list,
                    'all_endings': '',
                    'text': ans.result_text
                }
                context = {
                    'title': title,
                    'navbar': navbar,
                    'form': form,
                    'dict': dict,
                }
                return render(request, 'analyzer/word_analyzer.html', context=context)
            dict = {
                'word': word,
                'root': ans.root,
                'part_of_speech': ans.part_of_speech,
                'all_symbols': ans.symbols_list,
                'all_endings': ans.symbols,
                'text': ans.result_text
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


