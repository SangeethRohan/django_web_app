from django import forms

from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',

        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Product Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Product Description'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Product Price'}),
        }

class RawProductForm(forms.Form):
    title       = forms.CharField(label = 'Title', widget=forms.TextInput(
                        attrs = {
                            "placeholder": "Your Product Title",
                        }
                    )
                )
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs = {
                                "Class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 50,
                            }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)