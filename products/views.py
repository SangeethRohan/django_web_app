from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import Http404

# Create your views here.

def product_create_view(request):
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('create')
    else:
        form = RawProductForm()

    context = {
        "form": form,
    }
    return render(request, 'products/product_create.html', context)

def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }
    return render(request, 'products/product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "products/product_list.html",context)

def product_detail_view(request, *args, **kwargs):

    obj = Product.objects.get(id=30)
    context = {
        "object": obj,
        "title": obj.title,
        "description": obj.description,
        "price": obj.price,
        "summary": obj.summary,
    }
    return render(request, 'products/product_detail.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }

    return render(request, "products/product_delete.html",context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    obj = Product.objects.get(id=24)
    
    initial_data = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price
    }

    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('create')
    else:
        form = RawProductForm(initial=initial_data)

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request, *args, **kwargs):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)

# def product_create_view(request, *args, **kwargs):

#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()  # Reset the form after saving 
#     context = {
#         "form": form,
#     }
#     return render(request, 'products/product_create.html', context)

