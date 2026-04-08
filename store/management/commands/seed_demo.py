from django.core.management.base import BaseCommand
from store.models import Category, Product, HeroSlide


class Command(BaseCommand):
    help = 'Seed demo categories and products for Hiker Store TZ'

    def handle(self, *args, **options):
        self.stdout.write('Seeding demo data...')

        # Clear existing
        HeroSlide.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Categories
        categories_data = [
            {'name': 'Tents & Shelters', 'slug': 'tents', 'icon': 'tent', 'order': 1,
             'description': 'Quality camping tents for every adventure — solo, family & expedition.'},
            {'name': 'Camping Umbrellas', 'slug': 'umbrellas', 'icon': 'umbrella', 'order': 2,
             'description': 'Heavy-duty umbrellas for outdoor use, rain protection & shade.'},
            {'name': 'Camping Chairs', 'slug': 'chairs', 'icon': 'chair', 'order': 3,
             'description': 'Portable, durable camping chairs for comfort in the wild.'},
            {'name': 'Radio & Communication', 'slug': 'radio-calls', 'icon': 'radio', 'order': 4,
             'description': 'Two-way radios and communication gear for field use.'},
            {'name': 'Backpacks & Bags', 'slug': 'backpacks', 'icon': 'backpack', 'order': 5,
             'description': 'Hiking backpacks, day packs and travel bags for every journey.'},
            {'name': 'Hiking Boots & Footwear', 'slug': 'boots', 'icon': 'boot', 'order': 6,
             'description': 'Durable trail boots and outdoor footwear for Tanzania\'s terrain.'},
            {'name': 'Lighting & Torches', 'slug': 'lighting', 'icon': 'flashlight', 'order': 7,
             'description': 'Headlamps, torches and lanterns for camping and field use.'},
            {'name': 'Garden & Outdoor Tools', 'slug': 'garden', 'icon': 'map', 'order': 8,
             'description': 'Garden tools, outdoor equipment for home and field.'},
        ]
        cats = {}
        for c in categories_data:
            cat = Category.objects.create(**c)
            cats[c['slug']] = cat
            self.stdout.write(f'  ✅ Category: {cat.name}')

        # Products
        products_data = [
            # Tents
            {'name': '2-Person Dome Tent Waterproof', 'category': cats['tents'],
             'description': 'Lightweight 2-person camping tent with waterproof 3000mm coating. Easy setup, wind-resistant poles, ventilation windows. Perfect for Tanzania highland camping.',
             'price': 85000, 'old_price': 110000, 'is_featured': True, 'in_stock': True, 'stock_qty': 8,
             'tags': 'tent, camping, waterproof, 2 person'},
            {'name': 'Family Tent 4-Person Expedition', 'category': cats['tents'],
             'description': 'Spacious 4-person family camping tent with two rooms, full waterproofing and UV protection. Ideal for safari trips and extended camping.',
             'price': 145000, 'is_featured': True, 'in_stock': True, 'stock_qty': 5,
             'tags': 'tent, family, camping, 4 person, safari'},
            {'name': 'Pop-Up Instant Tent Solo', 'category': cats['tents'],
             'description': 'One-person instant pop-up tent. Sets up in 30 seconds. Lightweight 1.2kg, perfect for solo hikers on Kilimanjaro and Usambara trails.',
             'price': 55000, 'in_stock': True, 'stock_qty': 12,
             'tags': 'tent, solo, popup, hiking, kilimanjaro'},
            # Umbrellas
            {'name': 'Heavy Duty Golf Umbrella 30"', 'category': cats['umbrellas'],
             'description': 'Professional 30-inch golf umbrella with double canopy for wind resistance. Fiberglass frame, auto-open, strong enough for Tanzania\'s rain season.',
             'price': 28000, 'old_price': 35000, 'is_featured': True, 'in_stock': True, 'stock_qty': 20,
             'tags': 'umbrella, rain, golf, outdoor'},
            {'name': 'Beach Umbrella Sun Shade 2m', 'category': cats['umbrellas'],
             'description': '2-meter beach and garden umbrella with UV 50+ protection. Aluminum pole, carry bag included. Perfect for coastal Tanzania use.',
             'price': 42000, 'in_stock': True, 'stock_qty': 15,
             'tags': 'umbrella, beach, sun, garden'},
            # Chairs
            {'name': 'Folding Camping Chair Heavy Duty', 'category': cats['chairs'],
             'description': 'Heavy-duty foldable camping chair with 150kg capacity. Breathable mesh back, cup holder, carry bag. Comfortable for long days at camp.',
             'price': 35000, 'old_price': 42000, 'is_featured': True, 'in_stock': True, 'stock_qty': 18,
             'tags': 'chair, camping, folding, portable'},
            {'name': 'Camping Stool Lightweight', 'category': cats['chairs'],
             'description': 'Ultra-light tripod camping stool, 0.8kg weight. Folds flat. Ideal for hikers who need a quick rest without carrying heavy furniture.',
             'price': 18000, 'in_stock': True, 'stock_qty': 25,
             'tags': 'stool, camping, lightweight, hiking'},
            # Radio
            {'name': 'Walkie Talkie Pair 8km Range', 'category': cats['radio-calls'],
             'description': 'Professional walkie-talkie pair with 8km range, rechargeable batteries, 16 channels, weatherproof design. Ideal for tour guides and field teams.',
             'price': 95000, 'is_featured': True, 'in_stock': True, 'stock_qty': 6,
             'tags': 'radio, walkie talkie, communication, tour, guide'},
            {'name': 'AM/FM Outdoor Radio Solar Powered', 'category': cats['radio-calls'],
             'description': 'Solar + battery AM/FM radio with LED torch. Perfect for remote camps, emergencies and field use across Tanzania.',
             'price': 32000, 'in_stock': True, 'stock_qty': 10,
             'tags': 'radio, solar, outdoor, camping, emergency'},
            # Backpacks
            {'name': 'Trekking Backpack 60L Waterproof', 'category': cats['backpacks'],
             'description': '60-liter trekking backpack with rain cover, multiple compartments, hip belt and padded shoulder straps. Built for multi-day hikes.',
             'price': 78000, 'old_price': 95000, 'is_featured': True, 'in_stock': True, 'stock_qty': 7,
             'tags': 'backpack, trekking, hiking, 60l'},
            {'name': 'Day Hiking Pack 25L', 'category': cats['backpacks'],
             'description': 'Compact 25L hiking day pack with hydration sleeve, ventilated back panel and quick-access pockets. Great for day hikes and safaris.',
             'price': 38000, 'in_stock': True, 'stock_qty': 14,
             'tags': 'backpack, daypack, hiking, 25l'},
            # Boots
            {'name': 'Men\'s Trail Hiking Boots Waterproof', 'category': cats['boots'],
             'description': 'Durable men\'s waterproof hiking boots with non-slip rubber sole, ankle support and breathable lining. Sizes 39-46 available.',
             'price': 62000, 'is_featured': True, 'in_stock': True, 'stock_qty': 20,
             'tags': 'boots, hiking, waterproof, men'},
            # Lighting
            {'name': 'LED Headlamp 300 Lumens USB', 'category': cats['lighting'],
             'description': 'USB rechargeable LED headlamp with 300 lumens, red light mode, adjustable strap and IPX4 splash resistance. Essential camping gear.',
             'price': 22000, 'old_price': 28000, 'in_stock': True, 'stock_qty': 30,
             'tags': 'headlamp, torch, camping, led, rechargeable'},
            # Garden
            {'name': 'Multi-Tool Garden Set 5-Piece', 'category': cats['garden'],
             'description': '5-piece garden and outdoor tool set including trowel, pruner, weeder, transplanter and gloves. Durable stainless steel with ergonomic handles.',
             'price': 48000, 'in_stock': True, 'stock_qty': 8,
             'tags': 'garden, tools, outdoor, set'},
        ]

        for p in products_data:
            product = Product.objects.create(**p)
            self.stdout.write(f'  ✅ Product: {product.name}')

        # Hero Slides
        HeroSlide.objects.create(
            title='GEAR UP FOR YOUR\nNEXT ADVENTURE',
            subtitle='Tanzania\'s premier outdoor store. Camping, hiking & tactical gear for every explorer.',
            cta_text='Shop Now',
            cta_link='/products/',
            order=1, is_active=True
        )
        HeroSlide.objects.create(
            title='TENTS, CHAIRS\n& MORE',
            subtitle='From Kilimanjaro base camps to Serengeti safaris — we have the gear you need.',
            cta_text='See Categories',
            cta_link='/products/',
            order=2, is_active=True
        )

        self.stdout.write(self.style.SUCCESS('\n✅ Demo data seeded successfully!'))
        self.stdout.write('Categories: ' + str(Category.objects.count()))
        self.stdout.write('Products: ' + str(Product.objects.count()))
