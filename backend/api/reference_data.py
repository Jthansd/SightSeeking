"""Reference (lookup) data for San Diego County.

Bounding boxes are approximate and hand-drawn for this project; they are
good enough to group sightings by area, not survey-grade boundaries.

Each species also carries a *behavior profile* used only by the synthetic
data generator (seed.py) so the generated sightings follow believable
patterns (e.g. mule deer at dawn/dusk in the mountains, gray whales
offshore in winter). Profiles are simplified for demonstration purposes.
"""

CATEGORIES = ["Mammal", "Bird", "Reptile", "Amphibian", "Marine Mammal", "Fish", "Insect"]

# name, type, min_lat, max_lat, min_lon, max_lon, elevation_ft
REGIONS = [
    ("Torrey Pines & La Jolla Coast",      "Coastal",        32.82, 32.95, -117.28, -117.23,  300),
    ("Point Loma & Cabrillo",              "Coastal",        32.66, 32.74, -117.26, -117.22,  250),
    ("San Diego Offshore Waters",          "Ocean",          32.55, 33.10, -117.70, -117.32,    0),
    ("Tijuana River Estuary",              "Lagoon/Estuary", 32.53, 32.58, -117.13, -117.08,   10),
    ("Batiquitos & San Elijo Lagoons",     "Lagoon/Estuary", 33.00, 33.10, -117.30, -117.24,   15),
    ("Mission Bay & San Diego River",      "Lagoon/Estuary", 32.75, 32.80, -117.25, -117.18,   10),
    ("Mission Trails Regional Park",       "Inland Valley",  32.80, 32.86, -117.07, -116.99,  600),
    ("San Pasqual Valley",                 "Inland Valley",  33.06, 33.12, -117.05, -116.92,  400),
    ("Ramona Grasslands",                  "Inland Valley",  33.00, 33.06, -116.95, -116.88, 1400),
    ("Sweetwater & Otay Lakes",            "Inland Valley",  32.60, 32.70, -117.00, -116.88,  500),
    ("Santa Margarita River & Fallbrook",  "Inland Valley",  33.35, 33.45, -117.30, -117.15,  700),
    ("Lake Henshaw & Warner Springs",      "Inland Valley",  33.20, 33.33, -116.80, -116.60, 2900),
    ("Otay Mountain Wilderness",           "Mountain",       32.57, 32.63, -116.90, -116.80, 2500),
    ("Cuyamaca Rancho State Park",         "Mountain",       32.86, 33.02, -116.62, -116.52, 4800),
    ("Laguna Mountains",                   "Mountain",       32.80, 32.92, -116.48, -116.40, 5700),
    ("Palomar Mountain",                   "Mountain",       33.28, 33.38, -116.92, -116.80, 5500),
    ("Anza-Borrego Desert State Park",     "Desert",         32.95, 33.42, -116.45, -116.10,  700),
    ("Balboa Park & Urban Canyons",        "Urban/Suburban", 32.70, 32.80, -117.18, -117.08,  300),
]

HABITATS = [
    "Coastal Sage Scrub", "Chaparral", "Oak Woodland", "Conifer Forest",
    "Grassland/Meadow", "Riparian", "Freshwater Lake/Pond", "Salt Marsh/Estuary",
    "Beach/Dunes", "Rocky Shore/Tidepool", "Open Ocean", "Desert Scrub",
    "Desert Wash/Canyon", "Urban/Suburban", "Agricultural",
]

WEATHER = [
    "Clear/Sunny", "Partly Cloudy", "Overcast", "Marine Layer/Fog", "Light Rain",
    "Heavy Rain", "Windy", "Santa Ana Winds", "Extreme Heat", "Frost/Snow",
]

