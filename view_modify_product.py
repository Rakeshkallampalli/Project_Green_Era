def modify_product(request, product_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            product = get_object_or_404(Product, id=product_id)
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.price = data.get('price', product.price)
            product.eco_certification = data.get('eco_certification', product.eco_certification)
            product.category = data.get('category', product.category)
            product.brand = data.get('brand', product.brand)
            product.weight = data.get('weight', product.weight)
            product.dimensions = data.get('dimensions', product.dimensions)
            product.material = data.get('material', product.material)
            product.manufacturing_location = data.get('manufacturing_location', product.manufacturing_location)
            product.packaging_type = data.get('packaging_type', product.packaging_type)
            product.recyclable = data.get('recyclable', product.recyclable)
            product.biodegradable = data.get('biodegradable', product.biodegradable)
            product.cruelty_free = data.get('cruelty_free', product.cruelty_free)
            product.energy_efficient = data.get('energy_efficient', product.energy_efficient)
            product.image_url = data.get('image_url', product.energy_efficient)
            product.save()
            return JsonResponse({'message': 'Product updated successfully! ID: ' + str(product.id)},
                                status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
