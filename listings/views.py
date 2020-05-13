from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
    'listings' : page_obj
    }
    return render(request,'listings/listings.html',context)
 
def listing(request,listing_id): 
    return render(request,'listings/listing.html')

def search(request): 
    return render(request,'listings/search.html')    