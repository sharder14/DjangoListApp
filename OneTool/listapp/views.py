from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food,List
from .forms import FoodForm, ListForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
'''
def home(request):
    return render(request, "home.html", {})
'''

def home(request):
    def get_queryset(self):
        return List.objects.filter(acct_active=1, acct_user=request.user)

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to the list!'))
            r=render(request, 'home.html', {'all_items': all_items})
            return HttpResponse(r)

        else:
            return "ERROR"
    
    else:
        all_items = List.objects.all
        r=render(request, 'home.html', {'all_items': all_items})
        return HttpResponse(r)


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted.'))
    return redirect('home')