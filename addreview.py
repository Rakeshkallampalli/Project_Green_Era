@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = UserRatingForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.verified_purchase = True  # or any logic to determine if purchase is verified
            review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = UserRatingForm()
    return redirect('product_detail', product_id=product_id)