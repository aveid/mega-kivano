from category.models import Category


def get_category(title):
    try:
        obj = Category.objects.get(title=title)
    except Category.DoesNotExist:
        obj = Category.objects.create(title=title)
    return obj
