from django import forms
from .models import RentalProperty


class PropertyCreateForm(forms.ModelForm):
    class Meta:
        model = RentalProperty
        fields = ('prooerty_name', 'rent', 'address1',
                  'address2', 'address3', 'nearest_sta1', 'min_walk_from_sta1', 'area', 'layout', 'is_separated', 'has_indoor_laundry_space'#, 'photo1'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
