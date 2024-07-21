def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = UserRating.objects.filter(product=product)
    is_user_added_review = UserRating.objects.filter(product=product,
                                                     user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'EcoFriendlyProducts/product_details.html', {'product': product, 'reviews': reviews, 'isUserAddedReview': is_user_added_review})
