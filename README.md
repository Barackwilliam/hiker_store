# 🏔️ HIKER STORE TZ — Setup Guide

## Project Stack
- **Backend**: Django 4.2
- **Database**: Supabase PostgreSQL
- **Image Storage**: Uploadcare (CDN URL approach)
- **Hosting**: cPanel compatible
- **Frontend**: Ultra-advanced custom HTML/CSS/JS (no framework needed)

---

## 📁 Project Structure
```
hiker_store/
├── hiker_store/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                # Main app
│   ├── models.py         # Category, Product, HeroSlide, Inquiry
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/store/
│   │   ├── base.html          # Base template (navbar, footer)
│   │   ├── home.html          # Homepage with hero slider
│   │   ├── category.html      # Category page
│   │   ├── product_detail.html
│   │   ├── products.html      # All products
│   │   ├── search.html
│   │   ├── about.html
│   │   └── contact.html
│   └── management/commands/
│       └── seed_demo.py       # Demo data seeder
├── .env.example
├── requirements.txt
└── manage.py
```

---

## 🚀 Quick Setup

### 1. Clone & Install
```bash
cd hiker_store
pip install -r requirements.txt
```

### 2. Configure .env
```bash
cp .env.example .env
# Edit .env with your Supabase credentials
```

### 3. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User
```bash
python manage.py createsuperuser
```

### 5. Seed Demo Data (optional)
```bash
python manage.py seed_demo
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

---

## 🗄️ Supabase Setup

1. Go to https://supabase.com → Create project
2. Go to **Settings → Database**
3. Copy the connection details to your `.env`:
   - `DB_HOST` = your project's DB host (e.g. `db.xxxxx.supabase.co`)
   - `DB_PASSWORD` = your database password
   - `DB_NAME` = `postgres`
   - `DB_USER` = `postgres`

---

## 🖼️ Uploadcare Setup (Image Storage)

1. Sign up at https://uploadcare.com
2. Go to Dashboard → API Keys
3. Copy **Public Key** and **Secret Key** to `.env`
4. When adding products in admin, paste the Uploadcare CDN URL in the `image_url` field
   - Example: `https://ucarecdn.com/your-uuid/-/preview/800x600/`

---

## ⚙️ Admin Panel Usage

Visit `/admin` to manage:
- **Categories** — Add tent, umbrella, chair, radio etc categories
- **Products** — Add products with Uploadcare image URLs
- **Hero Slides** — Manage homepage hero banner slides
- **Inquiries** — View customer messages from contact form

---

## 📱 WhatsApp Integration

Every product has a direct WhatsApp order button. The number is configured in `.env`:
```
WHATSAPP_NUMBER=255742357287
```

The WhatsApp link format used:
```
https://wa.me/255742357287?text=Hello! I'm interested in PRODUCT NAME (TZS PRICE)
```

---

## 🌐 cPanel Deployment

1. Upload project files to `public_html` or subdirectory
2. Set up Python app in cPanel (Python 3.10+)
3. Set environment variables in cPanel → Python App
4. Run `python manage.py collectstatic`
5. Configure `passenger_wsgi.py` to point to `hiker_store.wsgi`

### passenger_wsgi.py (create in root)
```python
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hiker_store.settings'
from hiker_store.wsgi import application
```

---

## 🎨 Design Features

- Custom animated cursor (lime green dot + ring)
- Full-page hero section with auto-sliding panels
- Animated background terrain SVG
- Floating particles effect
- Scroll-reveal animations on all sections
- Hexagonal icon grid (outdoor-themed shapes)
- Running ticker/marquee
- Product image zoom on hover
- WhatsApp quick-order on every product card
- Sticky filter bar on category/product pages
- Mobile hamburger menu
- Toast notification system
- Responsive at all screen sizes
- Ultra-dark forest green color palette with lime accents

---

## 📞 Contact Info Configured
- Phone 1: 0742357287
- Phone 2: +255 68 964 1419
- Phone 3: 0759 131 659
- Locations: Dar es Salaam & Arusha
