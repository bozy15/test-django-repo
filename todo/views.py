from django.shortcuts import redirect, render, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "todo/todo_list.html", context)


# Add new item to the todo list
def add_item(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    # Creates an instance of the form
    form = ItemForm()
    context = {"form": form}
    return render(request, "todo/add_item.html", context)


# Edit Item in the todo list
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST, instance=item)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    # Creates an instance of the form
    form = ItemForm(instance=item)
    context = {"form": form}
    return render(request, "todo/edit_item.html", context)


# toggle item status
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.complete = not item.complete
    item.save()
    return redirect(get_todo_list)


# delete item delete
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo_list")