# Habitats that make sense for each region type (used by the generator and
# by the app to suggest a habitat).
HABITATS_BY_REGION_TYPE = {
    "Coastal":        ["Coastal Sage Scrub", "Beach/Dunes", "Rocky Shore/Tidepool", "Chaparral"],
    "Ocean":          ["Open Ocean"],
    "Lagoon/Estuary": ["Salt Marsh/Estuary", "Riparian", "Beach/Dunes", "Coastal Sage Scrub"],
    "Inland Valley":  ["Grassland/Meadow", "Riparian", "Oak Woodland", "Chaparral",
                       "Freshwater Lake/Pond", "Agricultural", "Coastal Sage Scrub"],
    "Mountain":       ["Conifer Forest", "Oak Woodland", "Chaparral", "Grassland/Meadow", "Riparian"],
    "Desert":         ["Desert Scrub", "Desert Wash/Canyon"],
    "Urban/Suburban": ["Urban/Suburban", "Coastal Sage Scrub", "Riparian"],
}

# ---------------------------------------------------------------------------
# Species. Profile keys (generator only):
#   regions : {region name: weight}
#   hours   : activity pattern name (see HOUR_PATTERNS in seed.py)
#   months  : 12 weights, Jan..Dec
#   weather : {weather name: multiplier} (default 1.0)
#   group   : (min, max) animals per sighting
#   habitats: preferred habitats (optional; used when the region offers them)
# ---------------------------------------------------------------------------
_YEAR = [1] * 12
_WINTER = [5, 5, 4, 2, 0.3, 0.1, 0.1, 0.1, 0.3, 1, 3, 5]
_GRAY_WHALE = [8, 7, 6, 3, 0.5, 0.1, 0.1, 0.1, 0.1, 0.3, 1, 5]
_SUMMER = [0.3, 0.3, 1, 2, 4, 5, 5, 5, 3, 1, 0.5, 0.3]
_SPRING = [0.5, 1, 4, 5, 5, 3, 2, 1, 1, 0.5, 0.5, 0.5]
_DEER = [1, 1, 1, 1.2, 1.2, 1, 1.5, 1.5, 1.5, 2.5, 3, 2]
_HERP = [0.2, 0.4, 1, 3, 5, 5, 4, 4, 3, 2, 0.5, 0.2]
_WET = [3, 4, 3, 1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.3, 1, 2]

_MOUNTAINS = {"Cuyamaca Rancho State Park": 5, "Laguna Mountains": 4, "Palomar Mountain": 4,
              "Lake Henshaw & Warner Springs": 2, "Otay Mountain Wilderness": 1}
_SCRUB = {"Mission Trails Regional Park": 4, "San Pasqual Valley": 3, "Ramona Grasslands": 3,
          "Sweetwater & Otay Lakes": 2, "Otay Mountain Wilderness": 2,
          "Santa Margarita River & Fallbrook": 2, "Torrey Pines & La Jolla Coast": 1}
_WETLANDS = {"Tijuana River Estuary": 4, "Batiquitos & San Elijo Lagoons": 4,
             "Mission Bay & San Diego River": 3, "Sweetwater & Otay Lakes": 2,
             "Lake Henshaw & Warner Springs": 2}
_RAIN_LOVER = {"Light Rain": 4, "Heavy Rain": 3, "Overcast": 1.5, "Clear/Sunny": 0.4, "Extreme Heat": 0.05}
_SUN_LOVER = {"Clear/Sunny": 2, "Extreme Heat": 1.5, "Overcast": 0.5, "Light Rain": 0.1,
              "Heavy Rain": 0.02, "Frost/Snow": 0.01, "Marine Layer/Fog": 0.4}
_FOG_OK = {"Marine Layer/Fog": 1.8, "Overcast": 1.5, "Extreme Heat": 0.3, "Santa Ana Winds": 0.4}

