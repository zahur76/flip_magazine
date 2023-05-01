from django import forms
from magazines.models import Magazines


class addMagazineForm(forms.ModelForm):
    class Meta:
        model = Magazines
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {"name": "Name"}

        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = f"{placeholders[field]} *"

            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-1 magazine-form-input mb-2 mt-2 text-left"
        
            self.fields[field].label = False
 