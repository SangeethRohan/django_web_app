from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_create_view(request, *args, **kwargs):

    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)

        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)

        else:
            print(my_form.errors)

    context = {
        "form": my_form,
    }
    return render(request, 'products/product_create.html', context)


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

def product_detail_view(request, *args, **kwargs):


    obj = Product.objects.get(id=2)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price": obj.price,
    #     "summary": obj.summary,
    # }
    context = {
        "object": obj,
        "title": obj.title,
        "description": obj.description,
        "price": obj.price,
        "summary": obj.summary,
    }
    return render(request, 'products/product_detail.html', context)