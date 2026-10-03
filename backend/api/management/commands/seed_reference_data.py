from django.core.management.base import BaseCommand
from django.db import transaction

from api.models import (
    SpeciesCategory,
    Region,
    Habitat,
    WeatherCondition,
    Species,
    HuntingSeason,
)

from api.reference_data import (
    CATEGORIES,
    REGIONS,
    HABITATS,
    WEATHER,
    SPECIES,
    HUNTING_SEASONS,
)


class Command(BaseCommand):
    help = "Load SightSeeking reference data into the database."

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Loading reference data...")

        for name in CATEGORIES:
            SpeciesCategory.objects.get_or_create(name=name)

        for (
            name,
            region_type,
            min_lat,
            max_lat,
            min_lon,
            max_lon,
            elevation_ft,
        ) in REGIONS:
            Region.objects.update_or_create(
                name=name,
                defaults={
                    "region_type": region_type,
                    "min_lat": min_lat,
                    "max_lat": max_lat,
                    "min_lon": min_lon,
                    "max_lon": max_lon,
                    "elevation_ft": elevation_ft,
                },
            )

        for name in HABITATS:
            Habitat.objects.get_or_create(name=name)

        for name in WEATHER:
            WeatherCondition.objects.get_or_create(name=name)

        for data in SPECIES:
            category = SpeciesCategory.objects.get(name=data["cat"])

            Species.objects.update_or_create(
                common_name=data["common"],
                defaults={
                    "scientific_name": data.get("sci", ""),
                    "category": category,
                    "is_game_species": bool(data.get("game", 0)),
                    "conservation_status": data.get("status", "Least Concern"),
                    "description": data.get("desc", ""),
                },
            )

        for (
            common_name,
            zone,
            weapon,
            open_month_day,
            close_month_day,
            notes,
        ) in HUNTING_SEASONS:
            species = Species.objects.get(common_name=common_name)

            HuntingSeason.objects.update_or_create(
                species=species,
                zone=zone,
                weapon=weapon,
                defaults={
                    "open_month_day": open_month_day,
                    "close_month_day": close_month_day,
                    "notes": notes,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Reference data loaded successfully.")
        )

        self.stdout.write(f"Categories: {SpeciesCategory.objects.count()}")
        self.stdout.write(f"Regions: {Region.objects.count()}")
        self.stdout.write(f"Habitats: {Habitat.objects.count()}")
        self.stdout.write(
            f"Weather conditions: {WeatherCondition.objects.count()}"
        )
        self.stdout.write(f"Species: {Species.objects.count()}")
        self.stdout.write(
            f"Hunting seasons: {HuntingSeason.objects.count()}"
        )