from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Category, Product, HeroSlide, Inquiry
import json


def get_base_context():
    return {
        'categories': Category.objects.filter(is_active=True),
        'store_contacts': settings.STORE_CONTACTS,
        'whatsapp_number': settings.WHATSAPP_NUMBER,
        'uploadcare_public_key': settings.UPLOADCARE_PUBLIC_KEY,
    }


def home(request):
    ctx = get_base_context()
    ctx.update({
        'hero_slides': HeroSlide.objects.filter(is_active=True),
        'featured_products': Product.objects.filter(is_featured=True, is_active=True)[:8],
        'new_arrivals': Product.objects.filter(is_active=True)[:8],
        'page': 'home',
    })
    return render(request, 'store/home.html', ctx)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True)

    # Filters
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort', 'newest')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')

    ctx = get_base_context()
    ctx.update({
        'category': category,
        'products': products,
        'sort': sort,
        'page': 'category',
    })
    return render(request, 'store/category.html', ctx)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:4]

    ctx = get_base_context()
    ctx.update({
        'product': product,
        'related_products': related,
        'page': 'product',
    })
    return render(request, 'store/product_detail.html', ctx)


def search(request):
    q = request.GET.get('q', '').strip()
    products = Product.objects.none()
    if q:
        products = Product.objects.filter(
            is_active=True
        ).filter(
            name__icontains=q
        ) | Product.objects.filter(
            is_active=True
        ).filter(
            description__icontains=q
        ) | Product.objects.filter(
            is_active=True
        ).filter(
            tags__icontains=q
        )

    ctx = get_base_context()
    ctx.update({'products': products, 'query': q, 'page': 'search'})
    return render(request, 'store/search.html', ctx)


def about(request):
    ctx = get_base_context()
    ctx['page'] = 'about'
    return render(request, 'store/about.html', ctx)


def contact(request):
    ctx = get_base_context()
    ctx['page'] = 'contact'
    return render(request, 'store/contact.html', ctx)


@require_POST
def submit_inquiry(request):
    try:
        data = json.loads(request.body)
        inq = Inquiry.objects.create(
            name=data.get('name', ''),
            phone=data.get('phone', ''),
            email=data.get('email', ''),
            message=data.get('message', ''),
        )
        product_slug = data.get('product_slug')
        if product_slug:
            try:
                inq.product = Product.objects.get(slug=product_slug)
                inq.save()
            except Product.DoesNotExist:
                pass
        return JsonResponse({'success': True, 'message': 'Inquiry sent successfully!'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)


def all_products(request):
    products = Product.objects.filter(is_active=True)
    sort = request.GET.get('sort', 'newest')
    cat_slug = request.GET.get('cat', '')

    if cat_slug:
        products = products.filter(category__slug=cat_slug)
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')

    ctx = get_base_context()
    ctx.update({'products': products, 'sort': sort, 'selected_cat': cat_slug, 'page': 'products'})
    return render(request, 'store/products.html', ctx)
