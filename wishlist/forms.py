from django import forms
from .models import Wishlist


class AddWishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddWishlistForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
