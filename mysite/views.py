from django.http import HttpResponseRedirect

from mysite.froms import ModelForm
from django.shortcuts import render

# Create your views here.
import model
from mysite.models import Predictions


pred = []


def bert(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)

        if form.is_valid():
            context = form.cleaned_data['context']

            words, anms, ners = model.model_infer(context)

            pred.clear()

            pred.append(words)
            pred.append(anms)
            pred.append(ners)

            Predictions.objects.create(context=context)

            return HttpResponseRedirect('/mysite/output/')
            # return render(request, 'bertweb_input.html', {'form': form,
            #                                       'words': words,
            #                                       'anms': anms,
            #                                       'ners': ners})

    else:
        form = ModelForm()

    return render(request, 'bertweb_input.html', {'form':form})


def bert_output(request):
    return render(request, 'bertweb_output.html', {'words': pred[0],
                                                   'anms': pred[1],
                                                   'ners': pred[2]})

def bert_tag(request):
    return render(request, 'bertweb_tag.html')