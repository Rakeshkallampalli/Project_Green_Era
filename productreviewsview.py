class ProductReviewsView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        ratings = UserRating.objects.filter(product=product)

        total_rating = sum([r.rating for r in ratings])
        average_rating = total_rating / len(ratings) if ratings else 0

        reviews = [{
            'user': rating.user.username,
            'rating': rating.rating,
            'review_title': rating.review_title,
            'review_text': rating.review_text,
            'verified_purchase': rating.verified_purchase,
            'created_at': rating.created_at
        } for rating in ratings]

        return JsonResponse({
            'average_rating': average_rating,
            'reviews': reviews
        }, status=200)