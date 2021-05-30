from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Listing
from .forms import ListingCreate


def about(request):
    return render(request, 'about.html', context={})


def home_page(request):
    context = {}
    heading_listings = Listing.objects.order_by('-list_date').filter(transactions__exact='2').all()[:5]

    featured_listings = Listing.objects.order_by('price').filter(transactions__exact='2').all()[:5]

    is_logged_in = request.user is not None and not request.user.is_anonymous
    return render(request, 'homepage.html',
                  {'context': context, 'heading_listings': heading_listings, 'featured_listings': featured_listings,
                   'is_logged_in': is_logged_in})


def listing_create(request):
    listing_create_form = ListingCreate()
    if request.method == 'POST':
        listing_create = ListingCreate(request.POST, request.FILES)
        if listing_create.is_valid():
            listing_create.save()
            return redirect('/listing/0/0/')
    is_logged_in = request.user is not None and not request.user.is_anonymous

    return render(request, 'listing/listing_create_update.html',
                  {'form': listing_create_form, 'submit': 'Adauga anunt', 'option': 'Adauga Anunt',
                   'is_logged_in': is_logged_in})


def listing_edit(request, id, origin_url='/listing/0/0/'):
    listing = Listing.objects.get(id=id)
    listing_edit_form = ListingCreate(instance=listing)
    if request.method == 'POST':
        listing_edit = ListingCreate(request.POST, instance=listing)
        if listing_edit.is_valid():
            listing_edit.save()
            return redirect(origin_url)

    is_logged_in = request.user is not None and not request.user.is_anonymous
    return render(request, 'listing/listing_create_update.html',
                  {'form': listing_edit_form, 'submit': 'Salveaza modificarile', 'option': 'Editeaza Anunt',
                   'is_logged_in': is_logged_in})


def listing_delete(request, id, origin_url='/listing/0/0/'):
    listing_delete = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing_delete.delete()
        return redirect(origin_url)

    is_logged_in = request.user is not None and not request.user.is_anonymous
    return render(request, 'listing/listing_delete.html',
                  {'form': listing_delete, 'is_logged_in': is_logged_in, 'option': 'Sterge Anunt'})


class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing/listing_details.html'
    context_object_name = 'prop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def listing_show(request, types, transactions, rooms='0', district='0'):

    # keywords
    searched = ''
    try:
        searched = str(request.POST['keywords'])
    except:
        pass
    keywords = Listing.objects.filter(
        Q(title__icontains=searched) | Q(description__icontains=searched) | Q(identifier__icontains=searched))

    # transactions
    if 'transactions' in request.POST.keys():
        transactions = request.POST.get('transactions')
    if transactions == '0':
        listings_transactions = Listing.objects.all()
    else:
        listings_transactions = Listing.objects.filter(transactions__in=transactions)

    # types
    if 'types' in request.POST.keys():
        types = request.POST.get('types')
    if types == '0':
        listings_types = Listing.objects.all()
    else:
        listings_types = Listing.objects.filter(types__in=types)

    # rooms
    if 'rooms' in request.POST.keys():
        rooms = request.POST.get('rooms')

    if rooms == '0':
        listings_rooms = Listing.objects.all()
    else:
        listings_rooms = Listing.objects.filter(rooms__in=rooms)

    # district
    if 'district' in request.POST.keys():
        district = request.POST.get('district')

    if district == '0':
        listings_district = Listing.objects.all()
    else:
        listings_district = Listing.objects.filter(district__in=district)

    # price
    min_price_value = 0
    max_price_value = 9999999999
    try:
        min_price_value = int(request.POST['min_price'])
    except:
        pass
    min_price = Listing.objects.filter(price__gte=min_price_value)
    try:
        max_price_value = int(request.POST['max_price'])
    except:
        pass
    max_price = Listing.objects.filter(price__lte=max_price_value)
    price_range = min_price.intersection(max_price)

    properties = listings_types.intersection(listings_transactions).intersection(listings_rooms).intersection(
        listings_district).intersection(price_range).intersection(keywords)

    # paginator
    paginator = Paginator(properties, 6)
    page = request.GET.get('page')
    properties = paginator.get_page(page)

    is_logged_in = request.user is not None and not request.user.is_anonymous

    return render(request, 'listing/listings_show.html',
                  {'properties': properties, 'is_logged_in': is_logged_in,
                   'path': request.get_full_path()})
