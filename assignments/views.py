
from django.shortcuts import render, redirect
from .forms import MemberApplicationForm

# Create your views here.

def apply_membership(request):
	if request.method == 'POST':
		form = MemberApplicationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'membership_success.html')
	else:
		form = MemberApplicationForm()
	return render(request, 'apply_membership.html', {'form': form})
