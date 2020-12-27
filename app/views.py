from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from app.utils import url_list


class HomeView(View):
    def get(self, request):
        return render(request, 'app/app.html', {'url_list': url_list})


home = HomeView.as_view()
