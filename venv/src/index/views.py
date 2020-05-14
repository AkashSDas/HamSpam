from django.shortcuts import redirect, render

from .forms import EmailForm
from .ml_model import ML_Model


def home_view(request, *args, **kwargs):
    form = EmailForm(request.POST or None)
    if form.is_valid():
            _model = ML_Model()
            content = form.cleaned_data.get('content')
            prediction = _model._predict(content)
            if prediction == 0:
                return redirect('/ham/')
            return redirect('/spam/')
    context = {'form': form}
    return render(request, 'index/home.html', context)

def ham_view(request, *args, **kwargs):
    return render(request, 'index/ham.html', {})

def spam_view(request, *args, **kwargs):
    return render(request, 'index/spam.html', {})
