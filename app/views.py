from django.shortcuts import get_object_or_404, render

from app.models import Transfer

from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

from .forms import TransferForm, AprovalForm
# Create your views here.


class transfer_list(ListView):

    queryset = Transfer.objects.all()
    template_name="app/transfer_list.html"



class transfer_detail(DetailView):
    queryset = Transfer.objects.all()
    template_name = "app/transfer_detail.html"

#    def get_object(self):
#        id_= self.kwargs.get("id")
#       return get_object_or_404(Transfer, id=id_)



def index(request):

	form = TransferForm()

	if request.method == 'POST':
		form = TransferForm(request.POST , request.FILES)
		if form.is_valid():
			print(form)
			form.save()
			
	context = {'form':form}
	return render(request, 'app/index.html', context)



def aprove(request):

	form = AprovalForm()

	if request.method == 'POST':
		form = AprovalForm(request.POST)
		if form.is_valid():
			print(form)
			form.save()
			
	context = {'form':form}
	return render(request, 'app/aprove.html', context)




def home(request):


	return render(request, 'app/home.html', {})

