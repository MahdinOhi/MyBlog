from django import forms


class updateProfile(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField(widget=forms.Textarea)
    last_name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass