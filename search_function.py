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
