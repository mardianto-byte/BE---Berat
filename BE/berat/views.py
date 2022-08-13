from django.shortcuts import render, redirect
from .forms import BeratForm
from .models import Berat

# Create your views here.
def berat_form(request, id=0):
 
    # create object of form
    if request.method == "GET":
        if(id == 0):
            form = BeratForm()
        else:
            berat = Berat.objects.get(pk=id)
            form = BeratForm(instance=berat)
        return render(request, "berat_register/berat_form.html", {"form": form})
    else: 
        if(id == 0):
            form = BeratForm(request.POST)
        else : 
            berat = Berat.objects.get(pk=id)
            form = BeratForm(request.POST,instance = berat)
        # check if form data is valid
        if form.is_valid() :
            form.save()
        return redirect("/berat/list")

def berat_list(request) :
    list = Berat.objects.all().order_by('-tanggal')
    context = {"berat_list":list}
    return render(request,"berat_register/berat_list.html", context)