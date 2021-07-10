from django.forms import ModelForm
from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
