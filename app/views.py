from django.shortcuts import render

# Create your views here.


def home(request):
    '''
    This is the docstring to create documentation with 
    sphinx.
    '''
    return render(request, 'app/app.html')
