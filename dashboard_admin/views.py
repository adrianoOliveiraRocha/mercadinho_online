from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User

@login_required
def index(request):
	user = User.objects.get(id=request.user.id)
	if user.is_staff:
		return render(request, 'dashboard_admin/index.html')
	else:
		return HttpResponse('Acesso não permitido!')

