from django.db import models


class Question(models.Model):
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

