from pathlib import Path

from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models.place import Place
from app.db.models.place_image import PlaceImage
from app.db.models.region import Region

IMAGE_DATA = {
    # Andaman and Nicobar Islands
    "baratang-island": [
        {
            "image_url": "/images/places/baratang-island.jpg",
            "alt_text": "Baratang Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "port-blair": [
        {
            "image_url": "/images/places/port-blair.jpg",
            "alt_text": "Port Blair",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "cellular-jail": [
        {
            "image_url": "/images/places/cellular-jail.jpg",
            "alt_text": "Cellular Jail",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "corbyns-cove-beach": [
        {
            "image_url": "/images/places/corbyns-cove-beach.jpg",
            "alt_text": "Corbyns Cove Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ross-island": [
        {
            "image_url": "/images/places/ross-island.webp",
            "alt_text": "Ross Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "north-bay-island": [
        {
            "image_url": "/images/places/north-bay-island.jpg",
            "alt_text": "North Bay Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "havelock-island-swaraj-dweep": [
        {
            "image_url": "/images/places/havelock-island-swaraj-dweep.jpg",
            "alt_text": "Havelock Island Swaraj Dweep",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "radhanagar-beach": [
        {
            "image_url": "/images/places/radhanagar-beach.jpg",
            "alt_text": "Radhanagar Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "elephant-beach": [
        {
            "image_url": "/images/places/elephant-beach.webp",
            "alt_text": "Elephant Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kalapathar-beach": [
        {
            "image_url": "/images/places/kalapathar-beach.jpg",
            "alt_text": "Kalapathar Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "neil-island-shaheed-dweep": [
        {
            "image_url": "/images/places/neil-island-shaheed-dweep.jpg",
            "alt_text": "Neil Island Shaheed Dweep",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "laxmanpur-beach": [
        {
            "image_url": "/images/places/laxmanpur-beach.jpg",
            "alt_text": "Laxmanpur Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chidiya-tapu": [
        {
            "image_url": "/images/places/chidiya-tapu.jpg",
            "alt_text": "Chidiya Tapu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mount-harriet-national-park": [
        {
            "image_url": "/images/places/mount-harriet-national-park.webp",
            "alt_text": "Mount Harriet National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "limestone-caves-baratang": [
        {
            "image_url": "/images/places/limestone-caves-baratang.webp",
            "alt_text": "Limestone Caves Baratang",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mud-volcanoes-baratang": [
        {
            "image_url": "/images/places/mud-volcanoes-baratang.webp",
            "alt_text": "Mud Volcanoes Baratang",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "long-island": [
        {
            "image_url": "/images/places/long-island.webp",
            "alt_text": "Long Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "diglipur": [
        {
            "image_url": "/images/places/diglipur.webp",
            "alt_text": "Diglipur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "saddle-peak-national-park": [
        {
            "image_url": "/images/places/saddle-peak-national-park.jpg",
            "alt_text": "Saddle Peak National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bharatpur-beach": [
        {
            "image_url": "/images/places/bharatpur-beach.jpg",
            "alt_text": "Bharatpur Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Chandigarh
    "rock-garden": [
        {
            "image_url": "/images/places/rock-garden.jpg",
            "alt_text": "Rock Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sukhna-lake": [
        {
            "image_url": "/images/places/sukhna-lake.jpg",
            "alt_text": "Sukhna Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rose-garden": [
        {
            "image_url": "/images/places/rose-garden.jpg",
            "alt_text": "Rose Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "capitol-complex": [
        {
            "image_url": "/images/places/capitol-complex.jpg",
            "alt_text": "Capitol Complex",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "government-museum-and-art-gallery": [
        {
            "image_url": "/images/places/government-museum-and-art-gallery.jpg",
            "alt_text": "Government Museum And Art Gallery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "le-corbusier-centre": [
        {
            "image_url": "/images/places/le-corbusier-centre.jpg",
            "alt_text": "Le Corbusier Centre",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pinjore-gardens": [
        {
            "image_url": "/images/places/pinjore-gardens.jpg",
            "alt_text": "Pinjore Gardens",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sukhna-wildlife-sanctuary": [
        {
            "image_url": "/images/places/sukhna-wildlife-sanctuary.jpg",
            "alt_text": "Sukhna Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "japanese-garden": [
        {
            "image_url": "/images/places/japanese-garden.jpg",
            "alt_text": "Japanese Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "terraced-garden": [
        {
            "image_url": "/images/places/terraced-garden.jpg",
            "alt_text": "Terraced Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "leisure-valley": [
        {
            "image_url": "/images/places/leisure-valley.jpg",
            "alt_text": "Leisure Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "international-dolls-museum": [
        {
            "image_url": "/images/places/international-dolls-museum.jpg",
            "alt_text": "International Dolls Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chhatbir-zoo": [
        {
            "image_url": "/images/places/chhatbir-zoo.jpg",
            "alt_text": "Chhatbir Zoo",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "elante-mall": [
        {
            "image_url": "/images/places/elante-mall.jpg",
            "alt_text": "Elante Mall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "garden-of-fragrance": [
        {
            "image_url": "/images/places/garden-of-fragrance.jpg",
            "alt_text": "Garden-Of Fragrance",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "cactus-garden-panchkula": [
        {
            "image_url": "/images/places/cactus-garden-panchkula.jpg",
            "alt_text": "Cactus Garden Panchkula",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nada-sahib-gurudwara": [
        {
            "image_url": "/images/places/nada-sahib-gurudwara.jpg",
            "alt_text": "Nada Sahib Gurudwara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bougainvillea-garden": [
        {
            "image_url": "/images/places/bougainvillea-garden.jpg",
            "alt_text": "Bougainvillea Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shanti-kunj": [
        {
            "image_url": "/images/places/shanti-kunj.jpg",
            "alt_text": "Shanti Kunj",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "fitness-trails-sukhna-lake": [
        {
            "image_url": "/images/places/fitness-trails-sukhna-lake.jpg",
            "alt_text": "Fitness Trails Sukhna Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Dadra and Nagar Haveli and Daman and Diu
    "daman": [
        {
            "image_url": "/images/places/daman.jpg",
            "alt_text": "Daman",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "diu": [
        {
            "image_url": "/images/places/diu.jpg",
            "alt_text": "Diu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "silvassa": [
        {
            "image_url": "/images/places/silvassa.avif",
            "alt_text": "Silvassa",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "devka-beach": [
        {
            "image_url": "/images/places/devka-beach.jpg",
            "alt_text": "Devka Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jampore-beach": [
        {
            "image_url": "/images/places/jampore-beach.jpg",
            "alt_text": "Jampore Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nagoa-beach": [
        {
            "image_url": "/images/places/nagoa-beach.avif",
            "alt_text": "Nagoa Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ghogla-beach": [
        {
            "image_url": "/images/places/ghogla-beach.jpg",
            "alt_text": "Ghogla Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "diu-fort": [
        {
            "image_url": "/images/places/diu-fort.jpg",
            "alt_text": "Diu Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "st-pauls-church": [
        {
            "image_url": "/images/places/st-pauls-church.jpg",
            "alt_text": "St Pauls Church",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "naida-caves": [
        {
            "image_url": "/images/places/naida-caves.jpg",
            "alt_text": "Naida Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ins-khukri-memorial": [
        {
            "image_url": "/images/places/ins-khukri-memorial.jpg",
            "alt_text": "Ins Khukri Memorial",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "daman-fort": [
        {
            "image_url": "/images/places/daman-fort.jpg",
            "alt_text": "Daman Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "moti-daman-fort": [
        {
            "image_url": "/images/places/moti-daman-fort.jpg",
            "alt_text": "Moti Daman Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "st-jerome-fort": [
        {
            "image_url": "/images/places/st-jerome-fort.jpg",
            "alt_text": "St Jerome Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dominican-monastery": [
        {
            "image_url": "/images/places/dominican-monastery.jpg",
            "alt_text": "Dominican Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gomatimata-beach": [
        {
            "image_url": "/images/places/gomatimata-beach.jpg",
            "alt_text": "Gomatimata Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vanganga-lake-garden": [
        {
            "image_url": "/images/places/vanganga-lake-garden.jpg",
            "alt_text": "Vanganga Lake Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tribal-museum-silvassa": [
        {
            "image_url": "/images/places/tribal-museum-silvassa.jpg",
            "alt_text": "Tribal Museum Silvassa",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hirwa-van-garden": [
        {
            "image_url": "/images/places/hirwa-van-garden.jpg",
            "alt_text": "Hirwa Van Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lion-safari-wildlife-park": [
        {
            "image_url": "/images/places/lion-safari-wildlife-park.jpg",
            "alt_text": "Lion Safari Wildlife Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Delhi
    "india-gate": [
        {
            "image_url": "/images/places/india-gate.jpg",
            "alt_text": "India Gate",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "red-fort": [
        {
            "image_url": "/images/places/red-fort.jpg",
            "alt_text": "Red Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "qutub-minar": [
        {
            "image_url": "/images/places/qutub-minar.jpg",
            "alt_text": "Qutub Minar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "humayuns-tomb": [
        {
            "image_url": "/images/places/humayuns-tomb.webp",
            "alt_text": "Humayuns Tomb",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lotus-temple": [
        {
            "image_url": "/images/places/lotus-temple.jpg",
            "alt_text": "Lotus Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "akshardham-temple": [
        {
            "image_url": "/images/places/akshardham-temple.jpg",
            "alt_text": "Akshardham Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jama-masjid": [
        {
            "image_url": "/images/places/jama-masjid.jpg",
            "alt_text": "Jama Masjid",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gurudwara-bangla-sahib": [
        {
            "image_url": "/images/places/gurudwara-bangla-sahib.jpg",
            "alt_text": "Gurudwara Bangla Sahib",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rashtrapati-bhavan": [
        {
            "image_url": "/images/places/rashtrapati-bhavan.webp",
            "alt_text": "Rashtrapati Bhavan",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "parliament-house": [
        {
            "image_url": "/images/places/parliament-house.webp",
            "alt_text": "Parliament House",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "raj-ghat": [
        {
            "image_url": "/images/places/raj-ghat.jpg",
            "alt_text": "Raj Ghat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "national-museum": [
        {
            "image_url": "/images/places/national-museum.jpg",
            "alt_text": "National Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "national-gallery-of-modern-art": [
        {
            "image_url": "/images/places/national-gallery-of-modern-art.jpg",
            "alt_text": "National Gallery Of Modern Art",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "purana-qila": [
        {
            "image_url": "/images/places/purana-qila.jpg",
            "alt_text": "Purana Qila",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lodhi-garden": [
        {
            "image_url": "/images/places/lodhi-garden.jpg",
            "alt_text": "Lodhi Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jantar-mantar": [
        {
            "image_url": "/images/places/jantar-mantar.jpg",
            "alt_text": "Jantar Mantar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "agrasen-ki-baoli": [
        {
            "image_url": "/images/places/agrasen-ki-baoli.jpg",
            "alt_text": "Agrasen Ki Baoli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dilli-haat": [
        {
            "image_url": "/images/places/dilli-haat.jpg",
            "alt_text": "Dilli Haat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "national-zoological-park": [
        {
            "image_url": "/images/places/national-zoological-park.jpg",
            "alt_text": "National Zoological Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "connaught-place": [
        {
            "image_url": "/images/places/connaught-place.jpg",
            "alt_text": "Connaught Place",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Jammu and Kashmir
    "srinagar": [
        {
            "image_url": "/images/places/srinagar.jpg",
            "alt_text": "Srinagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dal-lake": [
        {
            "image_url": "/images/places/dal-lake.jpg",
            "alt_text": "Dal Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mughal-gardens": [
        {
            "image_url": "/images/places/mughal-gardens.jpg",
            "alt_text": "Mughal Gardens",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nishat-bagh": [
        {
            "image_url": "/images/places/nishat-bagh.jpg",
            "alt_text": "Nishat Bagh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shalimar-bagh": [
        {
            "image_url": "/images/places/shalimar-bagh.jpg",
            "alt_text": "Shalimar Bagh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gulmarg": [
        {
            "image_url": "/images/places/gulmarg.jpg",
            "alt_text": "Gulmarg",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pahalgam": [
        {
            "image_url": "/images/places/pahalgam.jpg",
            "alt_text": "Pahalgam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sonamarg": [
        {
            "image_url": "/images/places/sonamarg.jpg",
            "alt_text": "Sonamarg",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "betaab-valley": [
        {
            "image_url": "/images/places/betaab-valley.jpg",
            "alt_text": "Betaab Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "aru-valley": [
        {
            "image_url": "/images/places/aru-valley.jpg",
            "alt_text": "Aru Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "doodhpathri": [
        {
            "image_url": "/images/places/doodhpathri.jpg",
            "alt_text": "Doodhpathri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "yusmarg": [
        {
            "image_url": "/images/places/yusmarg.jpg",
            "alt_text": "Yusmarg",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vaishno-devi": [
        {
            "image_url": "/images/places/vaishno-devi.jpg",
            "alt_text": "Vaishno Devi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jammu": [
        {
            "image_url": "/images/places/jammu.jpg",
            "alt_text": "Jammu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "patnitop": [
        {
            "image_url": "/images/places/patnitop.jpg",
            "alt_text": "Patnitop",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sanasar": [
        {
            "image_url": "/images/places/sanasar.jpg",
            "alt_text": "Sanasar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "aharbal-waterfall": [
        {
            "image_url": "/images/places/aharbal-waterfall.jpg",
            "alt_text": "Aharbal Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bangus-valley": [
        {
            "image_url": "/images/places/bangus-valley.png",
            "alt_text": "Bangus Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dachigam-national-park": [
        {
            "image_url": "/images/places/dachigam-national-park.jpg",
            "alt_text": "Dachigam National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "wular-lake": [
        {
            "image_url": "/images/places/wular-lake.jpg",
            "alt_text": "Wular Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Ladakh
    "leh": [
        {
            "image_url": "/images/places/leh.webp",
            "alt_text": "Leh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pangong-lake": [
        {
            "image_url": "/images/places/pangong-lake.avif",
            "alt_text": "Pangong Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nubra-valley": [
        {
            "image_url": "/images/places/nubra-valley.jpg",
            "alt_text": "Nubra Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khardung-la": [
        {
            "image_url": "/images/places/khardung-la.jpg",
            "alt_text": "Khardung La",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shanti-stupa": [
        {
            "image_url": "/images/places/shanti-stupa.jpg",
            "alt_text": "Shanti Stupa",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "leh-palace": [
        {
            "image_url": "/images/places/leh-palace.jpg",
            "alt_text": "Leh Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thiksey-monastery": [
        {
            "image_url": "/images/places/thiksey-monastery.jpg",
            "alt_text": "Thiksey Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hemis-monastery": [
        {
            "image_url": "/images/places/hemis-monastery.jpg",
            "alt_text": "Hemis Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shey-palace": [
        {
            "image_url": "/images/places/shey-palace.jpg",
            "alt_text": "Shey Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "magnetic-hill": [
        {
            "image_url": "/images/places/magnetic-hill.webp",
            "alt_text": "Magnetic Hill",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gurudwara-pathar-sahib": [
        {
            "image_url": "/images/places/gurudwara-pathar-sahib.jpg",
            "alt_text": "Gurudwara Pathar Sahib",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "alchi-monastery": [
        {
            "image_url": "/images/places/alchi-monastery.avif",
            "alt_text": "Alchi Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lamayuru": [
        {
            "image_url": "/images/places/lamayuru.jpg",
            "alt_text": "Lamayuru",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tso-moriri": [
        {
            "image_url": "/images/places/tso-moriri.jpg",
            "alt_text": "Tso Moriri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tso-kar": [
        {
            "image_url": "/images/places/tso-kar.jpg",
            "alt_text": "Tso Kar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "diskit-monastery": [
        {
            "image_url": "/images/places/diskit-monastery.jpg",
            "alt_text": "Diskit Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hunder": [
        {
            "image_url": "/images/places/hunder.jpg",
            "alt_text": "Hunder",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "zanskar-valley": [
        {
            "image_url": "/images/places/zanskar-valley.jpg",
            "alt_text": "Zanskar Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khalsar": [
        {
            "image_url": "/images/places/khalsar.webp",
            "alt_text": "Khalsar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hanle": [
        {
            "image_url": "/images/places/hanle.avif",
            "alt_text": "Hanle",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Lakshadweep
    "kavaratti": [
        {
            "image_url": "/images/places/kavaratti.jpg",
            "alt_text": "Kavaratti",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "agatti-island": [
        {
            "image_url": "/images/places/agatti-island.jpg",
            "alt_text": "Agatti Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bangaram-island": [
        {
            "image_url": "/images/places/bangaram-island.jpg",
            "alt_text": "Bangaram Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kadmat-island": [
        {
            "image_url": "/images/places/kadmat-island.jpg",
            "alt_text": "Kadmat Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kalpeni-island": [
        {
            "image_url": "/images/places/kalpeni-island.jpg",
            "alt_text": "Kalpeni Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "minicoy-island": [
        {
            "image_url": "/images/places/minicoy-island.avif",
            "alt_text": "Minicoy Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bangaram-beach": [
        {
            "image_url": "/images/places/bangaram-beach.jpg",
            "alt_text": "Bangaram Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "agatti-beach": [
        {
            "image_url": "/images/places/agatti-beach.webp",
            "alt_text": "Agatti Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kavaratti-beach": [
        {
            "image_url": "/images/places/kavaratti-beach.jpg",
            "alt_text": "Kavaratti Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kadmat-beach": [
        {
            "image_url": "/images/places/kadmat-beach.jpg",
            "alt_text": "Kadmat Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "minicoy-lighthouse": [
        {
            "image_url": "/images/places/minicoy-lighthouse.jpg",
            "alt_text": "Minicoy Lighthouse",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kavaratti-aquarium": [
        {
            "image_url": "/images/places/kavaratti-aquarium.jpg",
            "alt_text": "Kavaratti Aquarium",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "marine-aquarium-kavaratti": [
        {
            "image_url": "/images/places/marine-aquarium-kavaratti.jpg",
            "alt_text": "Marine Aquarium Kavaratti",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kalpeni-lagoon": [
        {
            "image_url": "/images/places/kalpeni-lagoon.jpg",
            "alt_text": "Kalpeni Lagoon",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thinnakara-island": [
        {
            "image_url": "/images/places/thinnakara-island.jpg",
            "alt_text": "Thinnakara Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "parali-island": [
        {
            "image_url": "/images/places/parali-island.jpg",
            "alt_text": "Parali Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "suheli-islands": [
        {
            "image_url": "/images/places/suheli-islands.jpg",
            "alt_text": "Suheli Islands",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bitra-island": [
        {
            "image_url": "/images/places/bitra-island.webp",
            "alt_text": "Bitra Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "andrott-island": [
        {
            "image_url": "/images/places/andrott-island.jpg",
            "alt_text": "Andrott Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "amini-island": [
        {
            "image_url": "/images/places/amini-island.jpg",
            "alt_text": "Amini Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Puducherry
    "puducherry-city": [
        {
            "image_url": "/images/places/puducherry-city.jpg",
            "alt_text": "Puducherry City",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "promenade-beach": [
        {
            "image_url": "/images/places/promenade-beach.jpg",
            "alt_text": "Promenade Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sri-aurobindo-ashram": [
        {
            "image_url": "/images/places/sri-aurobindo-ashram.jpg",
            "alt_text": "Sri Aurobindo Ashram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "auroville": [
        {
            "image_url": "/images/places/auroville.jpg",
            "alt_text": "Auroville",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "matrimandir": [
        {
            "image_url": "/images/places/matrimandir.jpg",
            "alt_text": "Matrimandir",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "paradise-beach": [
        {
            "image_url": "/images/places/paradise-beach.jpg",
            "alt_text": "Paradise Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "serenity-beach": [
        {
            "image_url": "/images/places/serenity-beach.jpg",
            "alt_text": "Serenity Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "auroville-beach": [
        {
            "image_url": "/images/places/auroville-beach.jpg",
            "alt_text": "Auroville Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "basilica-of-the-sacred-heart-of-jesus": [
        {
            "image_url": "/images/places/basilica-of-the-sacred-heart-of-jesus.jpg",
            "alt_text": "Basilica Of The Sacred Heart Of Jesus",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "french-quarter": [
        {
            "image_url": "/images/places/french-quarter.jpg",
            "alt_text": "French Quarter",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "white-town": [
        {
            "image_url": "/images/places/white-town.jpg",
            "alt_text": "White Town",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "arikamedu": [
        {
            "image_url": "/images/places/arikamedu.avif",
            "alt_text": "Arikamedu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pondicherry-museum": [
        {
            "image_url": "/images/places/pondicherry-museum.jpg",
            "alt_text": "Pondicherry Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bharati-park": [
        {
            "image_url": "/images/places/bharati-park.jpg",
            "alt_text": "Bharati Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "botanical-garden": [
        {
            "image_url": "/images/places/botanical-garden.avif",
            "alt_text": "Botanical Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chunnambar-boat-house": [
        {
            "image_url": "/images/places/chunnambar-boat-house.jpg",
            "alt_text": "Chunnambar Boat House",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "manakula-vinayagar-temple": [
        {
            "image_url": "/images/places/manakula-vinayagar-temple.jpg",
            "alt_text": "Manakula Vinayagar Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "immaculate-conception-cathedral": [
        {
            "image_url": "/images/places/immaculate-conception-cathedral.jpg",
            "alt_text": "Immaculate Conception Cathedral",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gingee-fort": [
        {
            "image_url": "/images/places/gingee-fort.avif",
            "alt_text": "Gingee Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ousteri-lake": [
        {
            "image_url": "/images/places/ousteri-lake.jpg",
            "alt_text": "Ousteri Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Maharashtra
    "mumbai": [
        {
            "image_url": "/images/places/mumbai.jpg",
            "alt_text": "Mumbai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gateway-of-india": [
        {
            "image_url": "/images/places/gateway-of-india.jpg",
            "alt_text": "Gateway Of India",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "marine-drive": [
        {
            "image_url": "/images/places/marine-drive.jpg",
            "alt_text": "Marine Drive",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "elephanta-caves": [
        {
            "image_url": "/images/places/elephanta-caves.jpg",
            "alt_text": "Elephanta Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ajanta-caves": [
        {
            "image_url": "/images/places/ajanta-caves.jpg",
            "alt_text": "Ajanta Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ellora-caves": [
        {
            "image_url": "/images/places/ellora-caves.jpg",
            "alt_text": "Ellora Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shirdi": [
        {
            "image_url": "/images/places/shirdi.jpg",
            "alt_text": "Shirdi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nashik": [
        {
            "image_url": "/images/places/nashik.jpg",
            "alt_text": "Nashik",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mahabaleshwar": [
        {
            "image_url": "/images/places/mahabaleshwar.webp",
            "alt_text": "Mahabaleshwar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lonavala": [
        {
            "image_url": "/images/places/lonavala.jpg",
            "alt_text": "Lonavala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khandala": [
        {
            "image_url": "/images/places/khandala.jpg",
            "alt_text": "Khandala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "matheran": [
        {
            "image_url": "/images/places/matheran.jpg",
            "alt_text": "Matheran",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "alibaug": [
        {
            "image_url": "/images/places/alibaug.jpg",
            "alt_text": "Alibaug",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "panchgani": [
        {
            "image_url": "/images/places/panchgani.jpg",
            "alt_text": "Panchgani",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pune": [
        {
            "image_url": "/images/places/pune.jpg",
            "alt_text": "Pune",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "raigad-fort": [
        {
            "image_url": "/images/places/raigad-fort.webp",
            "alt_text": "Raigad Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pratapgad-fort": [
        {
            "image_url": "/images/places/pratapgad-fort.jpg",
            "alt_text": "Pratapgad Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tadoba-andhari-tiger-reserve": [
        {
            "image_url": "/images/places/tadoba-andhari-tiger-reserve.jpg",
            "alt_text": "Tadoba Andhari Tiger Reserve",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chhatrapati-sambhajinagar": [
        {
            "image_url": "/images/places/chhatrapati-sambhajinagar.jpg",
            "alt_text": "Chhatrapati Sambhajinagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lonar-lake": [
        {
            "image_url": "/images/places/lonar-lake.jpg",
            "alt_text": "Lonar Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Andhra Pradesh
    "tirupati": [
        {
            "image_url": "/images/places/tirupati.jpg",
            "alt_text": "Tirupati",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tirumala": [
        {
            "image_url": "/images/places/tirumala.jpg",
            "alt_text": "Tirumala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "visakhapatnam-vizag": [
        {
            "image_url": "/images/places/visakhapatnam-vizag.avif",
            "alt_text": "Visakhapatnam Vizag",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "araku-valley": [
        {
            "image_url": "/images/places/araku-valley.jpg",
            "alt_text": "Araku Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "borra-caves": [
        {
            "image_url": "/images/places/borra-caves.jpg",
            "alt_text": "Borra Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vijayawada": [
        {
            "image_url": "/images/places/vijayawada.jpg",
            "alt_text": "Vijayawada",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "amaravati": [
        {
            "image_url": "/images/places/amaravati.jpg",
            "alt_text": "Amaravati",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "srisailam": [
        {
            "image_url": "/images/places/srisailam.jpg",
            "alt_text": "Srisailam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gandikota": [
        {
            "image_url": "/images/places/gandikota.jpg",
            "alt_text": "Gandikota",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "horsley-hills": [
        {
            "image_url": "/images/places/horsley-hills.jpg",
            "alt_text": "Horsley Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "papikondalu": [
        {
            "image_url": "/images/places/papikondalu.jpg",
            "alt_text": "Papikondalu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rajahmundry": [
        {
            "image_url": "/images/places/rajahmundry.jpg",
            "alt_text": "Rajahmundry",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "konaseema": [
        {
            "image_url": "/images/places/konaseema.jpg",
            "alt_text": "Konaseema",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lepakshi": [
        {
            "image_url": "/images/places/lepakshi.jpg",
            "alt_text": "Lepakshi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "belum-caves": [
        {
            "image_url": "/images/places/belum-caves.jpg",
            "alt_text": "Belum Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kurnool": [
        {
            "image_url": "/images/places/kurnool.jpg",
            "alt_text": "Kurnool",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mangalagiri": [
        {
            "image_url": "/images/places/mangalagiri.jpg",
            "alt_text": "Mangalagiri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "machilipatnam": [
        {
            "image_url": "/images/places/machilipatnam.webp",
            "alt_text": "Machilipatnam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pulicat-lake": [
        {
            "image_url": "/images/places/pulicat-lake.jpg",
            "alt_text": "Pulicat Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sri-kalahasti": [
        {
            "image_url": "/images/places/sri-kalahasti.jpg",
            "alt_text": "Sri Kalahasti",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Arunachal Pradesh
    "tawang": [
        {
            "image_url": "/images/places/tawang.jpg",
            "alt_text": "Tawang",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tawang-monastery": [
        {
            "image_url": "/images/places/tawang-monastery.jpg",
            "alt_text": "Tawang Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bum-la-pass": [
        {
            "image_url": "/images/places/bum-la-pass.jpg",
            "alt_text": "Bum La Pass",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sela-pass": [
        {
            "image_url": "/images/places/sela-pass.jpg",
            "alt_text": "Sela Pass",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ziro-valley": [
        {
            "image_url": "/images/places/ziro-valley.jpg",
            "alt_text": "Ziro Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bomdila": [
        {
            "image_url": "/images/places/bomdila.jpg",
            "alt_text": "Bomdila",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dirang": [
        {
            "image_url": "/images/places/dirang.jpg",
            "alt_text": "Dirang",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhalukpong": [
        {
            "image_url": "/images/places/bhalukpong.jpg",
            "alt_text": "Bhalukpong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "itanagar": [
        {
            "image_url": "/images/places/itanagar.jpg",
            "alt_text": "Itanagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "namdapha-national-park": [
        {
            "image_url": "/images/places/namdapha-national-park.jpg",
            "alt_text": "Namdapha National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mechuka": [
        {
            "image_url": "/images/places/mechuka.jpg",
            "alt_text": "Mechuka",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pasighat": [
        {
            "image_url": "/images/places/pasighat.jpg",
            "alt_text": "Pasighat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "roing": [
        {
            "image_url": "/images/places/roing.jpg",
            "alt_text": "Roing",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "anini": [
        {
            "image_url": "/images/places/anini.jpg",
            "alt_text": "Anini",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "aalo-along": [
        {
            "image_url": "/images/places/aalo-along.jpg",
            "alt_text": "Aalo Along",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "parashuram-kund": [
        {
            "image_url": "/images/places/parashuram-kund.jpg",
            "alt_text": "Parashuram Kund",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "golden-pagoda-namsai": [
        {
            "image_url": "/images/places/golden-pagoda-namsai.webp",
            "alt_text": "Golden Pagoda Namsai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "malinithan": [
        {
            "image_url": "/images/places/malinithan.jpg",
            "alt_text": "Malinithan",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhismaknagar": [
        {
            "image_url": "/images/places/bhismaknagar.jpg",
            "alt_text": "Bhismaknagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sangti-valley": [
        {
            "image_url": "/images/places/sangti-valley.jpg",
            "alt_text": "Sangti Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Assam
    "kaziranga-national-park": [
        {
            "image_url": "/images/places/kaziranga-national-park.jpg",
            "alt_text": "Kaziranga National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "manas-national-park": [
        {
            "image_url": "/images/places/manas-national-park.jpg",
            "alt_text": "Manas National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kamakhya-temple": [
        {
            "image_url": "/images/places/kamakhya-temple.jpg",
            "alt_text": "Kamakhya Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "majuli-island": [
        {
            "image_url": "/images/places/majuli-island.jpg",
            "alt_text": "Majuli Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "guwahati": [
        {
            "image_url": "/images/places/guwahati.jpg",
            "alt_text": "Guwahati",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sivasagar": [
        {
            "image_url": "/images/places/sivasagar.jpg",
            "alt_text": "Sivasagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rang-ghar": [
        {
            "image_url": "/images/places/rang-ghar.jpg",
            "alt_text": "Rang Ghar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "talatal-ghar": [
        {
            "image_url": "/images/places/talatal-ghar.jpg",
            "alt_text": "Talatal Ghar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "umananda-island": [
        {
            "image_url": "/images/places/umananda-island.avif",
            "alt_text": "Umananda Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hajo": [
        {
            "image_url": "/images/places/hajo.jpg",
            "alt_text": "Hajo",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "haflong": [
        {
            "image_url": "/images/places/haflong.jpg",
            "alt_text": "Haflong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tezpur": [
        {
            "image_url": "/images/places/tezpur.jpg",
            "alt_text": "Tezpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pobitora-wildlife-sanctuary": [
        {
            "image_url": "/images/places/pobitora-wildlife-sanctuary.jpg",
            "alt_text": "Pobitora Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dibru-saikhowa-national-park": [
        {
            "image_url": "/images/places/dibru-saikhowa-national-park.jpg",
            "alt_text": "Dibru Saikhowa National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nameri-national-park": [
        {
            "image_url": "/images/places/nameri-national-park.webp",
            "alt_text": "Nameri National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dibrugarh": [
        {
            "image_url": "/images/places/dibrugarh.jpg",
            "alt_text": "Dibrugarh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sualkuchi": [
        {
            "image_url": "/images/places/sualkuchi.jpg",
            "alt_text": "Sualkuchi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "charaideo": [
        {
            "image_url": "/images/places/charaideo.jpg",
            "alt_text": "Charaideo",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jatinga": [
        {
            "image_url": "/images/places/jatinga.webp",
            "alt_text": "Jatinga",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "panimoor-falls": [
        {
            "image_url": "/images/places/panimoor-falls.jpg",
            "alt_text": "Panimoor Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Bihar
    "bodh-gaya": [
        {
            "image_url": "/images/places/bodh-gaya.jpg",
            "alt_text": "Bodh Gaya",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mahabodhi-temple": [
        {
            "image_url": "/images/places/mahabodhi-temple.jpg",
            "alt_text": "Mahabodhi Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nalanda": [
        {
            "image_url": "/images/places/nalanda.jpg",
            "alt_text": "Nalanda",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nalanda-mahavihara": [
        {
            "image_url": "/images/places/nalanda-mahavihara.webp",
            "alt_text": "Nalanda Mahavihara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rajgir": [
        {
            "image_url": "/images/places/rajgir.jpg",
            "alt_text": "Rajgir",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vaishali": [
        {
            "image_url": "/images/places/vaishali.jpg",
            "alt_text": "Vaishali",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "patna": [
        {
            "image_url": "/images/places/patna.jpg",
            "alt_text": "Patna",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "golghar": [
        {
            "image_url": "/images/places/golghar.jpg",
            "alt_text": "Golghar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "patna-sahib-gurudwara": [
        {
            "image_url": "/images/places/patna-sahib-gurudwara.jpg",
            "alt_text": "Patna Sahib Gurudwara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pawapuri": [
        {
            "image_url": "/images/places/pawapuri.jpg",
            "alt_text": "Pawapuri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vishnupad-temple": [
        {
            "image_url": "/images/places/vishnupad-temple.jpg",
            "alt_text": "Vishnupad Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kesariya-stupa": [
        {
            "image_url": "/images/places/kesariya-stupa.jpg",
            "alt_text": "Kesariya Stupa",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "barabar-caves": [
        {
            "image_url": "/images/places/barabar-caves.jpg",
            "alt_text": "Barabar Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "valmiki-national-park": [
        {
            "image_url": "/images/places/valmiki-national-park.jpg",
            "alt_text": "Valmiki National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vikramshila": [
        {
            "image_url": "/images/places/vikramshila.jpg",
            "alt_text": "Vikramshila",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "madhubani": [
        {
            "image_url": "/images/places/madhubani.jpg",
            "alt_text": "Madhubani",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gaya": [
        {
            "image_url": "/images/places/gaya.jpg",
            "alt_text": "Gaya",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sonepur": [
        {
            "image_url": "/images/places/sonepur.jpg",
            "alt_text": "Sonepur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rajendra-smriti-sangrahalaya": [
        {
            "image_url": "/images/places/rajendra-smriti-sangrahalaya.png",
            "alt_text": "Rajendra Smriti Sangrahalaya",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "buddha-smriti-park": [
        {
            "image_url": "/images/places/buddha-smriti-park.jpg",
            "alt_text": "Buddha Smriti Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Chhattisgarh
    "chitrakote-waterfall": [
        {
            "image_url": "/images/places/chitrakote-waterfall.jpg",
            "alt_text": "Chitrakote Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tirathgarh-waterfall": [
        {
            "image_url": "/images/places/tirathgarh-waterfall.jpg",
            "alt_text": "Tirathgarh Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kanger-valley-national-park": [
        {
            "image_url": "/images/places/kanger-valley-national-park.jpg",
            "alt_text": "Kanger Valley National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jagdalpur": [
        {
            "image_url": "/images/places/jagdalpur.jpg",
            "alt_text": "Jagdalpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bastar-palace": [
        {
            "image_url": "/images/places/bastar-palace.jpg",
            "alt_text": "Bastar Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "danteshwari-temple": [
        {
            "image_url": "/images/places/danteshwari-temple.jpg",
            "alt_text": "Danteshwari Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhoramdeo-temple": [
        {
            "image_url": "/images/places/bhoramdeo-temple.jpg",
            "alt_text": "Bhoramdeo Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sirpur": [
        {
            "image_url": "/images/places/sirpur.jpg",
            "alt_text": "Sirpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "barnawapara-wildlife-sanctuary": [
        {
            "image_url": "/images/places/barnawapara-wildlife-sanctuary.jpg",
            "alt_text": "Barnawapara Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "achanakmar-wildlife-sanctuary": [
        {
            "image_url": "/images/places/achanakmar-wildlife-sanctuary.jpg",
            "alt_text": "Achanakmar Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "indravati-national-park": [
        {
            "image_url": "/images/places/indravati-national-park.webp",
            "alt_text": "Indravati National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mainpat": [
        {
            "image_url": "/images/places/mainpat.jpg",
            "alt_text": "Mainpat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "amarkantak": [
        {
            "image_url": "/images/places/amarkantak.jpg",
            "alt_text": "Amarkantak",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rajim": [
        {
            "image_url": "/images/places/rajim.jpg",
            "alt_text": "Rajim",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gangrel-dam": [
        {
            "image_url": "/images/places/gangrel-dam.jpg",
            "alt_text": "Gangrel Dam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tamda-ghumar-waterfall": [
        {
            "image_url": "/images/places/tamda-ghumar-waterfall.jpg",
            "alt_text": "Tamda Ghumar Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mendri-gumar-waterfall": [
        {
            "image_url": "/images/places/mendri-gumar-waterfall.jpg",
            "alt_text": "Mendri Gumar Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kutumsar-cave": [
        {
            "image_url": "/images/places/kutumsar-cave.jpg",
            "alt_text": "Kutumsar Cave",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kailash-cave": [
        {
            "image_url": "/images/places/kailash-cave.jpg",
            "alt_text": "Kailash Cave",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dalpat-sagar": [
        {
            "image_url": "/images/places/dalpat-sagar.jpg",
            "alt_text": "Dalpat Sagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Goa
    "baga-beach": [
        {
            "image_url": "/images/places/baga-beach.jpg",
            "alt_text": "Baga Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "calangute-beach": [
        {
            "image_url": "/images/places/calangute-beach.jpg",
            "alt_text": "Calangute Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "anjuna-beach": [
        {
            "image_url": "/images/places/anjuna-beach.jpg",
            "alt_text": "Anjuna Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vagator-beach": [
        {
            "image_url": "/images/places/vagator-beach.jpg",
            "alt_text": "Vagator Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "palolem-beach": [
        {
            "image_url": "/images/places/palolem-beach.jpg",
            "alt_text": "Palolem Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "colva-beach": [
        {
            "image_url": "/images/places/colva-beach.jpg",
            "alt_text": "Colva Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "candolim-beach": [
        {
            "image_url": "/images/places/candolim-beach.jpg",
            "alt_text": "Candolim Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "basilica-of-bom-jesus": [
        {
            "image_url": "/images/places/basilica-of-bom-jesus.jpg",
            "alt_text": "Basilica Of Bom Jesus",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "se-cathedral": [
        {
            "image_url": "/images/places/se-cathedral.jpg",
            "alt_text": "Se Cathedral",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "fort-aguada": [
        {
            "image_url": "/images/places/fort-aguada.jpg",
            "alt_text": "Fort Aguada",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chapora-fort": [
        {
            "image_url": "/images/places/chapora-fort.webp",
            "alt_text": "Chapora Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dudhsagar-falls": [
        {
            "image_url": "/images/places/dudhsagar-falls.jpg",
            "alt_text": "Dudhsagar Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "panjim-panaji": [
        {
            "image_url": "/images/places/panjim-panaji.webp",
            "alt_text": "Panjim Panaji",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "fontainhas": [
        {
            "image_url": "/images/places/fontainhas.jpg",
            "alt_text": "Fontainhas",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dona-paula": [
        {
            "image_url": "/images/places/dona-paula.jpg",
            "alt_text": "Dona Paula",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "salim-ali-bird-sanctuary": [
        {
            "image_url": "/images/places/salim-ali-bird-sanctuary.jpg",
            "alt_text": "Salim Ali Bird Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "reis-magos-fort": [
        {
            "image_url": "/images/places/reis-magos-fort.jpg",
            "alt_text": "Reis Magos Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "miramar-beach": [
        {
            "image_url": "/images/places/miramar-beach.jpg",
            "alt_text": "Miramar Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "grand-island": [
        {
            "image_url": "/images/places/grand-island.jpg",
            "alt_text": "Grand Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shri-mangueshi-temple": [
        {
            "image_url": "/images/places/shri-mangueshi-temple.jpg",
            "alt_text": "Shri Mangueshi Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Gujarat
    "statue-of-unity": [
        {
            "image_url": "/images/places/statue-of-unity.jpg",
            "alt_text": "Statue Of Unity",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ahmedabad": [
        {
            "image_url": "/images/places/ahmedabad.jpg",
            "alt_text": "Ahmedabad",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rann-of-kutch": [
        {
            "image_url": "/images/places/rann-of-kutch.jpg",
            "alt_text": "Rann Of Kutch",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "white-rann": [
        {
            "image_url": "/images/places/white-rann.webp",
            "alt_text": "White Rann",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gir-national-park": [
        {
            "image_url": "/images/places/gir-national-park.jpg",
            "alt_text": "Gir National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "somnath-temple": [
        {
            "image_url": "/images/places/somnath-temple.jpg",
            "alt_text": "Somnath Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dwarkadhish-temple": [
        {
            "image_url": "/images/places/dwarkadhish-temple.jpg",
            "alt_text": "Dwarkadhish Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dwarka": [
        {
            "image_url": "/images/places/dwarka.jpg",
            "alt_text": "Dwarka",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sabarmati-ashram": [
        {
            "image_url": "/images/places/sabarmati-ashram.jpg",
            "alt_text": "Sabarmati Ashram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "modhera-sun-temple": [
        {
            "image_url": "/images/places/modhera-sun-temple.jpg",
            "alt_text": "Modhera Sun Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rani-ki-vav": [
        {
            "image_url": "/images/places/rani-ki-vav.png",
            "alt_text": "Rani Ki Vav",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "champaner-pavagadh-archaeological-park": [
        {
            "image_url": "/images/places/champaner-pavagadh-archaeological-park.jpg",
            "alt_text": "Champaner Pavagadh Archaeological Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "junagadh": [
        {
            "image_url": "/images/places/junagadh.jpg",
            "alt_text": "Junagadh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "girnar": [
        {
            "image_url": "/images/places/girnar.jpg",
            "alt_text": "Girnar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dholavira": [
        {
            "image_url": "/images/places/dholavira.jpg",
            "alt_text": "Dholavira",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lakhpat": [
        {
            "image_url": "/images/places/lakhpat.jpg",
            "alt_text": "Lakhpat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "saputara": [
        {
            "image_url": "/images/places/saputara.jpg",
            "alt_text": "Saputara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "marine-national-park": [
        {
            "image_url": "/images/places/marine-national-park.jpg",
            "alt_text": "Marine National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "adalaj-stepwell": [
        {
            "image_url": "/images/places/adalaj-stepwell.jpg",
            "alt_text": "Adalaj Stepwell",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "velavadar-blackbuck-national-park": [
        {
            "image_url": "/images/places/velavadar-blackbuck-national-park.jpg",
            "alt_text": "Velavadar Blackbuck National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Haryana
    "gurugram": [
        {
            "image_url": "/images/places/gurugram.jpg",
            "alt_text": "Gurugram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kurukshetra": [
        {
            "image_url": "/images/places/kurukshetra.jpg",
            "alt_text": "Kurukshetra",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "brahma-sarovar": [
        {
            "image_url": "/images/places/brahma-sarovar.jpg",
            "alt_text": "Brahma Sarovar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jyotisar": [
        {
            "image_url": "/images/places/jyotisar.jpg",
            "alt_text": "Jyotisar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sultanpur-national-park": [
        {
            "image_url": "/images/places/sultanpur-national-park.jpg",
            "alt_text": "Sultanpur National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    ("haryana", "pinjore-gardens"): [
        {
            "image_url": "/images/places/pinjore-gardens.jpg",
            "alt_text": "Pinjore Gardens",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "morni-hills": [
        {
            "image_url": "/images/places/morni-hills.webp",
            "alt_text": "Morni Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "surajkund": [
        {
            "image_url": "/images/places/surajkund.jpg",
            "alt_text": "Surajkund",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "faridabad": [
        {
            "image_url": "/images/places/faridabad.webp",
            "alt_text": "Faridabad",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "panipat": [
        {
            "image_url": "/images/places/panipat.jpg",
            "alt_text": "Panipat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "panipat-museum": [
        {
            "image_url": "/images/places/panipat-museum.jpg",
            "alt_text": "Panipat Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sheikh-chillis-tomb": [
        {
            "image_url": "/images/places/sheikh-chillis-tomb.jpg",
            "alt_text": "Sheikh Chillis Tomb",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "raja-nahar-singh-palace": [
        {
            "image_url": "/images/places/raja-nahar-singh-palace.jpg",
            "alt_text": "Raja Nahar Singh Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rewari-heritage-steam-loco-museum": [
        {
            "image_url": "/images/places/rewari-heritage-steam-loco-museum.jpg",
            "alt_text": "Rewari Heritage Steam Loco Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "badkhal-lake": [
        {
            "image_url": "/images/places/badkhal-lake.jpg",
            "alt_text": "Badkhal Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    ("haryana", "nada-sahib-gurudwara"): [
        {
            "image_url": "/images/places/nada-sahib-gurudwara.jpg",
            "alt_text": "Nada Sahib Gurudwara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhindawas-wildlife-sanctuary": [
        {
            "image_url": "/images/places/bhindawas-wildlife-sanctuary.jpg",
            "alt_text": "Bhindawas Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hisar": [
        {
            "image_url": "/images/places/hisar.jpg",
            "alt_text": "Hisar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "agroha-dham": [
        {
            "image_url": "/images/places/agroha-dham.jpg",
            "alt_text": "Agroha Dham",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kabuli-bagh-mosque": [
        {
            "image_url": "/images/places/kabuli-bagh-mosque.jpg",
            "alt_text": "Kabuli Bagh Mosque",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Himachal Pradesh
    "shimla": [
        {
            "image_url": "/images/places/shimla.jpg",
            "alt_text": "Shimla",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "manali": [
        {
            "image_url": "/images/places/manali.jpg",
            "alt_text": "Manali",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dharamshala": [
        {
            "image_url": "/images/places/dharamshala.jpg",
            "alt_text": "Dharamshala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mcleod-ganj": [
        {
            "image_url": "/images/places/mcleod-ganj.jpg",
            "alt_text": "Mcleod Ganj",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dalhousie": [
        {
            "image_url": "/images/places/dalhousie.jpg",
            "alt_text": "Dalhousie",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kullu": [
        {
            "image_url": "/images/places/kullu.jpg",
            "alt_text": "Kullu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kasol": [
        {
            "image_url": "/images/places/kasol.jpg",
            "alt_text": "Kasol",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kinnaur": [
        {
            "image_url": "/images/places/kinnaur.avif",
            "alt_text": "Kinnaur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "spiti-valley": [
        {
            "image_url": "/images/places/spiti-valley.jpg",
            "alt_text": "Spiti Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rohtang-pass": [
        {
            "image_url": "/images/places/rohtang-pass.jpg",
            "alt_text": "Rohtang Pass",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "solang-valley": [
        {
            "image_url": "/images/places/solang-valley.jpg",
            "alt_text": "Solang Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "manikaran": [
        {
            "image_url": "/images/places/manikaran.avif",
            "alt_text": "Manikaran",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khajjiar": [
        {
            "image_url": "/images/places/khajjiar.jpg",
            "alt_text": "Khajjiar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chail": [
        {
            "image_url": "/images/places/chail.avif",
            "alt_text": "Chail",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kufri": [
        {
            "image_url": "/images/places/kufri.jpg",
            "alt_text": "Kufri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kasauli": [
        {
            "image_url": "/images/places/kasauli.webp",
            "alt_text": "Kasauli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tirthan-valley": [
        {
            "image_url": "/images/places/tirthan-valley.webp",
            "alt_text": "Tirthan Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "key-monastery": [
        {
            "image_url": "/images/places/key-monastery.jpg",
            "alt_text": "Key Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chandratal-lake": [
        {
            "image_url": "/images/places/chandratal-lake.jpg",
            "alt_text": "Chandratal Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kalpa": [
        {
            "image_url": "/images/places/kalpa.jpg",
            "alt_text": "Kalpa",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Jharkhand
    "ranchi": [
        {
            "image_url": "/images/places/ranchi.jpg",
            "alt_text": "Ranchi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dassam-falls": [
        {
            "image_url": "/images/places/dassam-falls.jpg",
            "alt_text": "Dassam Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hundru-falls": [
        {
            "image_url": "/images/places/hundru-falls.jpg",
            "alt_text": "Hundru Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jonha-falls": [
        {
            "image_url": "/images/places/jonha-falls.jpg",
            "alt_text": "Jonha Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "netarhat": [
        {
            "image_url": "/images/places/netarhat.jpg",
            "alt_text": "Netarhat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "betla-national-park": [
        {
            "image_url": "/images/places/betla-national-park.jpg",
            "alt_text": "Betla National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "deoghar": [
        {
            "image_url": "/images/places/deoghar.jpg",
            "alt_text": "Deoghar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "baidyanath-dham": [
        {
            "image_url": "/images/places/baidyanath-dham.jpg",
            "alt_text": "Baidyanath Dham",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "parasnath-hills": [
        {
            "image_url": "/images/places/parasnath-hills.jpg",
            "alt_text": "Parasnath Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shikharji": [
        {
            "image_url": "/images/places/shikharji.jpg",
            "alt_text": "Shikharji",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hazaribagh": [
        {
            "image_url": "/images/places/hazaribagh.jpg",
            "alt_text": "Hazaribagh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hazaribagh-national-park": [
        {
            "image_url": "/images/places/hazaribagh-national-park.jpg",
            "alt_text": "Hazaribagh National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "maithon-dam": [
        {
            "image_url": "/images/places/maithon-dam.jpg",
            "alt_text": "Maithon Dam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "patratu-valley": [
        {
            "image_url": "/images/places/patratu-valley.jpg",
            "alt_text": "Patratu Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "patratu-dam": [
        {
            "image_url": "/images/places/patratu-dam.jpg",
            "alt_text": "Patratu Dam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jagannath-temple-ranchi": [
        {
            "image_url": "/images/places/jagannath-temple-ranchi.jpg",
            "alt_text": "Jagannath Temple Ranchi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tagore-hill": [
        {
            "image_url": "/images/places/tagore-hill.jpg",
            "alt_text": "Tagore Hill",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "usri-falls": [
        {
            "image_url": "/images/places/usri-falls.jpg",
            "alt_text": "Usri Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lodh-falls": [
        {
            "image_url": "/images/places/lodh-falls.jpg",
            "alt_text": "Lodh Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "palamau-tiger-reserve": [
        {
            "image_url": "/images/places/palamau-tiger-reserve.jpg",
            "alt_text": "Palamau Tiger Reserve",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Karnataka
    "bengaluru": [
        {
            "image_url": "/images/places/bengaluru.jpg",
            "alt_text": "Bengaluru",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mysuru-palace": [
        {
            "image_url": "/images/places/mysuru-palace.jpg",
            "alt_text": "Mysuru Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hampi": [
        {
            "image_url": "/images/places/hampi.jpg",
            "alt_text": "Hampi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "coorg-kodagu": [
        {
            "image_url": "/images/places/coorg-kodagu.jpg",
            "alt_text": "Coorg Kodagu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gokarna": [
        {
            "image_url": "/images/places/gokarna.jpg",
            "alt_text": "Gokarna",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jog-falls": [
        {
            "image_url": "/images/places/jog-falls.jpg",
            "alt_text": "Jog Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chikmagalur": [
        {
            "image_url": "/images/places/chikmagalur.jpg",
            "alt_text": "Chikmagalur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "badami": [
        {
            "image_url": "/images/places/badami.jpg",
            "alt_text": "Badami",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pattadakal": [
        {
            "image_url": "/images/places/pattadakal.jpg",
            "alt_text": "Pattadakal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "aihole": [
        {
            "image_url": "/images/places/aihole.jpg",
            "alt_text": "Aihole",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "belur": [
        {
            "image_url": "/images/places/belur.jpg",
            "alt_text": "Belur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "halebidu": [
        {
            "image_url": "/images/places/halebidu.webp",
            "alt_text": "Halebidu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bandipur-national-park": [
        {
            "image_url": "/images/places/bandipur-national-park.jpg",
            "alt_text": "Bandipur National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nagarhole-national-park": [
        {
            "image_url": "/images/places/nagarhole-national-park.jpg",
            "alt_text": "Nagarhole National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kabini": [
        {
            "image_url": "/images/places/kabini.jpg",
            "alt_text": "Kabini",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "udupi": [
        {
            "image_url": "/images/places/udupi.jpg",
            "alt_text": "Udupi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "murudeshwar": [
        {
            "image_url": "/images/places/murudeshwar.webp",
            "alt_text": "Murudeshwar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dandeli": [
        {
            "image_url": "/images/places/dandeli.webp",
            "alt_text": "Dandeli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kudremukh": [
        {
            "image_url": "/images/places/kudremukh.avif",
            "alt_text": "Kudremukh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shravanabelagola": [
        {
            "image_url": "/images/places/shravanabelagola.jpg",
            "alt_text": "Shravanabelagola",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Kerala
    "munnar": [
        {
            "image_url": "/images/places/munnar.webp",
            "alt_text": "Munnar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "alleppey-alappuzha": [
        {
            "image_url": "/images/places/alleppey-alappuzha.jpg",
            "alt_text": "Alleppey Alappuzha",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kochi": [
        {
            "image_url": "/images/places/kochi.jpg",
            "alt_text": "Kochi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thekkady": [
        {
            "image_url": "/images/places/thekkady.jpg",
            "alt_text": "Thekkady",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "wayanad": [
        {
            "image_url": "/images/places/wayanad.jpg",
            "alt_text": "Wayanad",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kovalam": [
        {
            "image_url": "/images/places/kovalam.jpg",
            "alt_text": "Kovalam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "varkala": [
        {
            "image_url": "/images/places/varkala.webp",
            "alt_text": "Varkala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kumarakom": [
        {
            "image_url": "/images/places/kumarakom.jpg",
            "alt_text": "Kumarakom",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bekal-fort": [
        {
            "image_url": "/images/places/bekal-fort.jpg",
            "alt_text": "Bekal Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vagamon": [
        {
            "image_url": "/images/places/vagamon.jpg",
            "alt_text": "Vagamon",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "athirappilly-waterfalls": [
        {
            "image_url": "/images/places/athirappilly-waterfalls.jpg",
            "alt_text": "Athirappilly Waterfalls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "periyar-national-park": [
        {
            "image_url": "/images/places/periyar-national-park.jpg",
            "alt_text": "Periyar National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "silent-valley-national-park": [
        {
            "image_url": "/images/places/silent-valley-national-park.jpg",
            "alt_text": "Silent Valley National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sabarimala": [
        {
            "image_url": "/images/places/sabarimala.jpg",
            "alt_text": "Sabarimala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "guruvayur-temple": [
        {
            "image_url": "/images/places/guruvayur-temple.jpg",
            "alt_text": "Guruvayur Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thiruvananthapuram": [
        {
            "image_url": "/images/places/thiruvananthapuram.jpg",
            "alt_text": "Thiruvananthapuram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kannur": [
        {
            "image_url": "/images/places/kannur.jpg",
            "alt_text": "Kannur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kozhikode": [
        {
            "image_url": "/images/places/kozhikode.jpg",
            "alt_text": "Kozhikode",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "marari-beach": [
        {
            "image_url": "/images/places/marari-beach.jpg",
            "alt_text": "Marari Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "munroe-island": [
        {
            "image_url": "/images/places/munroe-island.jpg",
            "alt_text": "Munroe Island",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Madhya Pradesh
    "khajuraho": [
        {
            "image_url": "/images/places/khajuraho.webp",
            "alt_text": "Khajuraho",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ujjain": [
        {
            "image_url": "/images/places/ujjain.jpg",
            "alt_text": "Ujjain",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhopal": [
        {
            "image_url": "/images/places/bhopal.jpg",
            "alt_text": "Bhopal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "indore": [
        {
            "image_url": "/images/places/indore.jpg",
            "alt_text": "Indore",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gwalior": [
        {
            "image_url": "/images/places/gwalior.jpg",
            "alt_text": "Gwalior",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "orchha": [
        {
            "image_url": "/images/places/orchha.jpg",
            "alt_text": "Orchha",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sanchi": [
        {
            "image_url": "/images/places/sanchi.jpg",
            "alt_text": "Sanchi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pachmarhi": [
        {
            "image_url": "/images/places/pachmarhi.jpg",
            "alt_text": "Pachmarhi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kanha-national-park": [
        {
            "image_url": "/images/places/kanha-national-park.jpg",
            "alt_text": "Kanha National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bandhavgarh-national-park": [
        {
            "image_url": "/images/places/bandhavgarh-national-park.jpg",
            "alt_text": "Bandhavgarh National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pench-national-park": [
        {
            "image_url": "/images/places/pench-national-park.jpg",
            "alt_text": "Pench National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "satpura-national-park": [
        {
            "image_url": "/images/places/satpura-national-park.jpg",
            "alt_text": "Satpura National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mandu": [
        {
            "image_url": "/images/places/mandu.jpg",
            "alt_text": "Mandu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhimbetka": [
        {
            "image_url": "/images/places/bhimbetka.jpg",
            "alt_text": "Bhimbetka",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "omkareshwar": [
        {
            "image_url": "/images/places/omkareshwar.jpg",
            "alt_text": "Omkareshwar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "maheshwar": [
        {
            "image_url": "/images/places/maheshwar.jpg",
            "alt_text": "Maheshwar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chitrakoot": [
        {
            "image_url": "/images/places/chitrakoot.webp",
            "alt_text": "Chitrakoot",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jabalpur": [
        {
            "image_url": "/images/places/jabalpur.jpg",
            "alt_text": "Jabalpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "amarkantak": [
        {
            "image_url": "/images/places/amarkantak.jpg",
            "alt_text": "Amarkantak",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shivpuri": [
        {
            "image_url": "/images/places/shivpuri.jpg",
            "alt_text": "Shivpuri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Manipur
    "imphal": [
        {
            "image_url": "/images/places/imphal.jpg",
            "alt_text": "Imphal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "loktak-lake": [
        {
            "image_url": "/images/places/loktak-lake.webp",
            "alt_text": "Loktak Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "keibul-lamjao-national-park": [
        {
            "image_url": "/images/places/keibul-lamjao-national-park.jpg",
            "alt_text": "Keibul Lamjao National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sendra-tourist-hub": [
        {
            "image_url": "/images/places/sendra-tourist-hub.jpg",
            "alt_text": "Sendra Tourist Hub",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kangla-fort": [
        {
            "image_url": "/images/places/kangla-fort.jpg",
            "alt_text": "Kangla Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shri-govindajee-temple": [
        {
            "image_url": "/images/places/shri-govindajee-temple.jpg",
            "alt_text": "Shri Govindajee Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "andro": [
        {
            "image_url": "/images/places/andro.avif",
            "alt_text": "Andro",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khongjom-war-memorial": [
        {
            "image_url": "/images/places/khongjom-war-memorial.jpg",
            "alt_text": "Khongjom War Memorial",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "moreh": [
        {
            "image_url": "/images/places/moreh.webp",
            "alt_text": "Moreh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ukhrul": [
        {
            "image_url": "/images/places/ukhrul.jpg",
            "alt_text": "Ukhrul",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shirui-hills": [
        {
            "image_url": "/images/places/shirui-hills.jpg",
            "alt_text": "Shirui Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dzuko-valley": [
        {
            "image_url": "/images/places/dzuko-valley.jpg",
            "alt_text": "Dzuko Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "singda-dam": [
        {
            "image_url": "/images/places/singda-dam.webp",
            "alt_text": "Singda Dam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "leimakhong": [
        {
            "image_url": "/images/places/leimakhong.jpg",
            "alt_text": "Leimakhong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khonghampat-orchidarium": [
        {
            "image_url": "/images/places/khonghampat-orchidarium.webp",
            "alt_text": "Khonghampat Orchidarium",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ima-keithel": [
        {
            "image_url": "/images/places/ima-keithel.jpg",
            "alt_text": "Ima Keithel",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sekta-archaeological-living-museum": [
        {
            "image_url": "/images/places/sekta-archaeological-living-museum.webp",
            "alt_text": "Sekta Archaeological Living Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tharon-cave": [
        {
            "image_url": "/images/places/tharon-cave.png",
            "alt_text": "Tharon Cave",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kaina-temple": [
        {
            "image_url": "/images/places/kaina-temple.jpg",
            "alt_text": "Kaina Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "waithou-lake": [
        {
            "image_url": "/images/places/waithou-lake.webp",
            "alt_text": "Waithou Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Meghalaya
    "shillong": [
        {
            "image_url": "/images/places/shillong.jpg",
            "alt_text": "Shillong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "cherrapunji-sohra": [
        {
            "image_url": "/images/places/cherrapunji-sohra.jpg",
            "alt_text": "Cherrapunji Sohra",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dawki": [
        {
            "image_url": "/images/places/dawki.jpg",
            "alt_text": "Dawki",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nongriat": [
        {
            "image_url": "/images/places/nongriat.webp",
            "alt_text": "Nongriat",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "double-decker-living-root-bridge": [
        {
            "image_url": "/images/places/double-decker-living-root-bridge.jpg",
            "alt_text": "Double Decker Living Root Bridge",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mawlynnong": [
        {
            "image_url": "/images/places/mawlynnong.jpg",
            "alt_text": "Mawlynnong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "laitlum-grand-canyon": [
        {
            "image_url": "/images/places/laitlum-grand-canyon.jpg",
            "alt_text": "Laitlum Grand Canyon",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nohkalikai-falls": [
        {
            "image_url": "/images/places/nohkalikai-falls.jpg",
            "alt_text": "Nohkalikai Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "seven-sisters-falls": [
        {
            "image_url": "/images/places/seven-sisters-falls.webp",
            "alt_text": "Seven Sisters Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mawsmai-cave": [
        {
            "image_url": "/images/places/mawsmai-cave.jpg",
            "alt_text": "Mawsmai Cave",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "arwah-cave": [
        {
            "image_url": "/images/places/arwah-cave.jpg",
            "alt_text": "Arwah Cave",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "krang-suri-waterfall": [
        {
            "image_url": "/images/places/krang-suri-waterfall.jpg",
            "alt_text": "Krang Suri Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "umiam-lake": [
        {
            "image_url": "/images/places/umiam-lake.jpg",
            "alt_text": "Umiam Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "elephant-falls": [
        {
            "image_url": "/images/places/elephant-falls.jpg",
            "alt_text": "Elephant Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mawphlang-sacred-forest": [
        {
            "image_url": "/images/places/mawphlang-sacred-forest.jpg",
            "alt_text": "Mawphlang Sacred Forest",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nongpoh": [
        {
            "image_url": "/images/places/nongpoh.jpg",
            "alt_text": "Nongpoh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jowai": [
        {
            "image_url": "/images/places/jowai.jpg",
            "alt_text": "Jowai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nartiang-monoliths": [
        {
            "image_url": "/images/places/nartiang-monoliths.jpg",
            "alt_text": "Nartiang Monoliths",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "balpakram-national-park": [
        {
            "image_url": "/images/places/balpakram-national-park.avif",
            "alt_text": "Balpakram National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nokrek-national-park": [
        {
            "image_url": "/images/places/nokrek-national-park.jpg",
            "alt_text": "Nokrek National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Mizoram
    "aizawl": [
        {
            "image_url": "/images/places/aizawl.jpg",
            "alt_text": "Aizawl",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "reiek": [
        {
            "image_url": "/images/places/reiek.jpg",
            "alt_text": "Reiek",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hmuifang": [
        {
            "image_url": "/images/places/hmuifang.jpg",
            "alt_text": "Hmuifang",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "durtlang-hills": [
        {
            "image_url": "/images/places/durtlang-hills.jpg",
            "alt_text": "Durtlang Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vantawng-falls": [
        {
            "image_url": "/images/places/vantawng-falls.jpg",
            "alt_text": "Vantawng Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "phawngpui-blue-mountain-national-park": [
        {
            "image_url": "/images/places/phawngpui-blue-mountain-national-park.jpg",
            "alt_text": "Phawngpui Blue Mountain National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "champhai": [
        {
            "image_url": "/images/places/champhai.jpg",
            "alt_text": "Champhai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tam-dil": [
        {
            "image_url": "/images/places/tam-dil.jpg",
            "alt_text": "Tam Dil",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rih-dil": [
        {
            "image_url": "/images/places/rih-dil.jpg",
            "alt_text": "Rih Dil",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thenzawl": [
        {
            "image_url": "/images/places/thenzawl.jpg",
            "alt_text": "Thenzawl",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "serchhip": [
        {
            "image_url": "/images/places/serchhip.jpg",
            "alt_text": "Serchhip",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lunglei": [
        {
            "image_url": "/images/places/lunglei.jpg",
            "alt_text": "Lunglei",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "murlen-national-park": [
        {
            "image_url": "/images/places/murlen-national-park.jpg",
            "alt_text": "Murlen National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "palak-lake": [
        {
            "image_url": "/images/places/palak-lake.jpg",
            "alt_text": "Palak Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "saitual": [
        {
            "image_url": "/images/places/saitual.jpg",
            "alt_text": "Saitual",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "falkawn": [
        {
            "image_url": "/images/places/falkawn.jpg",
            "alt_text": "Falkawn",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "solomons-temple": [
        {
            "image_url": "/images/places/solomons-temple.jpg",
            "alt_text": "Solomons Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khawnglung-wildlife-sanctuary": [
        {
            "image_url": "/images/places/khawnglung-wildlife-sanctuary.jpg",
            "alt_text": "Khawnglung Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tuirihiau-falls": [
        {
            "image_url": "/images/places/tuirihiau-falls.jpg",
            "alt_text": "Tuirihiau Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lalsavunga-park": [
        {
            "image_url": "/images/places/lalsavunga-park.jpg",
            "alt_text": "Lalsavunga Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Nagaland
    "kohima": [
        {
            "image_url": "/images/places/kohima.jpg",
            "alt_text": "Kohima",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kisama-heritage-village": [
        {
            "image_url": "/images/places/kisama-heritage-village.jpg",
            "alt_text": "Kisama Heritage Village",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dzuko-valley": [
        {
            "image_url": "/images/places/dzuko-valley.jpg",
            "alt_text": "Dzuko Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "japfu-peak": [
        {
            "image_url": "/images/places/japfu-peak.jpg",
            "alt_text": "Japfu Peak",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kohima-war-cemetery": [
        {
            "image_url": "/images/places/kohima-war-cemetery.jpg",
            "alt_text": "Kohima War Cemetery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khonoma-village": [
        {
            "image_url": "/images/places/khonoma-village.jpg",
            "alt_text": "Khonoma Village",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hornbill-festival": [
        {
            "image_url": "/images/places/hornbill-festival.webp",
            "alt_text": "Hornbill Festival",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mokokchung": [
        {
            "image_url": "/images/places/mokokchung.jpg",
            "alt_text": "Mokokchung",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "wokha": [
        {
            "image_url": "/images/places/wokha.jpg",
            "alt_text": "Wokha",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mount-pauna": [
        {
            "image_url": "/images/places/mount-pauna.png",
            "alt_text": "Mount Pauna",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "doyang-reservoir": [
        {
            "image_url": "/images/places/doyang-reservoir.jpg",
            "alt_text": "Doyang Reservoir",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mon": [
        {
            "image_url": "/images/places/mon.webp",
            "alt_text": "Mon",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "longwa-village": [
        {
            "image_url": "/images/places/longwa-village.jpg",
            "alt_text": "Longwa Village",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pfutsero": [
        {
            "image_url": "/images/places/pfutsero.jpg",
            "alt_text": "Pfutsero",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tuophema-village": [
        {
            "image_url": "/images/places/tuophema-village.jpg",
            "alt_text": "Tuophema Village",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "intangki-national-park": [
        {
            "image_url": "/images/places/intangki-national-park.webp",
            "alt_text": "Intangki National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "benreu": [
        {
            "image_url": "/images/places/benreu.jpg",
            "alt_text": "Benreu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shilloi-lake": [
        {
            "image_url": "/images/places/shilloi-lake.jpg",
            "alt_text": "Shilloi Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "satoi-range": [
        {
            "image_url": "/images/places/satoi-range.webp",
            "alt_text": "Satoi Range",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kachari-ruins": [
        {
            "image_url": "/images/places/kachari-ruins.jpg",
            "alt_text": "Kachari Ruins",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Odisha
    "puri": [
        {
            "image_url": "/images/places/puri.jpg",
            "alt_text": "Puri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jagannath-temple": [
        {
            "image_url": "/images/places/jagannath-temple.jpg",
            "alt_text": "Jagannath Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "konark-sun-temple": [
        {
            "image_url": "/images/places/konark-sun-temple.jpg",
            "alt_text": "Konark Sun Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhubaneswar": [
        {
            "image_url": "/images/places/bhubaneswar.jpg",
            "alt_text": "Bhubaneswar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chilika-lake": [
        {
            "image_url": "/images/places/chilika-lake.jpg",
            "alt_text": "Chilika Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lingaraj-temple": [
        {
            "image_url": "/images/places/lingaraj-temple.jpg",
            "alt_text": "Lingaraj Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "udayagiri-and-khandagiri-caves": [
        {
            "image_url": "/images/places/udayagiri-and-khandagiri-caves.jpg",
            "alt_text": "Udayagiri And Khandagiri Caves",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dhauli": [
        {
            "image_url": "/images/places/dhauli.jpg",
            "alt_text": "Dhauli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "cuttack": [
        {
            "image_url": "/images/places/cuttack.jpg",
            "alt_text": "Cuttack",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "barabati-fort": [
        {
            "image_url": "/images/places/barabati-fort.jpg",
            "alt_text": "Barabati Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "similipal-national-park": [
        {
            "image_url": "/images/places/similipal-national-park.jpg",
            "alt_text": "Similipal National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gopalpur-beach": [
        {
            "image_url": "/images/places/gopalpur-beach.webp",
            "alt_text": "Gopalpur Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chandipur-beach": [
        {
            "image_url": "/images/places/chandipur-beach.jpg",
            "alt_text": "Chandipur Beach",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "daringbadi": [
        {
            "image_url": "/images/places/daringbadi.jpg",
            "alt_text": "Daringbadi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "raghurajpur": [
        {
            "image_url": "/images/places/raghurajpur.jpg",
            "alt_text": "Raghurajpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nandankanan-zoological-park": [
        {
            "image_url": "/images/places/nandankanan-zoological-park.jpg",
            "alt_text": "Nandankanan Zoological Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "satkosia-gorge": [
        {
            "image_url": "/images/places/satkosia-gorge.jpg",
            "alt_text": "Satkosia Gorge",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhitarkanika-national-park": [
        {
            "image_url": "/images/places/bhitarkanika-national-park.jpg",
            "alt_text": "Bhitarkanika National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hirakud-dam": [
        {
            "image_url": "/images/places/hirakud-dam.jpg",
            "alt_text": "Hirakud Dam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sambalpur": [
        {
            "image_url": "/images/places/sambalpur.jpg",
            "alt_text": "Sambalpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Punjab
    "amritsar": [
        {
            "image_url": "/images/places/amritsar.jpg",
            "alt_text": "Amritsar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "golden-temple": [
        {
            "image_url": "/images/places/golden-temple.jpg",
            "alt_text": "Golden Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jallianwala-bagh": [
        {
            "image_url": "/images/places/jallianwala-bagh.jpg",
            "alt_text": "Jallianwala Bagh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "wagah-border": [
        {
            "image_url": "/images/places/wagah-border.jpg",
            "alt_text": "Wagah Border",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "anandpur-sahib": [
        {
            "image_url": "/images/places/anandpur-sahib.jpg",
            "alt_text": "Anandpur Sahib",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "virasat-e-khalsa": [
        {
            "image_url": "/images/places/virasat-e-khalsa.jpg",
            "alt_text": "Virasat E Khalsa",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "patiala": [
        {
            "image_url": "/images/places/patiala.jpg",
            "alt_text": "Patiala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "qila-mubarak": [
        {
            "image_url": "/images/places/qila-mubarak.jpg",
            "alt_text": "Qila Mubarak",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bathinda-fort": [
        {
            "image_url": "/images/places/bathinda-fort.jpg",
            "alt_text": "Bathinda Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ludhiana": [
        {
            "image_url": "/images/places/ludhiana.jpg",
            "alt_text": "Ludhiana",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "harike-wetland": [
        {
            "image_url": "/images/places/harike-wetland.jpg",
            "alt_text": "Harike Wetland",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sultanpur-lodhi": [
        {
            "image_url": "/images/places/sultanpur-lodhi.jpg",
            "alt_text": "Sultanpur Lodhi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "durgiana-temple": [
        {
            "image_url": "/images/places/durgiana-temple.jpg",
            "alt_text": "Durgiana Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gobindgarh-fort": [
        {
            "image_url": "/images/places/gobindgarh-fort.jpg",
            "alt_text": "Gobindgarh Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tarn-taran-sahib": [
        {
            "image_url": "/images/places/tarn-taran-sahib.jpg",
            "alt_text": "Tarn Taran Sahib",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kapurthala": [
        {
            "image_url": "/images/places/kapurthala.jpg",
            "alt_text": "Kapurthala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rangla-punjab-haveli": [
        {
            "image_url": "/images/places/rangla-punjab-haveli.jpg",
            "alt_text": "Rangla Punjab Haveli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ropar-wetland": [
        {
            "image_url": "/images/places/ropar-wetland.jpg",
            "alt_text": "Ropar Wetland",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pushpa-gujral-science-city": [
        {
            "image_url": "/images/places/pushpa-gujral-science-city.jpg",
            "alt_text": "Pushpa Gujral Science City",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "maharaja-ranjit-singh-museum": [
        {
            "image_url": "/images/places/maharaja-ranjit-singh-museum.jpg",
            "alt_text": "Maharaja Ranjit Singh Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Rajasthan
    "jaipur": [
        {
            "image_url": "/images/places/jaipur.jpg",
            "alt_text": "Jaipur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "udaipur": [
        {
            "image_url": "/images/places/udaipur.jpg",
            "alt_text": "Udaipur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jodhpur": [
        {
            "image_url": "/images/places/jodhpur.jpg",
            "alt_text": "Jodhpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jaisalmer": [
        {
            "image_url": "/images/places/jaisalmer.jpg",
            "alt_text": "Jaisalmer",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ajmer": [
        {
            "image_url": "/images/places/ajmer.jpg",
            "alt_text": "Ajmer",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pushkar": [
        {
            "image_url": "/images/places/pushkar.jpg",
            "alt_text": "Pushkar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mount-abu": [
        {
            "image_url": "/images/places/mount-abu.jpg",
            "alt_text": "Mount Abu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ranthambore-national-park": [
        {
            "image_url": "/images/places/ranthambore-national-park.jpg",
            "alt_text": "Ranthambore National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chittorgarh-fort": [
        {
            "image_url": "/images/places/chittorgarh-fort.jpg",
            "alt_text": "Chittorgarh Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mehrangarh-fort": [
        {
            "image_url": "/images/places/mehrangarh-fort.jpg",
            "alt_text": "Mehrangarh Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "amber-fort": [
        {
            "image_url": "/images/places/amber-fort.jpg",
            "alt_text": "Amber Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "city-palace-udaipur": [
        {
            "image_url": "/images/places/city-palace-udaipur.jpg",
            "alt_text": "City Palace Udaipur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hawa-mahal": [
        {
            "image_url": "/images/places/hawa-mahal.jpg",
            "alt_text": "Hawa Mahal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jantar-mantar-jaipur": [
        {
            "image_url": "/images/places/jantar-mantar-jaipur.jpg",
            "alt_text": "Jantar Mantar Jaipur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "junagarh-fort": [
        {
            "image_url": "/images/places/junagarh-fort.jpg",
            "alt_text": "Junagarh Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kumbhalgarh-fort": [
        {
            "image_url": "/images/places/kumbhalgarh-fort.jpg",
            "alt_text": "Kumbhalgarh Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bikaner": [
        {
            "image_url": "/images/places/bikaner.jpg",
            "alt_text": "Bikaner",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bundi": [
        {
            "image_url": "/images/places/bundi.jpg",
            "alt_text": "Bundi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "keoladeo-national-park": [
        {
            "image_url": "/images/places/keoladeo-national-park.avif",
            "alt_text": "Keoladeo National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sam-sand-dunes": [
        {
            "image_url": "/images/places/sam-sand-dunes.jpg",
            "alt_text": "Sam Sand Dunes",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Sikkim
    "gangtok": [
        {
            "image_url": "/images/places/gangtok.jpg",
            "alt_text": "Gangtok",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tsomgo-lake": [
        {
            "image_url": "/images/places/tsomgo-lake.jpg",
            "alt_text": "Tsomgo Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nathula-pass": [
        {
            "image_url": "/images/places/nathula-pass.jpg",
            "alt_text": "Nathula Pass",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pelling": [
        {
            "image_url": "/images/places/pelling.jpg",
            "alt_text": "Pelling",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "yumthang-valley": [
        {
            "image_url": "/images/places/yumthang-valley.webp",
            "alt_text": "Yumthang Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lachung": [
        {
            "image_url": "/images/places/lachung.avif",
            "alt_text": "Lachung",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lachen": [
        {
            "image_url": "/images/places/lachen.avif",
            "alt_text": "Lachen",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gurudongmar-lake": [
        {
            "image_url": "/images/places/gurudongmar-lake.jpg",
            "alt_text": "Gurudongmar Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ravangla": [
        {
            "image_url": "/images/places/ravangla.jpg",
            "alt_text": "Ravangla",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "namchi": [
        {
            "image_url": "/images/places/namchi.jpg",
            "alt_text": "Namchi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "zuluk": [
        {
            "image_url": "/images/places/zuluk.webp",
            "alt_text": "Zuluk",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rumtek-monastery": [
        {
            "image_url": "/images/places/rumtek-monastery.webp",
            "alt_text": "Rumtek Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khecheopalri-lake": [
        {
            "image_url": "/images/places/khecheopalri-lake.jpg",
            "alt_text": "Khecheopalri Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "yuksom": [
        {
            "image_url": "/images/places/yuksom.jpg",
            "alt_text": "Yuksom",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dzongu": [
        {
            "image_url": "/images/places/dzongu.webp",
            "alt_text": "Dzongu",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "temi-tea-garden": [
        {
            "image_url": "/images/places/temi-tea-garden.jpg",
            "alt_text": "Temi Tea Garden",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "buddha-park": [
        {
            "image_url": "/images/places/buddha-park.webp",
            "alt_text": "Buddha Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pemayangtse-monastery": [
        {
            "image_url": "/images/places/pemayangtse-monastery.jpg",
            "alt_text": "Pemayangtse Monastery",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "khangchendzonga-national-park": [
        {
            "image_url": "/images/places/khangchendzonga-national-park.jpg",
            "alt_text": "Khangchendzonga National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nathang-valley": [
        {
            "image_url": "/images/places/nathang-valley.jpg",
            "alt_text": "Nathang Valley",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Tamil Nadu
    "chennai": [
        {
            "image_url": "/images/places/chennai.jpg",
            "alt_text": "Chennai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "madurai": [
        {
            "image_url": "/images/places/madurai.jpg",
            "alt_text": "Madurai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ooty": [
        {
            "image_url": "/images/places/ooty.avif",
            "alt_text": "Ooty",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kodaikanal": [
        {
            "image_url": "/images/places/kodaikanal.avif",
            "alt_text": "Kodaikanal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rameswaram": [
        {
            "image_url": "/images/places/rameswaram.webp",
            "alt_text": "Rameswaram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kanyakumari": [
        {
            "image_url": "/images/places/kanyakumari.jpg",
            "alt_text": "Kanyakumari",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mahabalipuram": [
        {
            "image_url": "/images/places/mahabalipuram.jpg",
            "alt_text": "Mahabalipuram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thanjavur": [
        {
            "image_url": "/images/places/thanjavur.jpg",
            "alt_text": "Thanjavur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kanchipuram": [
        {
            "image_url": "/images/places/kanchipuram.jpg",
            "alt_text": "Kanchipuram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "coimbatore": [
        {
            "image_url": "/images/places/coimbatore.jpg",
            "alt_text": "Coimbatore",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "yercaud": [
        {
            "image_url": "/images/places/yercaud.jpg",
            "alt_text": "Yercaud",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "coonoor": [
        {
            "image_url": "/images/places/coonoor.jpg",
            "alt_text": "Coonoor",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chidambaram": [
        {
            "image_url": "/images/places/chidambaram.jpg",
            "alt_text": "Chidambaram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tiruchirappalli": [
        {
            "image_url": "/images/places/tiruchirappalli.jpg",
            "alt_text": "Tiruchirappalli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dhanushkodi": [
        {
            "image_url": "/images/places/dhanushkodi.jpg",
            "alt_text": "Dhanushkodi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mudumalai-national-park": [
        {
            "image_url": "/images/places/mudumalai-national-park.jpg",
            "alt_text": "Mudumalai National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "meghamalai": [
        {
            "image_url": "/images/places/meghamalai.jpg",
            "alt_text": "Meghamalai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "valparai": [
        {
            "image_url": "/images/places/valparai.jpg",
            "alt_text": "Valparai",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "courtallam": [
        {
            "image_url": "/images/places/courtallam.jpg",
            "alt_text": "Courtallam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hogenakkal-falls": [
        {
            "image_url": "/images/places/hogenakkal-falls.jpg",
            "alt_text": "Hogenakkal Falls",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Telangana
    "hyderabad": [
        {
            "image_url": "/images/places/hyderabad.jpg",
            "alt_text": "Hyderabad",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "charminar": [
        {
            "image_url": "/images/places/charminar.jpg",
            "alt_text": "Charminar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "golconda-fort": [
        {
            "image_url": "/images/places/golconda-fort.jpg",
            "alt_text": "Golconda Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hussain-sagar-lake": [
        {
            "image_url": "/images/places/hussain-sagar-lake.avif",
            "alt_text": "Hussain Sagar Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "salar-jung-museum": [
        {
            "image_url": "/images/places/salar-jung-museum.jpg",
            "alt_text": "Salar Jung Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chowmahalla-palace": [
        {
            "image_url": "/images/places/chowmahalla-palace.jpg",
            "alt_text": "Chowmahalla Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ramoji-film-city": [
        {
            "image_url": "/images/places/ramoji-film-city.webp",
            "alt_text": "Ramoji Film City",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "warangal": [
        {
            "image_url": "/images/places/warangal.jpg",
            "alt_text": "Warangal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "warangal-fort": [
        {
            "image_url": "/images/places/warangal-fort.jpg",
            "alt_text": "Warangal Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "thousand-pillar-temple": [
        {
            "image_url": "/images/places/thousand-pillar-temple.jpg",
            "alt_text": "Thousand Pillar Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ramappa-temple": [
        {
            "image_url": "/images/places/ramappa-temple.webp",
            "alt_text": "Ramappa Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "nagarjuna-sagar": [
        {
            "image_url": "/images/places/nagarjuna-sagar.jpg",
            "alt_text": "Nagarjuna Sagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bhadrachalam": [
        {
            "image_url": "/images/places/bhadrachalam.jpg",
            "alt_text": "Bhadrachalam",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "yadadri": [
        {
            "image_url": "/images/places/yadadri.jpg",
            "alt_text": "Yadadri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "basara": [
        {
            "image_url": "/images/places/basara.jpg",
            "alt_text": "Basara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "medaram": [
        {
            "image_url": "/images/places/medaram.jpg",
            "alt_text": "Medaram",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ananthagiri-hills": [
        {
            "image_url": "/images/places/ananthagiri-hills.webp",
            "alt_text": "Ananthagiri Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kuntala-waterfall": [
        {
            "image_url": "/images/places/kuntala-waterfall.avif",
            "alt_text": "Kuntala Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bogatha-waterfall": [
        {
            "image_url": "/images/places/bogatha-waterfall.png",
            "alt_text": "Bogatha Waterfall",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pakhal-lake": [
        {
            "image_url": "/images/places/pakhal-lake.jpg",
            "alt_text": "Pakhal Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Tripura
    "agartala": [
        {
            "image_url": "/images/places/agartala.jpg",
            "alt_text": "Agartala",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ujjayanta-palace": [
        {
            "image_url": "/images/places/ujjayanta-palace.jpg",
            "alt_text": "Ujjayanta Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "neermahal-palace": [
        {
            "image_url": "/images/places/neermahal-palace.jpg",
            "alt_text": "Neermahal Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "unakoti": [
        {
            "image_url": "/images/places/unakoti.webp",
            "alt_text": "Unakoti",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tripura-sundari-temple": [
        {
            "image_url": "/images/places/tripura-sundari-temple.jpg",
            "alt_text": "Tripura Sundari Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sepahijala-wildlife-sanctuary": [
        {
            "image_url": "/images/places/sepahijala-wildlife-sanctuary.jpg",
            "alt_text": "Sepahijala Wildlife Sanctuary",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jampui-hills": [
        {
            "image_url": "/images/places/jampui-hills.jpg",
            "alt_text": "Jampui Hills",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dumboor-lake": [
        {
            "image_url": "/images/places/dumboor-lake.avif",
            "alt_text": "Dumboor Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pilak": [
        {
            "image_url": "/images/places/pilak.png",
            "alt_text": "Pilak",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "heritage-park": [
        {
            "image_url": "/images/places/heritage-park.jpg",
            "alt_text": "Heritage Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "maharaja-bir-bikram-college-lake": [
        {
            "image_url": "/images/places/maharaja-bir-bikram-college-lake.jpg",
            "alt_text": "Maharaja Bir Bikram College Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "venuban-vihar": [
        {
            "image_url": "/images/places/venuban-vihar.jpg",
            "alt_text": "Venuban Vihar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chittorgarh-tourist-centre": [
        {
            "image_url": "/images/places/chittorgarh-tourist-centre.jpg",
            "alt_text": "Chittorgarh Tourist Centre",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tepania-eco-park": [
        {
            "image_url": "/images/places/tepania-eco-park.jpg",
            "alt_text": "Tepania Eco Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "debtamura": [
        {
            "image_url": "/images/places/debtamura.webp",
            "alt_text": "Debtamura",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "matabari": [
        {
            "image_url": "/images/places/matabari.jpg",
            "alt_text": "Matabari",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "boxanagar": [
        {
            "image_url": "/images/places/boxanagar.jpg",
            "alt_text": "Boxanagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kamalasagar": [
        {
            "image_url": "/images/places/kamalasagar.jpg",
            "alt_text": "Kamalasagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rose-valley-park": [
        {
            "image_url": "/images/places/rose-valley-park.jpg",
            "alt_text": "Rose Valley Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "gedu-mias-mosque": [
        {
            "image_url": "/images/places/gedu-mias-mosque.webp",
            "alt_text": "Gedu Mias Mosque",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Uttar Pradesh
    "agra": [
        {
            "image_url": "/images/places/agra.jpg",
            "alt_text": "Agra",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "taj-mahal": [
        {
            "image_url": "/images/places/taj-mahal.webp",
            "alt_text": "Taj Mahal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "varanasi": [
        {
            "image_url": "/images/places/varanasi.jpg",
            "alt_text": "Varanasi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ayodhya": [
        {
            "image_url": "/images/places/ayodhya.jpg",
            "alt_text": "Ayodhya",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lucknow": [
        {
            "image_url": "/images/places/lucknow.jpg",
            "alt_text": "Lucknow",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mathura": [
        {
            "image_url": "/images/places/mathura.jpg",
            "alt_text": "Mathura",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vrindavan": [
        {
            "image_url": "/images/places/vrindavan.webp",
            "alt_text": "Vrindavan",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "fatehpur-sikri": [
        {
            "image_url": "/images/places/fatehpur-sikri.webp",
            "alt_text": "Fatehpur Sikri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sarnath": [
        {
            "image_url": "/images/places/sarnath.jpg",
            "alt_text": "Sarnath",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "prayagraj": [
        {
            "image_url": "/images/places/prayagraj.jpg",
            "alt_text": "Prayagraj",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jhansi": [
        {
            "image_url": "/images/places/jhansi.jpg",
            "alt_text": "Jhansi",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chitrakoot": [
        {
            "image_url": "/images/places/chitrakoot.webp",
            "alt_text": "Chitrakoot",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kushinagar": [
        {
            "image_url": "/images/places/kushinagar.jpg",
            "alt_text": "Kushinagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dudhwa-national-park": [
        {
            "image_url": "/images/places/dudhwa-national-park.jpg",
            "alt_text": "Dudhwa National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kanpur": [
        {
            "image_url": "/images/places/kanpur.jpg",
            "alt_text": "Kanpur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "meerut": [
        {
            "image_url": "/images/places/meerut.jpg",
            "alt_text": "Meerut",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "vindhyachal": [
        {
            "image_url": "/images/places/vindhyachal.webp",
            "alt_text": "Vindhyachal",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "barsana": [
        {
            "image_url": "/images/places/barsana.jpg",
            "alt_text": "Barsana",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "agra-fort": [
        {
            "image_url": "/images/places/agra-fort.jpg",
            "alt_text": "Agra Fort",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bara-imambara": [
        {
            "image_url": "/images/places/bara-imambara.jpg",
            "alt_text": "Bara Imambara",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # Uttarakhand
    "nainital": [
        {
            "image_url": "/images/places/nainital.jpg",
            "alt_text": "Nainital",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mussoorie": [
        {
            "image_url": "/images/places/mussoorie.webp",
            "alt_text": "Mussoorie",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "rishikesh": [
        {
            "image_url": "/images/places/rishikesh.jpg",
            "alt_text": "Rishikesh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "haridwar": [
        {
            "image_url": "/images/places/haridwar.jpg",
            "alt_text": "Haridwar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kedarnath": [
        {
            "image_url": "/images/places/kedarnath.png",
            "alt_text": "Kedarnath",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "badrinath": [
        {
            "image_url": "/images/places/badrinath.jpg",
            "alt_text": "Badrinath",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "valley-of-flowers": [
        {
            "image_url": "/images/places/valley-of-flowers.jpg",
            "alt_text": "Valley Of Flowers",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "auli": [
        {
            "image_url": "/images/places/auli.webp",
            "alt_text": "Auli",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dehradun": [
        {
            "image_url": "/images/places/dehradun.jpg",
            "alt_text": "Dehradun",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "jim-corbett-national-park": [
        {
            "image_url": "/images/places/jim-corbett-national-park.jpg",
            "alt_text": "Jim Corbett National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ranikhet": [
        {
            "image_url": "/images/places/ranikhet.jpg",
            "alt_text": "Ranikhet",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "almora": [
        {
            "image_url": "/images/places/almora.jpg",
            "alt_text": "Almora",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kausani": [
        {
            "image_url": "/images/places/kausani.jpg",
            "alt_text": "Kausani",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "chopta": [
        {
            "image_url": "/images/places/chopta.jpg",
            "alt_text": "Chopta",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mukteshwar": [
        {
            "image_url": "/images/places/mukteshwar.jpg",
            "alt_text": "Mukteshwar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dhanaulti": [
        {
            "image_url": "/images/places/dhanaulti.jpg",
            "alt_text": "Dhanaulti",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "lansdowne": [
        {
            "image_url": "/images/places/lansdowne.jpg",
            "alt_text": "Lansdowne",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "pithoragarh": [
        {
            "image_url": "/images/places/pithoragarh.jpg",
            "alt_text": "Pithoragarh",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "tehri-lake": [
        {
            "image_url": "/images/places/tehri-lake.jpg",
            "alt_text": "Tehri Lake",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hemkund-sahib": [
        {
            "image_url": "/images/places/hemkund-sahib.webp",
            "alt_text": "Hemkund Sahib",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    # West Bengal
    "kolkata": [
        {
            "image_url": "/images/places/kolkata.jpg",
            "alt_text": "Kolkata",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "darjeeling": [
        {
            "image_url": "/images/places/darjeeling.jpg",
            "alt_text": "Darjeeling",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "siliguri": [
        {
            "image_url": "/images/places/siliguri.jpg",
            "alt_text": "Siliguri",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kalimpong": [
        {
            "image_url": "/images/places/kalimpong.jpg",
            "alt_text": "Kalimpong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "digha": [
        {
            "image_url": "/images/places/digha.jpg",
            "alt_text": "Digha",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "sundarbans-national-park": [
        {
            "image_url": "/images/places/sundarbans-national-park.jpg",
            "alt_text": "Sundarbans National Park",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "howrah-bridge": [
        {
            "image_url": "/images/places/howrah-bridge.jpg",
            "alt_text": "Howrah Bridge",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "victoria-memorial": [
        {
            "image_url": "/images/places/victoria-memorial.jpg",
            "alt_text": "Victoria Memorial",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "indian-museum": [
        {
            "image_url": "/images/places/indian-museum.jpg",
            "alt_text": "Indian Museum",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dakshineswar-kali-temple": [
        {
            "image_url": "/images/places/dakshineswar-kali-temple.webp",
            "alt_text": "Dakshineswar Kali Temple",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "belur-math": [
        {
            "image_url": "/images/places/belur-math.jpg",
            "alt_text": "Belur Math",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "bishnupur": [
        {
            "image_url": "/images/places/bishnupur.webp",
            "alt_text": "Bishnupur",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "shantiniketan": [
        {
            "image_url": "/images/places/shantiniketan.webp",
            "alt_text": "Shantiniketan",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "murshidabad": [
        {
            "image_url": "/images/places/murshidabad.webp",
            "alt_text": "Murshidabad",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "hazarduari-palace": [
        {
            "image_url": "/images/places/hazarduari-palace.webp",
            "alt_text": "Hazarduari Palace",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "dooars": [
        {
            "image_url": "/images/places/dooars.jpg",
            "alt_text": "Dooars",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "buxa-tiger-reserve": [
        {
            "image_url": "/images/places/buxa-tiger-reserve.jpg",
            "alt_text": "Buxa Tiger Reserve",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "mirik": [
        {
            "image_url": "/images/places/mirik.jpg",
            "alt_text": "Mirik",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "kurseong": [
        {
            "image_url": "/images/places/kurseong.jpg",
            "alt_text": "Kurseong",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
    "ganga-sagar": [
        {
            "image_url": "/images/places/ganga-sagar.jpg",
            "alt_text": "Ganga Sagar",
            "is_cover": True,
            "sort_order": 1,
        },
    ],
}

IMAGE_DIR = Path(__file__).resolve().parents[2] / "static" / "images" / "places"

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".avif",
    ".gif",
}


def seed_place_images() -> None:
    db = SessionLocal()

    created = 0
    skipped = 0

    try:
        # Load all places once.
        all_places = (
            db.query(Place, Region.slug.label("region_slug"))
            .join(Region, Place.region_id == Region.id)
            .all()
        )

        # Lookup by (region_slug, place_slug)
        places_by_region_and_slug = {
            (region_slug, place.slug): place.id for place, region_slug in all_places
        }

        # Lookup place slugs that are unique globally.
        places_by_slug = {}

        for place, region_slug in all_places:
            places_by_slug.setdefault(place.slug, []).append(place.id)

        existing_images = {
            (place_id, image_url)
            for place_id, image_url in db.execute(
                select(
                    PlaceImage.place_id,
                    PlaceImage.image_url,
                )
            ).all()
        }

        for place_key, images in IMAGE_DATA.items():

            # Support both:
            # "place-slug"
            # ("region-slug", "place-slug")
            if isinstance(place_key, tuple):
                region_slug, place_slug = place_key

                place_id = places_by_region_and_slug.get((region_slug, place_slug))

                if place_id is None:
                    print(f"Place not found: {place_key}")
                    continue

            else:
                place_slug = place_key
                matching_ids = places_by_slug.get(place_slug, [])

                if not matching_ids:
                    print(
                        f"Place not found: {place_slug}"
                    )
                    continue
                
                for place_id in matching_ids:
                
                    for image_data in images:
                        image_url = image_data["image_url"]
                
                        existing_key = (
                            place_id,
                            image_url,
                        )
                
                        if existing_key in existing_images:
                            skipped += 1
                            continue
                        
                        db.add(
                            PlaceImage(
                                place_id=place_id,
                                image_url=image_url,
                                alt_text=image_data.get("alt_text"),
                                is_cover=image_data.get(
                                    "is_cover",
                                    False,
                                ),
                                sort_order=image_data.get(
                                    "sort_order",
                                    0,
                                ),
                            )
                        )
                
                        existing_images.add(existing_key)
                        created += 1

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

    print()
    print("Place image seed completed.")
    print(f"Images created: {created}")
    print(f"Images skipped: {skipped}")


if __name__ == "__main__":
    seed_place_images()
