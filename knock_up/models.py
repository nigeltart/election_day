from django.db import models


class Voter(models.Model):
    # RA2356
    elector_number = models.CharField("Elector Number", max_length=6)
    # Nigel
    forename = models.CharField("Forename", max_length=20)
    # Tart
    surname = models.CharField("Surname", max_length=20)
    # Flat 1, AAA House
    address1 = models.CharField("address1", max_length=30)
    # 999 The Street
    address2 = models.CharField("address2", max_length=30)
    # BN9 9ZZ
    postcode = models.CharField("Postcode", max_length=8)
    # G1 / G2
    support_level = models.CharField("Support Level", max_length=2)
    # False / True
    voted_yet = models.BooleanField("Voted yet?", default=False)
    #
    knocker = models.ForeignKey("knocker")


class Knocker(models.Model):
    # John
    forename = models.CharField("Forename", max_length=20)
    # Smith
    surname = models.CharField("Surname", max_length=20)
    # name@domain.com
    email_address = models.CharField("Email address", max_length=256)
    # 07123456789
    phone_number = models.CharField("Phone number", max_length=15)
    # 18:30
    start_time = models.DateTimeField("Start time")
    # 22:15
    end_time = models.DateTimeField("End time")