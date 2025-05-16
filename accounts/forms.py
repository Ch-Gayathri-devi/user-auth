from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=50, required=True)
    state = forms.CharField(max_length=50, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    user_type = forms.ChoiceField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture',
                 'address_line1', 'city', 'state', 'pincode', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = self.cleaned_data['user_type'] == 'patient'
        user.is_doctor = self.cleaned_data['user_type'] == 'doctor'
        if commit:
            user.save()
            if user.is_patient:
                Patient.objects.create(user=user)
            elif user.is_doctor:
                Doctor.objects.create(user=user)
        return user