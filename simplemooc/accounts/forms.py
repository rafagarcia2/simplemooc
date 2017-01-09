from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):

    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def cleaned_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 == password2:
            raise forms.ValidationError('A confirmação não está correta!')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        else:
            return user

    class Meta:
        model = User
        fields = ['username', 'email', ]


class EditAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError("Já existe um usuário com esse E-mail")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'name']
