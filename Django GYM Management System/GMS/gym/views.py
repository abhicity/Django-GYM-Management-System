from django.shortcuts import render, redirect
from .models import Equipment, MembershipPlan, Enquiry
from .forms import EnquiryForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'gym/home.html')

@login_required
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'gym/equipment_list.html', {'equipments': equipments})

@login_required
def membership_plans(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'gym/membership_plans.html', {'plans': plans})

def enquiry_form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnquiryForm()
    return render(request, 'gym/enquiry_form.html', {'form': form})
