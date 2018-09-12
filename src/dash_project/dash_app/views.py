from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView 
from .forms import HomeForm
from .models import Company


def company_article_list(request):
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['Query']
	form =HomeForm()
	args = {'form' :form,  }
	return render(request,"dash/home.html", args)



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        net_worth = dict()
        for company in Company.objects.all():
            if company.net_worth > 0:
                net_worth[company.name] = company.net_worth
    
        net_worth = sorted(net_worth.items(), key=lambda x: x[1])
        net_worth = dict(net_worth)

        data = {
            "article_labels":net_worth.keys(),
            "article_data": net_worth.values(),
        }
    
        return Response(data)
