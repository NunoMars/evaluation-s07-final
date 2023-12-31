from django.db import models

# Create your models here.


class SentencesFr(models.Model):
    """Class to define the response sentences."""

    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral"),
    )
    sentence = models.TextField()
    sentence_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif"
    )

    def __str__(self):
        return f"{self.sentence}, {self.sentence_polarity}"


class SentencesEn(models.Model):
    """Class to define the response sentences."""

    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral"),
    )
    sentence = models.TextField()
    sentence_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif"
    )

    def __str__(self):
        return f"{self.sentence}, {self.sentence_polarity}"


class SentencesPt(models.Model):
    """Class to define the response sentences."""

    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral"),
    )
    sentence = models.TextField()
    sentence_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif"
    )

    def __str__(self):
        return f"{self.sentence}, {self.sentence_polarity}"


class SentencesEs(models.Model):
    """Class to define the response sentences."""

    CHOICES = (
        ("Positif", "Positif"),
        ("Negatif", "Negatif"),
        ("Neutral", "neutral"),
    )
    sentence = models.TextField()
    sentence_polarity = models.CharField(
        max_length=10, choices=CHOICES, default="Positif"
    )

    def __str__(self):
        return f"{self.sentence}, {self.sentence_polarity}"
