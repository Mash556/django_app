from django.shortcuts import render

from .templatetags.menu_tags import draw_menu

def my_view(request, menu_name=None):
    if 'q' in request.GET:
        menu_name = request.GET['q']
    
    if menu_name:
        menu_items = draw_menu(request, menu_name)
    else:
        menu_items = draw_menu(request, '')
    return render(request, 'home.html', {'menu_items': menu_items})
