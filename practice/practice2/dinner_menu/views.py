from django.shortcuts import render

# Create your views here.
def dinner_menu(request, menu, num):
    context = {
        'menu' : menu,
        'num' : num,
    }
    return render(request, 'dinner_menu.html', context)