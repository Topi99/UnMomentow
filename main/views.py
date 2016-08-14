from django.shortcuts import render
from django.views.generic import View

class Welcome(View):
	def get(self, request):
		template_name = "main/welcome.html"
		context = {}
		return render(request, template_name)