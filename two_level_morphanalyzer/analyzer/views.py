import markdown, sys
from django.views.generic import ListView
from django.shortcuts import render
from analyzer.forms import *
from .models import *
from .backend.analyzer.main_analyzer import Word

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
        'navbar': navbar
    }
    return render(request, 'analyzer/home.html', context=context)


class AboutListView(ListView):
    model = About
    context_object_name = 'posts'
    template_name = 'analyzer/about.html'
    print(model)

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
        print(html)
        toc_html = md.toc
        headings = md.toc_tokens
        # print(headings)

    # Convert each heading to a dictionary with its text and slug
    # This will be used to create anchor links for the sidebar
    headings_with_slugs = []
    for heading in headings:
        slug = slugify(heading['name'])
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


            print(word)
    else:
        form = WordForm()

    context = {
        'title': title,
        'navbar': navbar,
        'form': form,
        'dict' : dict,
    }
    return render(request, 'analyzer/word_analyzer.html', context=context)


def text_analyzer(request):
    title = 'Текст анализатор'
    context = {
        'title': title,
        'navbar': navbar,
    }
    if request.method == 'POST':
        if 'text_submit' in request.POST:
            form = TextFileForm(request.POST)
            if form.is_valid():
                sentences = form.cleaned_data['text']
                sentences = str(sentences).strip()
                all_text = ''
                text = ''
                words_list = sentences.split(' ')
                for word in words_list:
                    word = str(word).strip()
                    ans = Word(word)
                    res = ans.search_word_db(ans.change_word)
                    all_text = all_text + str(ans.result_text) + ' '

                dict = {
                    'sentences': sentences,
                    'res': all_text
                }

                results = {'text': text, 'word_count': len(words_list)}
                context['text'] = text
                context['results'] = results
                context['form'] = form
                context['dict'] = dict
                return render(request, 'analyzer/text_analyzer.html', context=context)
        elif 'file_submit' in request.POST:
            uploaded_file = request.FILES['file']
            text = uploaded_file.read().decode('utf-8', errors='ignore')
            sentences = str(text).strip()
            all_text = ''
            text = ''
            words_list = sentences.split(' ')
            for word in words_list:
                word = str(word).strip()
                if not word == '':
                    ans = Word(word)
                    res = ans.search_word_db(ans.change_word)
                    all_text = all_text + str(ans.result_text) + ' '

            file = open("myfile.txt", 'w', encoding='UTF8')
            file.write(str(all_text))
            file.close()
            dict = {
                'sentences': sentences,
                'res': all_text
            }
            results = {'file_name': uploaded_file.name, 'file_size': uploaded_file.size}
            context['uploaded_file'] = uploaded_file
            context['file_name'] = uploaded_file
            context['file_size'] = uploaded_file.size
            context['dict'] = dict
            return render(request, 'analyzer/text_analyzer.html', context=context)
    else:
        form = TextFileForm()
        context['form'] = form
        return render(request, 'analyzer/text_analyzer.html', context=context)
