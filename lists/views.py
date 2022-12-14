from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.models import Item, List
from lists.forms import ExistingListItemForm, ItemForm


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    """Rendering list view"""
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == "POST":
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})


def new_list(request):
    """Creating new list"""
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        form.save()
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})
