from . import models


def category(request):
    category = models.Category.objects.all()
    return {'category': category}
