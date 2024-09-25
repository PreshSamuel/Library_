from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Homepage(View):

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)