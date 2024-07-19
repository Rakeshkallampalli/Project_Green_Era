def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            product = get_object_or_404(Product, id=product_id)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
