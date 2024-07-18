def add_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = Product(
                name=data.get('name'),
                description=data.get('description'),
                price=data.get('price'),
                eco_certification=data.get('eco_certification'),
                category=data.get('category'),
                brand=data.get('brand'),
                weight=data.get('weight'),
                dimensions=data.get('dimensions'),
                material=data.get('material'),
                manufacturing_location=data.get('manufacturing_location'),
                packaging_type=data.get('packaging_type'),
                recyclable=data.get('recyclable', False),
                biodegradable=data.get('biodegradable', False),
                cruelty_free=data.get('cruelty_free', False),
                energy_efficient=data.get('energy_efficient', False),
                image_url=data.get('image_url'),
            )
            product.save()
            return JsonResponse({'message': 'Product created successfully ID: ' + str(product.id)}, status=status.HTTP_201_CREATED)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
