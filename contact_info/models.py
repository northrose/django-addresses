from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "countries"


class Address(models.Model):
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.ForeignKey(State, null=True, blank=True)
    province = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    country_other = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return " ".join(filter(None, [", ".join(filter(
            None,
            [self.address1, self.address2, self.city, self.state.abbreviation])),
            self.postal_code]))

    class Meta:
        verbose_name_plural = "addresses"


class SalutationType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact_info_salutation_type"


class PhoneType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact_info_phone_type"


class Phone(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class Email(models.Model):
    address = models.EmailField()
    role = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.address


class Person(models.Model):
    salutation = models.ForeignKey(SalutationType, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)
    phone_numbers = models.ManyToManyField(Phone, blank=True)
    emails = models.ManyToManyField(Email, blank=True)

    def __str__(self):
        if self.first_name or self.last_name:
            return " ".join(filter(None, [self.first_name, self.last_name]))
        else:
            return self.title

    class Meta:
        verbose_name = "contact"
