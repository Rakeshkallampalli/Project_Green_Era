import json
import os
from django.utils import timezone


from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from ecoFriendly import settings
from .forms import CustomPasswordResetForm
from .models import Product, UserRating, User, UserDailyVisit
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class AddRatingView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = get_object_or_404(User, id=data['user_id'])
        product = get_object_or_404(Product, id=data['product_id'])
        rating = data.get('rating')
        review_title = data.get('review_title', '')
        review_text = data.get('review_text', '')
        verified_purchase = data.get('verified_purchase', False)

        UserRating.objects.create(
            user=user,
            product=product,
            rating=rating,
            review_title=review_title,
            review_text=review_text,
            verified_purchase=verified_purchase
        )

        return JsonResponse({'message': 'Rating added successfully'}, status=201)

    @method_decorator(csrf_exempt, name='dispatch')
    class ModifyRatingView(View):
        def put(self, request, rating_id):
            data = json.loads(request.body)
            rating = get_object_or_404(UserRating, id=rating_id)

            rating.rating = data.get('rating', rating.rating)
            rating.review_title = data.get('review_title', rating.review_title)
            rating.review_text = data.get('review_text', rating.review_text)
            rating.verified_purchase = data.get('verified_purchase', rating.verified_purchase)

            rating.save()

            return JsonResponse({'message': 'Rating modified successfully'}, status=200)

    @method_decorator(csrf_exempt, name='dispatch')
    class DeleteRatingView(View):
        def delete(self, request, rating_id):
            rating = get_object_or_404(UserRating, id=rating_id)
            rating.delete()
            return JsonResponse({'message': 'Rating deleted successfully'}, status=200)


def generate_random_password(param, param1):
    pass


def send_password_reset_email(email, new_password):
    pass


def forgot_password(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = generate_random_password(8, 20)
                send_password_reset_email(email, new_password)
                user.set_password(new_password)
                user.save()
                return render(request, 'EcoFriendlyProducts/forgot_password.html', {
                    'form': form,
                    'success_message': 'A password reset email has been sent to the provided email address.'
                })
            except User.DoesNotExist:
                form.add_error('email', 'No account found with that email address.')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'EcoFriendlyProducts/forgot_password.html', {'form': form})

def forgot_password_view(request):
    form = CustomPasswordResetForm()
    return render(request, 'EcoFriendlyProducts/forgot_password.html', {'form': form})