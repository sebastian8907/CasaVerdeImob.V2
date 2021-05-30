from django import forms
from listings.models import Listing


class ListingCreate(forms.ModelForm):

    class Meta:
        model = Listing
        fields = "__all__"