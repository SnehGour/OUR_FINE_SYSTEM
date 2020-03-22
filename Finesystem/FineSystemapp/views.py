from django.shortcuts import render
from FineSystemapp.forms import New_2FineApply
# Create your views here.
def Home(request):
    return render(request,'FineSystemapp/index.html')
def Fine_Apply(request):
    form = New_2FineApply()
    if request.method == 'POST':
        form = New_2FineApply(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return Home(request)
        else:
            print("ERROR FROM INVALID")
    return render(request, 'FineSystemapp/Fine_Apply.html', {'form': form})


def myview(request):
    queryset = ImageModel.objects.all()
    return render(request, 'template.html' , {'q':queryset})