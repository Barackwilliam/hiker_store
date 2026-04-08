from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    ICON_CHOICES = [
        ('tent', '⛺'),
        ('umbrella', '☂️'),
        ('chair', '🪑'),
        ('radio', '📻'),
        ('backpack', '🎒'),
        ('boot', '🥾'),
        ('compass', '🧭'),
        ('flashlight', '🔦'),
        ('knife', '🔪'),
        ('binocular', '🔭'),
        ('map', '🗺️'),
        ('fire', '🔥'),
        ('water', '💧'),
        ('first_aid', '🩺'),
        ('sleeping_bag', '🛌'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=30, choices=ICON_CHOICES, default='backpack')
    image_url = models.CharField(blank=True, help_text="Uploadcare CDN URL")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.products.filter(is_active=True).count()


class Product(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Brand New'),
        ('used', 'Used - Good'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='new')
    image_url = models.CharField(blank=True, help_text="Uploadcare CDN URL - main image")
    image_url_2 = models.CharField(max_length=255, blank=True, null=True)
    image_url_3 = models.CharField(max_length=255, blank=True, null=True)
    image_url_4 = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    stock_qty = models.IntegerField(default=0)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            n = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def discount_percent(self):
        if self.old_price and self.old_price > self.price:
            return int(((self.old_price - self.price) / self.old_price) * 100)
        return None

    @property
    def images(self):
        imgs = []
        for url in [self.image_url, self.image_url_2, self.image_url_3, self.image_url_4]:
            if url:
                imgs.append(url)
        return imgs

    # Open Graph image (Facebook / WhatsApp preview)
    def get_og_image_url(self):
        if self.image_url:
            return f"https://ucarecdn.com/{self.image_url}/-/resize/1200x630/-/format/auto/"
        return ""

    # Optimized image for normal website usage
    def get_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image_url}/-/format/jpg/-/quality/smart/"
        return ""



class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    cta_text = models.CharField(max_length=50, default='Shop Now')
    cta_link = models.CharField(max_length=200, default='/')
    image_url = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

     # Open Graph image (Facebook / WhatsApp preview)
    def get_og_image_url(self):
        if self.image_url:
            return f"https://ucarecdn.com/{self.image_url}/-/resize/1200x630/-/format/auto/"
        return ""

    # Optimized image for normal website usage
    def get_image_url(self):
        if self.image_url:
            return f"https://ucarecdn.com/{self.image_url}/-/format/jpg/-/quality/smart/"
        return ""


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
