from core.models import Product

class ProductService:

  @staticmethod
  def get_all(name: str):
    products = Product.objects.all()
  
    if name:
      products = products.filter(name__icontains=name)

    return products

  @staticmethod
  def delete(request,id: int):
    product = Product.objects.delete(id=id)
    return product