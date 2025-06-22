from django import forms

from .models import Product
class ProductForm(forms.ModelForm):
    title  = forms.CharField(
                label = '', 
                widget=forms.TextInput(
                    attrs = {
                        "placeholder": "Your Product Title",
                        }   
                    )
            )
    
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs = {
                                "placeholder": "Your Description",
                                "Class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 50,
                            }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',

        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "R" in title :
    #         raise forms.ValidationError("This is not a valid title")
    #     if not "news" in title :
    #         raise forms.ValidationError("This is not a valid title")
        
    #     return title
        
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not (email.endswith(".edu") or email.endswith(".com")):
    #         raise forms.ValidationError("Email must end with .edu or .com")
    #     return email


        

class RawProductForm(forms.Form):
    title       = forms.CharField(
                        required=True,
                        label = '', 
                        widget=forms.TextInput(
                            attrs = {
                            "placeholder": "Your Product Title",
                            }   
                        )
                    )
    description = forms.CharField(
                        required=True, 
                        widget=forms.Textarea(
                            attrs = {
                                "placeholder": "Your Description",
                                "Class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 50,
                            }
                            )
                        )
    price       = forms.DecimalField(required=True)