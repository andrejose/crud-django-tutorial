from django.forms import ModelForm, Textarea
from django.forms.widgets import TextInput
from app.models import Carro
from django.utils.translation import gettext_lazy as _

# Create the form class.
class CarroForm(ModelForm):
	class Meta:
		model = Carro
		fields = ('modelo', 'marca', 'ano')
		widgets = {
			'modelo': TextInput(attrs={'class': 'form-control mb-3', 'autofocus': 'true'}),
			'marca': TextInput(attrs={'class': 'form-control mb-3'}),
			'ano': TextInput(attrs={'class': 'form-control  mb-3', 'type': 'number'}),
        }
		labels = {
			'modelo': 'Modelo',
		}
		#help_texts = {
		#	'modelo': 'Informar como consta no documento',
		#}