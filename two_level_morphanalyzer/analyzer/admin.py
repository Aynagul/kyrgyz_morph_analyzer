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
    list_display = ('root',)

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


admin.site.register(Tags)
admin.site.register(PartOfSpeech)
admin.site.register(AllRoot, AllRootAdmin)
admin.site.register(NewRoot)
admin.site.register(models.About)


