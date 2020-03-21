from django.shortcuts import render
from FineSystemapp.forms import NewFineApply
from .models import *
# Create your views here.
def Home(request):
    return render(request,'FineSystemapp/index.html')
def Fine_Apply(request):
    form = NewFineApply()
    if request.method == 'POST':
        form = NewFineApply(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return Home(request)
        else:
            print("ERROR FROM INVALID")
    return render(request, 'FineSystemapp/Fine_Apply.html', {'form': form})