SPECIES = [
    # --- Game mammals -----------------------------------------------------
    dict(common="Mule Deer", sci="Odocoileus hemionus", cat="Mammal", game=1,
         desc="San Diego's only native deer; most active at dawn and dusk, rut peaks in late fall.",
         regions={**_MOUNTAINS, "San Pasqual Valley": 1, "Ramona Grasslands": 1, "Santa Margarita River & Fallbrook": 1},
         hours="crepuscular", months=_DEER, weather=_FOG_OK, group=(1, 6)),
    dict(common="Wild Turkey", habitats=['Oak Woodland', 'Grassland/Meadow', 'Conifer Forest'], sci="Meleagris gallopavo", cat="Bird", game=1,
         desc="Introduced game bird common in oak woodlands around Julian, Palomar and Cuyamaca.",
         regions={"Palomar Mountain": 5, "Cuyamaca Rancho State Park": 4, "Lake Henshaw & Warner Springs": 3,
                  "Laguna Mountains": 1, "Ramona Grasslands": 1},
         hours="morning", months=[1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1.5, 1], weather=_FOG_OK, group=(2, 18)),
    dict(common="California Quail", sci="Callipepla californica", cat="Bird", game=1,
         desc="California's state bird; coveys forage in brushy edges early and late in the day.",
         regions={**_SCRUB, "Anza-Borrego Desert State Park": 1, "Lake Henshaw & Warner Springs": 2},
         hours="crepuscular", months=_YEAR, weather={}, group=(3, 30)),
    dict(common="Mountain Quail", sci="Oreortyx pictus", cat="Bird", game=1,
         desc="Secretive quail of dense chaparral and conifer forest at higher elevations.",
         regions=_MOUNTAINS, hours="morning", months=[0.5, 0.5, 1, 2, 2, 2, 1.5, 1.5, 1, 1, 0.5, 0.5],
         weather={}, group=(2, 12)),
    dict(common="Mourning Dove", sci="Zenaida macroura", cat="Bird", game=1,
         desc="Abundant dove of farmland, grassland and suburbs; huge numbers in early September.",
         regions={"San Pasqual Valley": 4, "Ramona Grasslands": 4, "Lake Henshaw & Warner Springs": 3,
                  "Anza-Borrego Desert State Park": 2, "Balboa Park & Urban Canyons": 2},
         hours="morning", months=[1, 1, 1, 1.5, 2, 2, 2.5, 3, 4, 2, 1, 1], weather=_SUN_LOVER, group=(1, 40)),
    dict(common="Band-tailed Pigeon", habitats=['Oak Woodland', 'Conifer Forest'], sci="Patagioenas fasciata", cat="Bird", game=1,
         desc="Large native pigeon of mountain oak and conifer forests; feeds heavily on acorns.",
         regions={"Palomar Mountain": 5, "Cuyamaca Rancho State Park": 3, "Laguna Mountains": 3},
         hours="morning", months=[2, 2, 1, 1, 1, 1, 1, 1, 1.5, 2, 3, 3], weather={}, group=(2, 25)),
    dict(common="Desert Cottontail", sci="Sylvilagus audubonii", cat="Mammal", game=1,
         desc="Common rabbit of open scrub, grassland and desert edges.",
         regions={**_SCRUB, "Anza-Borrego Desert State Park": 3, "Balboa Park & Urban Canyons": 2},
         hours="crepuscular", months=_YEAR, weather={}, group=(1, 3)),
    dict(common="Black-tailed Jackrabbit", sci="Lepus californicus", cat="Mammal", game=1,
         desc="Large hare of open grassland and desert flats; mostly nocturnal.",
         regions={"Ramona Grasslands": 4, "Anza-Borrego Desert State Park": 4, "Lake Henshaw & Warner Springs": 3,
                  "San Pasqual Valley": 2},
         hours="nocturnal", months=_YEAR, weather={}, group=(1, 3)),
    dict(common="Western Gray Squirrel", habitats=['Oak Woodland', 'Conifer Forest'], sci="Sciurus griseus", cat="Mammal", game=1,
         desc="Native tree squirrel found in mountain oak and pine forests.",
         regions={"Palomar Mountain": 5, "Cuyamaca Rancho State Park": 4, "Laguna Mountains": 4},
         hours="diurnal", months=_YEAR, weather=_SUN_LOVER, group=(1, 3)),
    dict(common="Mallard", habitats=['Freshwater Lake/Pond', 'Salt Marsh/Estuary', 'Riparian'], sci="Anas platyrhynchos", cat="Bird", game=1,
         desc="The most familiar dabbling duck; numbers swell with winter migrants.",
         regions={**_WETLANDS, "Lake Henshaw & Warner Springs": 4, "San Pasqual Valley": 1},
         hours="diurnal", months=[3, 3, 2, 1, 1, 1, 1, 1, 1, 1.5, 2.5, 3], weather={}, group=(2, 60)),
    # --- Non-game mammals -------------------------------------------------
    dict(common="Coyote", sci="Canis latrans", cat="Mammal", game=0,
         desc="Highly adaptable predator found everywhere from deserts to city canyons.",
         regions={**_SCRUB, "Balboa Park & Urban Canyons": 3, "Anza-Borrego Desert State Park": 2,
                  "Cuyamaca Rancho State Park": 1},
         hours="nocturnal", months=_YEAR, weather={}, group=(1, 4)),
    dict(common="Bobcat", sci="Lynx rufus", cat="Mammal", game=0,
         desc="Elusive wild cat of chaparral and riparian edges; often hunts at dawn.",
         regions={**_SCRUB, **_MOUNTAINS}, hours="crepuscular", months=_YEAR, weather=_FOG_OK, group=(1, 2)),
    dict(common="Mountain Lion", sci="Puma concolor", cat="Mammal", game=0, status="Fully Protected",
         desc="Specially protected in California; rarely seen, mostly in the eastern mountains.",
         regions={"Cuyamaca Rancho State Park": 4, "Laguna Mountains": 3, "Palomar Mountain": 3,
                  "Otay Mountain Wilderness": 2, "Anza-Borrego Desert State Park": 1},
         hours="nocturnal", months=_YEAR, weather={}, group=(1, 2), rarity=0.15),
    dict(common="Gray Fox", sci="Urocyon cinereoargenteus", cat="Mammal", game=0,
         desc="Small tree-climbing fox of chaparral and oak woodland.",
         regions={**_SCRUB, **_MOUNTAINS}, hours="nocturnal", months=_YEAR, weather={}, group=(1, 3)),
    dict(common="Raccoon", sci="Procyon lotor", cat="Mammal", game=0,
         desc="Nocturnal omnivore of creeks, lakes and suburban neighborhoods.",
         regions={"Balboa Park & Urban Canyons": 4, "Mission Bay & San Diego River": 3, "San Pasqual Valley": 2,
                  "Sweetwater & Otay Lakes": 2},
         hours="nocturnal", months=_YEAR, weather={}, group=(1, 4)),
    dict(common="Desert Bighorn Sheep", habitats=['Desert Wash/Canyon', 'Desert Scrub'], sci="Ovis canadensis nelsoni", cat="Mammal", game=0, status="Endangered",
         desc="Peninsular bighorn sheep are federally endangered; look for them on rocky desert slopes.",
         regions={"Anza-Borrego Desert State Park": 1}, hours="diurnal",
         months=[1, 1, 1, 1, 1.5, 3, 4, 3, 1.5, 1, 1, 1], weather=_SUN_LOVER, group=(1, 8), rarity=0.3),
    dict(common="California Ground Squirrel", sci="Otospermophilus beecheyi", cat="Mammal", game=0,
         desc="Ubiquitous burrowing squirrel of grasslands, parks and road edges.",
         regions={**_SCRUB, "Balboa Park & Urban Canyons": 3, "Torrey Pines & La Jolla Coast": 2},
         hours="diurnal", months=[0.5, 0.7, 1.2, 1.5, 1.5, 1.5, 1.3, 1.2, 1, 0.8, 0.6, 0.5],
         weather=_SUN_LOVER, group=(1, 8)),
    # --- Birds of prey & others --------------------------------------------
    dict(common="Red-tailed Hawk", sci="Buteo jamaicensis", cat="Bird", game=0,
         desc="The county's most common large hawk, often perched on poles over grassland.",
         regions={**_SCRUB, "Lake Henshaw & Warner Springs": 2}, hours="diurnal", months=_YEAR,
         weather={"Windy": 1.5, **_SUN_LOVER}, group=(1, 2)),
    dict(common="Golden Eagle", sci="Aquila chrysaetos", cat="Bird", game=0, status="Fully Protected",
         desc="Fully protected raptor of open backcountry; Ramona Grasslands is a known haunt.",
         regions={"Ramona Grasslands": 4, "Lake Henshaw & Warner Springs": 3, "Anza-Borrego Desert State Park": 1,
                  "Otay Mountain Wilderness": 1},
         hours="diurnal", months=_YEAR, weather={"Windy": 1.5, "Clear/Sunny": 1.5}, group=(1, 2), rarity=0.3),
    dict(common="Great Horned Owl", sci="Bubo virginianus", cat="Bird", game=0,
         desc="Large owl heard calling at night across almost every habitat.",
         regions={**_SCRUB, **_MOUNTAINS, "Balboa Park & Urban Canyons": 2}, hours="nocturnal",
         months=[2, 2, 1.5, 1, 1, 1, 1, 1, 1, 1.2, 1.5, 2], weather={}, group=(1, 2)),
    dict(common="Osprey", habitats=['Salt Marsh/Estuary', 'Freshwater Lake/Pond', 'Open Ocean', 'Riparian'], sci="Pandion haliaetus", cat="Bird", game=0,
         desc="Fish-eating hawk that nests on light towers around San Diego Bay and Mission Bay.",
         regions={**_WETLANDS, "Point Loma & Cabrillo": 2}, hours="diurnal", months=_YEAR, weather={}, group=(1, 2)),
    dict(common="Great Blue Heron", habitats=['Salt Marsh/Estuary', 'Freshwater Lake/Pond', 'Riparian'], sci="Ardea herodias", cat="Bird", game=0,
         desc="Tall wading bird of lagoons, lakes and the bay shore.",
         regions=_WETLANDS, hours="diurnal", months=_YEAR, weather={}, group=(1, 3)),
    dict(common="Brown Pelican", habitats=['Rocky Shore/Tidepool', 'Beach/Dunes', 'Open Ocean', 'Salt Marsh/Estuary'], sci="Pelecanus occidentalis", cat="Bird", game=0,
         desc="Coastal diving bird; large roosts on the La Jolla cliffs.",
         regions={"Torrey Pines & La Jolla Coast": 5, "Point Loma & Cabrillo": 3, "Mission Bay & San Diego River": 2,
                  "San Diego Offshore Waters": 2},
         hours="diurnal", months=[1, 1, 1, 1, 1, 1.5, 2, 2, 2, 1.5, 1, 1], weather={}, group=(1, 40)),
    dict(common="Western Snowy Plover", habitats=['Beach/Dunes'], sci="Charadrius nivosus nivosus", cat="Bird", game=0, status="Threatened",
         desc="Federally threatened shorebird that nests on open beaches; give nesting areas space.",
         regions={"Tijuana River Estuary": 3, "Batiquitos & San Elijo Lagoons": 3, "Mission Bay & San Diego River": 2},
         hours="diurnal", months=_YEAR, weather={}, group=(1, 12), rarity=0.4),
    dict(common="Coastal California Gnatcatcher", habitats=['Coastal Sage Scrub'], sci="Polioptila californica californica", cat="Bird", game=0,
         status="Threatened",
         desc="Small federally threatened songbird restricted to coastal sage scrub.",
         regions={"Mission Trails Regional Park": 3, "Torrey Pines & La Jolla Coast": 2, "Sweetwater & Otay Lakes": 2,
                  "Point Loma & Cabrillo": 1},
         hours="morning", months=_YEAR, weather={}, group=(1, 3), rarity=0.5),
    dict(common="Acorn Woodpecker", habitats=['Oak Woodland', 'Conifer Forest'], sci="Melanerpes formicivorus", cat="Bird", game=0,
         desc="Noisy, social woodpecker that stores acorns in 'granary' trees.",
         regions={"Palomar Mountain": 4, "Cuyamaca Rancho State Park": 4, "Laguna Mountains": 3,
                  "Lake Henshaw & Warner Springs": 2},
         hours="diurnal", months=_YEAR, weather={}, group=(1, 8)),
    dict(common="Anna's Hummingbird", sci="Calypte anna", cat="Bird", game=0,
         desc="Year-round hummingbird of gardens, parks and scrub; males dive-display in winter.",
         regions={"Balboa Park & Urban Canyons": 5, **_SCRUB}, hours="diurnal", months=_YEAR,
         weather={}, group=(1, 3)),
    # --- Reptiles & amphibians --------------------------------------------
    dict(common="Southern Pacific Rattlesnake", sci="Crotalus oreganus helleri", cat="Reptile", game=0,
         desc="The most frequently encountered rattlesnake in the county; watch your step on warm days.",
         regions={**_SCRUB, **_MOUNTAINS}, hours="diurnal_warm", months=_HERP, weather=_SUN_LOVER, group=(1, 1)),
    dict(common="Red Diamond Rattlesnake", sci="Crotalus ruber", cat="Reptile", game=0,
         status="Species of Special Concern",
         desc="Large, relatively docile rattlesnake of rocky chaparral and desert edges.",
         regions={"Otay Mountain Wilderness": 3, "Anza-Borrego Desert State Park": 3, "Mission Trails Regional Park": 2,
                  "San Pasqual Valley": 2},
         hours="diurnal_warm", months=_HERP, weather=_SUN_LOVER, group=(1, 1)),
    dict(common="Coast Horned Lizard", sci="Phrynosoma blainvillii", cat="Reptile", game=0,
         status="Species of Special Concern",
         desc="Flat, spiny lizard that eats harvester ants in sandy openings.",
         regions={"Ramona Grasslands": 3, "San Pasqual Valley": 2, "Otay Mountain Wilderness": 2,
                  "Cuyamaca Rancho State Park": 1},
         hours="diurnal_warm", months=_HERP, weather=_SUN_LOVER, group=(1, 1), rarity=0.5),
    dict(common="Western Fence Lizard", sci="Sceloporus occidentalis", cat="Reptile", game=0,
         desc="The familiar 'blue-belly' lizard doing push-ups on rocks and fences.",
         regions={**_SCRUB, **_MOUNTAINS, "Balboa Park & Urban Canyons": 2}, hours="diurnal_warm",
         months=_HERP, weather=_SUN_LOVER, group=(1, 3)),
    dict(common="Arroyo Toad", habitats=['Riparian'], sci="Anaxyrus californicus", cat="Amphibian", game=0, status="Endangered",
         desc="Endangered toad of sandy stream terraces; breeds in spring after rains.",
         regions={"Santa Margarita River & Fallbrook": 3, "Lake Henshaw & Warner Springs": 2,
                  "Cuyamaca Rancho State Park": 1},
         hours="nocturnal", months=[0.5, 1, 4, 5, 4, 2, 1, 0.5, 0.2, 0.2, 0.2, 0.3],
         weather=_RAIN_LOVER, group=(1, 10), rarity=0.3),
    dict(common="Baja California Treefrog", habitats=['Riparian', 'Freshwater Lake/Pond', 'Salt Marsh/Estuary'], sci="Pseudacris hypochondriaca", cat="Amphibian", game=0,
         desc="Small treefrog whose chorus fills canyons after winter rains.",
         regions={**_WETLANDS, "Mission Trails Regional Park": 2, "Balboa Park & Urban Canyons": 1},
         hours="nocturnal", months=_WET, weather=_RAIN_LOVER, group=(1, 20)),
    # --- Marine ------------------------------------------------------------
    dict(common="Gray Whale", habitats=['Open Ocean'], sci="Eschrichtius robustus", cat="Marine Mammal", game=0,
         desc="Passes San Diego on its migration to and from Baja lagoons, peaking December-March.",
         regions={"San Diego Offshore Waters": 6, "Point Loma & Cabrillo": 2, "Torrey Pines & La Jolla Coast": 1},
         hours="diurnal", months=_GRAY_WHALE, weather={"Clear/Sunny": 1.5, "Heavy Rain": 0.2, "Windy": 0.5},
         group=(1, 5)),
    dict(common="Common Bottlenose Dolphin", habitats=['Open Ocean', 'Beach/Dunes'], sci="Tursiops truncatus", cat="Marine Mammal", game=0,
         desc="Coastal pods often surf the waves just beyond the break.",
         regions={"San Diego Offshore Waters": 4, "Torrey Pines & La Jolla Coast": 2, "Point Loma & Cabrillo": 1},
         hours="diurnal", months=_YEAR, weather={}, group=(2, 30)),
    dict(common="California Sea Lion", habitats=['Rocky Shore/Tidepool', 'Open Ocean', 'Beach/Dunes'], sci="Zalophus californianus", cat="Marine Mammal", game=0,
         desc="Loud, social pinniped hauled out on the La Jolla cliffs and bay buoys.",
         regions={"Torrey Pines & La Jolla Coast": 5, "Point Loma & Cabrillo": 3, "Mission Bay & San Diego River": 1,
                  "San Diego Offshore Waters": 1},
         hours="diurnal", months=_YEAR, weather={}, group=(1, 50)),
    dict(common="Harbor Seal", habitats=['Rocky Shore/Tidepool', 'Beach/Dunes'], sci="Phoca vitulina", cat="Marine Mammal", game=0,
         desc="Pupping season at the Children's Pool beach runs roughly December to May.",
         regions={"Torrey Pines & La Jolla Coast": 5, "Point Loma & Cabrillo": 1},
         hours="diurnal", months=[3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 2], weather={}, group=(1, 60)),
    dict(common="Garibaldi", habitats=['Rocky Shore/Tidepool', 'Open Ocean'], sci="Hypsypops rubicundus", cat="Fish", game=0,
         desc="California's bright-orange state marine fish; protected from take.",
         regions={"Torrey Pines & La Jolla Coast": 5, "Point Loma & Cabrillo": 2},
         hours="diurnal", months=_SUMMER, weather={"Clear/Sunny": 2}, group=(1, 6)),
    dict(common="Leopard Shark", habitats=['Beach/Dunes', 'Open Ocean'], sci="Triakis semifasciata", cat="Fish", game=0,
         desc="Harmless sharks that gather in the warm shallows off La Jolla Shores in late summer.",
         regions={"Torrey Pines & La Jolla Coast": 6, "Mission Bay & San Diego River": 1},
         hours="midday", months=[0.1, 0.1, 0.2, 0.3, 1, 3, 6, 6, 4, 1, 0.2, 0.1],
         weather={"Clear/Sunny": 2}, group=(1, 40)),
    # --- Insects -----------------------------------------------------------
    dict(common="Monarch Butterfly", sci="Danaus plexippus", cat="Insect", game=0,
         desc="Iconic migratory butterfly; small numbers overwinter along the coast.",
         regions={"Balboa Park & Urban Canyons": 3, "Torrey Pines & La Jolla Coast": 2, "San Pasqual Valley": 2,
                  "Anza-Borrego Desert State Park": 1},
         hours="midday", months=[2, 2, 3, 3, 2, 1, 1, 1, 1.5, 2, 2.5, 2], weather=_SUN_LOVER, group=(1, 20)),
]

