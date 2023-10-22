from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.objects.all()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='review_list')


    @property
    def gpa_rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        return stars // count

    def __str__(self):
        return self.title


@property
def filtered_review_list(self):
    return self.review_list.filter(stats__gt=4)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review_list')
    stars = models.IntegerField(default=5, choices=((iterator_, '*' * iterator_)for iterator_ in range(1, 6)))

    def __str__(self):
        return self.product


