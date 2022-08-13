from django.shortcuts import render, redirect
from .forms import BeratForm
from .models import Berat

# Create your views here.
def berat_form(request):
 
    # create object of form
    if request.method == "GET":
        form = BeratForm()
        return render(request, "berat_register/berat_form.html", {"form": form})
    else: 
        form = BeratForm(request.POST)
        if form.is_valid() :
            form.save()
        return redirect("/berat/list")

def berat_list(request) :
    list = Berat.objects.all().order_by('-tanggal')
    context = {"berat_list":list}
    return render(request,"berat_register/berat_list.html", context)