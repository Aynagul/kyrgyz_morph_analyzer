import markdown, sys, os
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

    headings_with_slugs = []
    for heading in headings:
        slug = slugify(heading['name'])
        headings_with_slugs.append({'text': heading['name'], 'children': heading['children']})

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
            res = ans.search_word_db(ans.change_word)
            root = ans.root
            part_of_speech = ans.part_of_speech
            all_symbols = ans.symbols_list
            all_endings = ans.symbols
            text_res = ans.result_text
            dict = {
                'word': word,
                'root': root,
                'part_of_speech': part_of_speech,
                'all_symbols': all_symbols,
                'all_endings': all_endings,
                'text': text_res
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
            all_text = ''
            text = str(text).strip()
            words_list = text.split(' ')
            for word in words_list:
                word = str(word).strip()
                obj = Word(word)
                result = obj.search_word_db(obj.change_word)
                all_text = all_text + str(obj.result_text) + ' '
            context['text'] = text
            context['symbol_counter'] = len(text)
            context['word_counter'] = len(words_list)
            context['all_text'] = all_text
        else:
            text = file.read().decode('utf-8', errors='ignore')
            all_text = ''
            sentences = str(text).strip()
            words_list = sentences.split(' ')
            for word in words_list:
                word = str(word).strip()
                if not word == '':
                    ans = Word(word)
                    res = ans.search_word_db(ans.change_word)
                    all_text = all_text + str(ans.result_text) + ' '
            context['text'] = text
            context['symbol_counter'] = len(text)
            context['word_counter'] = len(words_list)
            context['all_text'] = all_text
    return render(request, 'analyzer/text_analyzer.html', context=context)


def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'result.txt'
    filepath = BASE_DIR + '/' + filename
    path = open(filepath, 'r', encoding='UTF8')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response