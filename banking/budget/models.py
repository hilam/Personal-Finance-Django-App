from django.db import models
from django.utils.text import slugify

class Budget(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Budget, self).save()

class MonthlyBudget(models.Model):
    budget = models.ForeignKey('Budget')
    month = models.DateField()
    planned = models.DecimalField(max_digits=100, decimal_places=2)
    actual = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        forslug = "{0.budget}-{0.month}".format(self)
        self.slug = slugify(forslug)
        super(MonthlyBudget, self).save()

class SavingsGoal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    target = models.DecimalField(max_digits=100, decimal_places=2)
    allotted = models.DecimalField(max_digits=100, decimal_places=2)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug