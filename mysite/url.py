from django.urls import path

from mysite.views import bert, bert_output

urlpatterns = [
    path('input/', bert, name='input'),
    path('output/', bert_output, name='output')

]