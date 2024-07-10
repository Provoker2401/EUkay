from sileo.resource import Resource
from sileo.fields import ResourceTypeConvert, ResourceModelManager
from product.models import Category, Product
from product.forms import CategoryForm
from sileo.registration import register

class CategoryResource(Resource):
    query_set = Category.objects.all()
    fields = [
        'pk', 'slug', 'name'
    ]
    allowed_methods = [
        'get_pk', 'filter', 'create', 'update', 'delete'
    ]
    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']
    filter_fields = ['pk']
    form_class = CategoryForm

# register('product2', 'category2', CategoryResource, version='v1')
register(namespace='category', name='category', resource=CategoryResource, version='v1')