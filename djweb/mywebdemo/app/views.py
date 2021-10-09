import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from app.forms import LogMessageForm
from app.models import LogMessage
from django.views.generic import ListView

#def home(request):
#    return render(request, "app/index.html")

class HomeListView(ListView):
    model = LogMessage
    
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
        return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def hello(request, name):
    return render(
        request,
        'app/hello.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def log(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return render(request, "app/index.html")
    else:
        return render(request, "app/log.html", {"form": form})