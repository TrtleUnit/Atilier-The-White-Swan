from urllib.parse import urlencode

from django.shortcuts import render

# Placeholder catalogue until there is a Product model.
CATEGORIES = {
    'armband': 'Armband',
    'ketting': 'Ketting',
}

_SAMPLE = [
    {'name': 'Armband zilver', 'price': 100, 'category': 'armband', 'image': 'img/product-armband-1.jpg'},
    {'name': 'Armband zilver', 'price': 100, 'category': 'armband', 'image': 'img/product-armband-2.jpg'},
    {'name': 'Zilveren ketting', 'price': 100, 'category': 'ketting', 'image': 'img/product-ketting-1.jpg'},
    {'name': 'Zilveren ketting', 'price': 100, 'category': 'ketting', 'image': 'img/product-ketting-2.jpg'},
]
PRODUCTS = _SAMPLE * 3


def index(request):
    return render(request, 'home/index.html')


def producten(request):
    selected = [c for c in request.GET.getlist('categorie') if c in CATEGORIES]
    products = [p for p in PRODUCTS if not selected or p['category'] in selected]

    # One chip per active filter; clicking it removes just that filter.
    chips = []
    for cat in selected:
        rest = [('categorie', c) for c in selected if c != cat]
        chips.append({
            'label': CATEGORIES[cat].lower(),
            'url': f'?{urlencode(rest)}' if rest else request.path,
        })

    return render(request, 'producten/producten.html', {
        'products': products,
        'categories': CATEGORIES.items(),
        'selected': selected,
        'chips': chips,
    })


def workshops(request):
    return render(request, 'workshops/workshops.html')


def contact(request):
    return render(request, 'contact/contact.html')
