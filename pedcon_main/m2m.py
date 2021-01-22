from django.db import models

# classes for ManyToManyField variables
class ContactVia(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Options(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class ReleasedInfo(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class ServicesReceived(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class TypeOfDiscipline(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class MuscleTone(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Babinski(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class FootTendonGuard(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class LegsCrossedFlexionExtension(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class ATNR(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class TrunkExtension(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class HandsGrasp(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class HandsSupporting(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class HandsPulling(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Babkin(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Moro(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class FearParalysis(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class SpinalPerez(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class TLR(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Landau(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class BauerCrawling(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class SpinalGalant(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class STNR(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class FlyingAndLanding(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

# Speech Language Hx form
class Conditions(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class CurrentCare(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class DoesClient(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class DoesYourChild(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class SocialChar(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class BehavioralChar(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

# SSP form
class SoundSensitivity(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class GeneralSensitivity(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Sympathetic(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class DorsalVagal(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

