
from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        
        # Verifica se todos os campos obrigatórios foram preenchidos
        if name and email and textarea:
            # Cria e salva o objeto Contact no banco de dados
            contact = Contact.objects.create(name=name, email=email, textarea=textarea)
            # Redireciona para a página de sucesso
            return redirect('success')
        else:
            # Se algum campo estiver em branco, exibe uma mensagem de erro
            return render(request, 'contact.html', {'error_message': 'Please fill in all required fields.'})
    
    return render(request, 'contact.html')

def success(request):
    return render(request, 'contact_success.html')