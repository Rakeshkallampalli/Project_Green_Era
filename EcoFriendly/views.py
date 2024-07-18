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


