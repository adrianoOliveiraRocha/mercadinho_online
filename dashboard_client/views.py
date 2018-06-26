from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from django.contrib import messages
from core.utils import Utils
from django.urls import reverse
from accounts.forms import ClientForm


@login_required
def index(request):
	return render(request, 'dashboard_client/index.html')


@login_required
def my_data(request):
	client = User.objects.get(id=request.user.id)
	form = ClientForm(instance=client)
	context = {'form': form}
	return render(request, 'dashboard_client/my_data.html',
		context)
	