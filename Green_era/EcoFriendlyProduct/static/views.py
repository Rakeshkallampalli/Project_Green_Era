import json
import os
from django.utils import timezone

import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


from django.db.models import Sum

from Green_era.EcoFriendlyProduct.models import User


class Product:
    pass


class UserRating:



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