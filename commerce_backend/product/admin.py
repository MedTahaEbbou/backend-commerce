from django.contrib import admin
from.models import Product,Category,Comment,Rating,Ads
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Ads)