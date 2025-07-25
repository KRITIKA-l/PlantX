from django import forms
from .models import userplant

class UserPlantForm(forms.ModelForm):
    class Meta:
        model = userplant
        exclude = ['user', 'deleted_at','deleted']

        widgets = {
            'planted_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'last_watered': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'last_fertilized': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        labels = {
            'nickname': 'Plant Nickname',
            'plant_type': 'Plant Type',
            'custom_image': 'Upload Plant Image',
            'location': 'Location (Indoor/Outdoor)',
            'sunlight': 'Sunlight Level',
            'planted_date': 'Date Planted',
            'last_watered': 'Last Watered On',
            'watering_frequency': 'Watering Frequency (days)',
            'last_fertilized': 'Last Fertilized On',
            'fertilizing_frequency': 'Fertilizing Frequency (days)',
            'is_flowering_and_fruiting': 'Flowering or Fruiting?',
            'notes': 'Additional Notes',
        }
    def __init__(self, *args, **kwargs):
        super(UserPlantForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Don't add 'form-control' to CheckboxInput (e.g. BooleanField)
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = existing_classes + ' form-control'


