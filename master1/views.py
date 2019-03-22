from django.shortcuts import render
from.models import BankMaster
from django.db import IntegrityError


def show_bank(request):
    return render(request, 'bank1_master.html')


def bank_list(request):
    bank_name = request.POST.get("name")
    branch_name = request.POST.get("type")
    cs = BankMaster(bank_name=bank_name, branch_name=branch_name)
    cs.save()
    return render(request,'bank1_master.html')