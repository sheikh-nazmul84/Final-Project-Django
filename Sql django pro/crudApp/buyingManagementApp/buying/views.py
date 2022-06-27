from django.shortcuts import render, redirect
from buying.forms import BuyingForm
from buying.models import Buying


# Create Buying.

def createBuying(request):
    print("Test")
    if request.method == "POST":
        form = BuyingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
            pass
    else:
        form = BuyingForm()
    return render(request, "index.html", {'form': form})


def show(request):
    buyings = Buying.objects.all()
    return render(request, "show.html", {"buyings": buyings})


def edit(request, srNo):
    buying = Buying.objects.get(srNo=srNo)
    return render(request, "edit.html", {"buying": buying})


def update(request, srNo):
    buying = Buying.objects.get(srNo=srNo)
    form = BuyingForm(request.POST, instance=buying)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {"buying": buying})


def delete(request, srNo):
    buying = Buying.objects.get(srNo=srNo)
    buying.delete()
    return redirect('/show')
