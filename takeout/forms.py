from django import forms
from .models import Shop

class ShopCreateForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['address'].widget.attrs.update({'rows':'2'})
        self.fields['hours'].widget.attrs.update({'rows':'3'})