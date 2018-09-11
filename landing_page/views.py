from django.shortcuts import render


from django.http import HttpResponse,HttpResponseRedirect
from .forms import CadastroLandingForm

def index(request):
    if request.method == 'POST':
        form = CadastroLandingForm(request.POST)
        if form.is_valid():
            #se valido, salva no db e redireciona
            form.save()
            return HttpResponseRedirect('/thanks/')
        else:
            for field in form:
                print (field.label,field.errors) 
            return render(request, 'index.html', {'form_email': form,})
    else:
        form = CadastroLandingForm()
    return render(request, 'index.html', {'form_email': form})

def thanks(request):
    return render(request,'thanks.html')