# Approximate hunting seasons (month-day ranges). Informational only:
# dates change every year -- always confirm with current CDFW regulations.
# common name, zone, weapon, open MM-DD, close MM-DD, notes
HUNTING_SEASONS = [
    ("Mule Deer", "D16 (San Diego)", "Archery", "09-06", "09-28", "Approximate; check CDFW for exact dates and tags."),
    ("Mule Deer", "D16 (San Diego)", "General", "10-11", "11-09", "Approximate; tag required."),
    ("Wild Turkey", "Statewide (Spring)", "General", "03-28", "05-03", "Bearded turkeys only in spring."),
    ("Wild Turkey", "Statewide (Fall)", "General", "11-08", "12-14", "Approximate."),
    ("California Quail", "Southern Zone", "General", "10-18", "01-25", "Approximate; daily bag limit applies."),
    ("Mountain Quail", "Southern Zone", "General", "10-18", "01-25", "Approximate."),
    ("Mourning Dove", "Statewide (Split 1)", "General", "09-01", "09-15", "Approximate."),
    ("Mourning Dove", "Statewide (Split 2)", "General", "11-08", "12-22", "Approximate."),
    ("Band-tailed Pigeon", "Southern Zone", "General", "12-20", "01-18", "Approximate."),
    ("Desert Cottontail", "Statewide", "General", "07-01", "01-31", "Approximate."),
    ("Black-tailed Jackrabbit", "Statewide", "General", "01-01", "12-31", "No closed season (license required)."),
    ("Western Gray Squirrel", "Southern Zone", "General", "09-13", "01-31", "Approximate."),
    ("Mallard", "Southern California Zone", "General", "10-25", "01-31", "Approximate; federal duck stamp required."),
]
