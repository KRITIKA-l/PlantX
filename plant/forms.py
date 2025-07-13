from django import forms
from .models import userplant

class UserPlantForm(forms.ModelForm):
    class Meta:
        model = userplant
        fields = '__all__' 

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
            'humidity': 'Humidity Level',
            'temperature_preference': 'Preferred Temperature',
            'planted_date': 'Date Planted',
            'last_watered': 'Last Watered On',
            'watering_frequency': 'Watering Frequency (days)',
            'water_reminder': 'Enable Water Reminders?',
            'last_fertilized': 'Last Fertilized On',
            'fertilizing_frequency': 'Fertilizing Frequency (days)',
            'height_cm': 'Plant Height (cm)',
            'is_flowering': 'Is Flowering?',
            'is_fruiting': 'Is Fruiting?',
            'current_status': 'Plant Health Status',
            'source': 'Plant Source',
            'notes': 'Additional Notes',
        }
    def __init__(self, *args, **kwargs):
        super(UserPlantForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Don't add 'form-control' to CheckboxInput (e.g. BooleanField)
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = existing_classes + ' form-control'


