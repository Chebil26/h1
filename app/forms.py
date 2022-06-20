from django.forms import ModelForm
from .models import  Approval, Transfer

class TransferForm(ModelForm):
	class Meta:
		model = Transfer
		exclude = ('approved',)
		fields = '__all__'


class AprovalForm(ModelForm):
	class Meta:
		model = Approval
		fields = '__all__'
		exclude = ('approved',)