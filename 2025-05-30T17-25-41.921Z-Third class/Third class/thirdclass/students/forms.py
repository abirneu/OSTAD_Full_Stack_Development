# students/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__'
        #exclude = ['age'] # Exclude the 'age' field from the form
        fields = ['name','age', 'email', 'profile_pic', 'dob']
        
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'age': 'Age',
            'profile_pic': 'Profile Picture'
        }
        # Adding custom widgets for better UI
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }
       
