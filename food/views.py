from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import item
from .forms import ItemForm
# Create your views here.
#step 1
def index(request):
    item_list = item.objects.all()
   # template = loader.get_template('food/index.html')
    context ={
        'item_list': item_list
    }
    return render(request,'food/index.html', context)
  #  return HttpResponse(template.render(context, request))

def item_list(request):
    return HttpResponse("<h1>items are listed below</h1>")

def details(request, item_id):
     items =item.objects.get(pk=item_id)
     return render(request, 'food/details.html', {'item' : items})

def create_item(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form})
def  update_item(request, id):
    items = get_object_or_404(item, id=id)
    form = ItemForm(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form, 'item':items})

def delete_item(request, id):
    items =item.objects.get(id=id)

    if request.method == 'POST':
        items.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item':items})