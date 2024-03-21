from django import forms
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, Testimonial, Partner, Faq, Privacy, WorkImage, SocialMedia

SOCIAL_MEDIA_CHOICES = [
    ('01', 'Facebook'),
    ('02', 'Twitter'),
    ('03', 'Instagram'),
    ('04', 'TikTok'),
    ('05', 'YouTube'),
    ('06', 'LinkedIn'),
]

STARS_REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['location', 'city', 'phone1', 'phone2', 'email', 'latitude', 'longitude']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number' }),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
        }

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'title1', 'title2', 'subtitle', 'description', 'insurance1', 'insurance2']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'insurance1': forms.TextInput(attrs={'class': 'form-control'}),
            'insurance2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['image1', 'image2', 'about', 'mision', 'vision', 'image_google', 'url_google']
        widgets = {
            'url_google': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title1', 'description1', 'title2', 'description2', 'title3', 'description3']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'description1': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'description2': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'description3': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['title1', 'number1', 'symbol1', 'title2', 'number2', 'symbol2', 'title3', 'number3', 'symbol3']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'number1': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol1': forms.TextInput(attrs={'class': 'form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'number2': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol2': forms.TextInput(attrs={'class': 'form-control'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'number3': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol3': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['image', 'image_large', 'image_small', 'title', 'description', 'description_finish']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ServiceDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())

class SubServiceForm(forms.ModelForm):
    class Meta:
        model = SubService
        fields = ['service', 'image', 'title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TestimonialForm(forms.ModelForm):
    stars = forms.ChoiceField(
        choices=STARS_REVIEW_CHOICES, 
        label='Stars', 
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    class Meta:
        model = Testimonial
        fields = ['image', 'name', 'location', 'stars', 'url', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id':'position'}),
            'stars': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class TestimonialDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['image']

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkImage
        fields = ['image']

class SocialMediaForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=SOCIAL_MEDIA_CHOICES, 
        label='Name', 
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    class Meta:
        model = SocialMedia
        fields = ['name', 'url']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
        }