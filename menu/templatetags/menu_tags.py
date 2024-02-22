from django.db.models import Q
from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(request, menu_name):
    current_url = request.path
    # Q(parent__isnull=True) & Q(
    menu_items = MenuItem.objects.filter(title__icontains=menu_name).all()
    
    menu_data = []
    for item in menu_items:
        menu_data.append(process_menu_item(item, current_url))
    
    return menu_data

def process_menu_item(menu_item, current_url):

    data = {
        'title': menu_item.title,
        'url': menu_item.url if menu_item.url else '',
        'is_active': current_url == menu_item.url or current_url.startswith(menu_item.url),
        'description': menu_item.description
    }
    
    if menu_item.children.exists():
        data['children'] = []
        for child_item in menu_item.children.all():
            data['children'].append(process_menu_item(child_item, current_url))
    
    return data



