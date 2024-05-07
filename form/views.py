from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect

def IndexView(request):
    return render(request, 'index.html')

def client_form_view(request):
    if request.method == 'POST':
        # Extract data from POST request
        statut = request.POST.get('statut')
        nom = request.POST.get('fname')
        prenom = request.POST.get('lname')
        code_postal = request.POST.get('Code postal')
        adresse = request.POST.get('Adresse')
        age = request.POST.get('Age')
        ville = request.POST.get('Ville')
        email = request.POST.get('Email')
        numero_telephone = request.POST.get('Mobile / Fixe')
        surface_habitable_m2 = request.POST.get('Surface habitable (m2)')
        facture_electricite = request.POST.get('facture delectricite')
        type_toiture = request.POST.get('type de toiture')

        # Create CLient instance and save to database
        CLient.objects.create(
            statut=statut,
            Nom=nom,
            Prenom=prenom,
            code_Postal=code_postal,
            adresse=adresse,
            Age=age,
            Ville=ville,
            E_mail=email,
            N_de_téléphone=numero_telephone,
            Surface_habitable_m2=surface_habitable_m2,
            facture_d_electricite=facture_electricite,
            type_de_toiture=type_toiture
        )
        return redirect('home')
    
    return render(request,'form.html')