from django.urls import path

from mysite.views import bert, bert_output, bert_tag

urlpatterns = [
    path('input/', bert, name='input'),
    path('output/', bert_output, name='output'),
    path('tag/', bert_tag, name='tag'),


]