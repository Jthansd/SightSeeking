from django.conf import settings
from django.db import models


# ============================================================
# LOOKUP TABLES
# ============================================================

class SpeciesCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True
    )

    region_type = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    min_lat = models.FloatField(
        null=True,
        blank=True
    )

    max_lat = models.FloatField(
        null=True,
        blank=True
    )

    min_lon = models.FloatField(
        null=True,
        blank=True
    )

    max_lon = models.FloatField(
        null=True,
        blank=True
    )

    elevation_ft = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Habitat(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class WeatherCondition(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Species(models.Model):
    common_name = models.CharField(
        max_length=150,
        unique=True
    )

    scientific_name = models.CharField(
        max_length=150,
        blank=True,
        default=""
    )

    category = models.ForeignKey(
        SpeciesCategory,
        on_delete=models.PROTECT,
        related_name="species"
    )

    is_game_species = models.BooleanField(
        default=False
    )

    conservation_status = models.CharField(
        max_length=100,
        default="Least Concern"
    )

    description = models.TextField(
        blank=True,
        default=""
    )

    def __str__(self):
        return self.common_name


# ============================================================
# MAIN SIGHTING TABLE
# ============================================================

class Sighting(models.Model):

    class SightingType(models.TextChoices):
        ANIMAL = "ANIMAL", "Animal"
        VEGETATION = "VEGETATION", "Vegetation"
        VIEWING = "VIEWING", "Viewing"
        OTHER = "OTHER", "Other"

    class Behavior(models.TextChoices):
        FEEDING = "FEEDING", "Feeding"
        RESTING = "RESTING", "Resting"
        MOVING = "MOVING", "Moving"
        DRINKING = "DRINKING", "Drinking"
        HUNTING = "HUNTING", "Hunting"
        CALLING = "CALLING", "Calling"
        NESTING = "NESTING", "Nesting"
        MATING = "MATING", "Rutting/Mating"
        FLEEING = "FLEEING", "Fleeing"
        OTHER = "OTHER", "Other"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sightings"
    )

    sighting_type = models.CharField(
        max_length=20,
        choices=SightingType.choices
    )

    # Jonathan's existing field.
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    # Jonathan's existing field.
    description = models.TextField()

    # Keep these exact names so existing code does not break.
    locationLongitude = models.FloatField()
    locationLatitude = models.FloatField()

    # Actual time the sighting was observed.
    observed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="sightings"
    )

    habitat = models.ForeignKey(
        Habitat,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="sightings"
    )

    weather = models.ForeignKey(
        WeatherCondition,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="sightings"
    )

    temperature_f = models.IntegerField(
        null=True,
        blank=True
    )

    animal_count = models.PositiveIntegerField(
        default=1
    )

    behavior = models.CharField(
        max_length=30,
        choices=Behavior.choices,
        blank=True,
        default=""
    )

    notes = models.TextField(
        blank=True,
        default=""
    )

    is_public = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Sighting {self.pk} - {self.sighting_type}"


# ============================================================
# EXISTING ANIMAL / VEGETATION TABLES
# ============================================================

class Animal_Sighting(models.Model):
    sighting = models.OneToOneField(
        Sighting,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="animal_sighting"
    )

    # Existing fields kept for compatibility.
    common_name = models.CharField(
        max_length=100
    )

    species = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # New normalized relationship.
    species_record = models.ForeignKey(
        Species,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="animal_sightings"
    )

    def __str__(self):
        return self.common_name


class Vegetation_Sighting(models.Model):
    sighting = models.OneToOneField(
        Sighting,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="vegetation_sighting"
    )

    common_name = models.CharField(
        max_length=100
    )

    species = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    def __str__(self):
        return self.common_name


# ============================================================
# EXISTING IMAGE TABLE
# ============================================================

class Sighting_Image(models.Model):
    sighting = models.OneToOneField(
        Sighting,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="legacy_image"
    )

    image_url = models.URLField(
        max_length=500
    )

    def __str__(self):
        return self.image_url


# ============================================================
# MULTIPLE PHOTO SUPPORT
# ============================================================

class SightingPhoto(models.Model):
    sighting = models.ForeignKey(
        Sighting,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    image_url = models.URLField(
        max_length=500
    )

    caption = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Photo {self.pk} for sighting {self.sighting.pk}"


# ============================================================
# VERIFICATION / VOTING
# ============================================================

class Verification(models.Model):

    class Vote(models.IntegerChoices):
        DISPUTE = -1, "Dispute"
        CONFIRM = 1, "Confirm"

    sighting = models.ForeignKey(
        Sighting,
        on_delete=models.CASCADE,
        related_name="verifications"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sighting_verifications"
    )

    vote = models.IntegerField(
        choices=Vote.choices
    )

    voted_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sighting", "user"],
                name="unique_sighting_verification"
            )
        ]

    def __str__(self):
        return f"{self.user.pk}: {self.vote}"


# ============================================================
# COMMENTS
# ============================================================

class Comment(models.Model):
    sighting = models.ForeignKey(
        Sighting,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sighting_comments"
    )

    body = models.TextField(
        max_length=2000
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.body[:50]


# ============================================================
# HUNTING SEASONS
# ============================================================

class HuntingSeason(models.Model):
    species = models.ForeignKey(
        Species,
        on_delete=models.CASCADE,
        related_name="hunting_seasons"
    )

    zone = models.CharField(
        max_length=100
    )

    weapon = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # Stored as MM-DD, for example 10-11.
    open_month_day = models.CharField(
        max_length=5
    )

    close_month_day = models.CharField(
        max_length=5
    )

    notes = models.TextField(
        blank=True,
        default=""
    )

    def __str__(self):
        return f"{self.species.common_name} - {self.zone}"