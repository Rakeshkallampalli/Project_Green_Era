import os

from django.db.models import Sum
from pandas import pd

from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone

from EcoFriendly.models import Product
from EcoFriendlyProducts import settings


# Create your views here.
def main(request):
    today = timezone.now().date()
    session_key = f"visited_{today}"
    context = {
        'products': Product.objects.order_by('-created_at')[:8],
        'form': ContactForm(request.POST or None)
    }

    if request.user.is_authenticated:
        user_visit, created = UserDailyVisit.objects.get_or_create(
            user=request.user, date=today,
            defaults={'visits': 0}
        )
        if not request.session.get(session_key):
            user_visit.visits += 1
            user_visit.save()
            request.session[session_key] = True

        # Context data only for authenticated users
        context.update({
            'user_visits_today': user_visit.visits,
            'total_user_visits': UserDailyVisit.objects.filter(user=request.user).aggregate(Sum('visits'))[
                                     'visits__sum'] or 0,
            'total_visits_today': UserDailyVisit.objects.filter(date=today).aggregate(Sum('visits'))[
                                      'visits__sum'] or 0,
            'total_visits_all_time': UserDailyVisit.objects.aggregate(Sum('visits'))['visits__sum'] or 0,
            'user': request.user  # Passing the user object to the template
        })

    if request.method == 'POST' and context['form'].is_valid():
        data = context['form'].cleaned_data
        file_path = os.path.join(settings.EXCEL_FILES_DIR, 'contacts.xlsx')
        df = pd.read_excel(file_path) if os.path.exists(file_path) else pd.DataFrame(
            columns=['name', 'email', 'phone', 'message'])
        new_data = pd.DataFrame([data])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(file_path, index=False)
        return redirect('main')

    return render(request, 'EcoFriendlyProducts/index.html', context)


def viewAllProducts(request):
    # Query all products from the database
    products = Product.objects.all()

    # Pass the products to the template
    context = {
        'products': products
    }

    return render(request, 'EcoFriendlyProducts/shop.html',context)


def shop(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        no_results = not products.exists()  # Check if the filtered queryset is empty
    else:
        products = Product.objects.all()
        no_results = False  # Always false when not searching

    context = {
        'products': products,
        'query': query,
        'no_results': no_results  # Pass this flag to the template
    }
    return render(request, 'EcoFriendlyProducts/shop.html', context)