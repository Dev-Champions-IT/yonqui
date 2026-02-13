from django import forms
from .models import MemberApplication

from django_countries.fields import CountryField

# Nigerian states
NIGERIAN_STATES = [
    ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'),
    ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'),
    ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'),
    ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'FCT'), ('Gombe', 'Gombe'),
    ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'),
    ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'),
    ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'),
    ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'),
    ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'),
]

# Major Nigerian tribes (add more as needed)
NIGERIAN_TRIBES = [
    ('Yoruba', 'Yoruba'), ('Hausa', 'Hausa'), ('Igbo', 'Igbo'), ('Ijaw', 'Ijaw'),
    ('Kanuri', 'Kanuri'), ('Ibibio', 'Ibibio'), ('Tiv', 'Tiv'), ('Edo', 'Edo'),
    ('Nupe', 'Nupe'), ('Gwari', 'Gwari'), ('Jukun', 'Jukun'), ('Idoma', 'Idoma'),
    ('Fulani', 'Fulani'), ('Urhobo', 'Urhobo'), ('Itsekiri', 'Itsekiri'), ('Other', 'Other'),
]

from django_countries import countries

class MemberApplicationForm(forms.ModelForm):
    state = forms.ChoiceField(choices=NIGERIAN_STATES, widget=forms.Select(attrs={'class': 'form-control'}), required=True, label='State *')
    country = forms.ChoiceField(choices=list(countries), widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    tribe = forms.ChoiceField(choices=NIGERIAN_TRIBES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = MemberApplication
        fields = [
            'full_name', 'date_of_birth', 'gender', 'email', 'phone', 'address', 'city', 'state', 'country',
            'tribe', 'is_yoruba', 'passport_id_number', 'passport_id_type', 'passport_id_image',
            'occupation', 'education', 'reason_for_joining'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'reason_for_joining': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_yoruba': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
