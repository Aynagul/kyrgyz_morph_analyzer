from django.contrib import admin
from . import models

from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django import forms
from .models import AllRoot, Tags, PartOfSpeech, NewRoot


class CsvImportFrom(forms.Form):
    csv_upload = forms.FileField()


class AllRootAdmin(admin.ModelAdmin):
    list_display = ('id', 'root', 'part_of_speech', 'get_tags')
    list_display_links = ('root', 'part_of_speech')
    search_fields = ('root',)
    list_filter = ('part_of_speech',)


    def get_tags(self, obj):
        return "\n".join([p.tag for p in obj.tag.all()])

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            for x in csv_data:
                filds = x.split(";")
                created = NewRoot.objects.update_or_create(
                    word=filds[0],
                    tags=filds[0],
                    is_done=1,
                )
        form = CsvImportFrom()
        data = {"form": form}
        return render(request, "analyzer/admin/csv_upload.html", data)


class EndingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tagid')
    list_display_links = ('name', 'tagid')
    search_fields = ('name',)
    list_filter = ('tagid',)


class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ('id', 'part_of_speech', 'get_tags')
    list_display_links = ('id', 'part_of_speech')
    search_fields = ('part_of_speech',)

    def get_tags(self, obj):
        return "\n".join([p.tag for p in obj.tag.all()])


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'priority', 'description')
    list_display_links = ('tag', 'priority', 'description')
    search_fields = ('tag', 'priority', 'description')

class NewRootAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'root', 'tags','endings', 'is_done')

    # def get_tags(self, obj):
    #     return "\n".join([p.tag for p in obj.tag.all()])

admin.site.register(Tags, TagsAdmin)
admin.site.register(PartOfSpeech, PartOfSpeechAdmin)
admin.site.register(AllRoot, AllRootAdmin)
admin.site.register(NewRoot, NewRootAdmin)
admin.site.register(models.Endings, EndingsAdmin)