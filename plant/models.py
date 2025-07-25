from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password=models.CharField(max_length=500)
    user_email=models.CharField(max_length=500, blank=True, null=True)
    user_city=models.CharField(max_length=500)
    user_dp=models.ImageField(upload_to='user_plants/', blank=True, null=True)

    def __str__(self):
        return str(self.user)

class tips(models.Model):
    tip_id=models.CharField(max_length=50)
    tip_name=models.CharField(max_length=100)
    tip_desc=models.CharField(max_length=500)
    tip_img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tip_id
    
class plantinfo(models.Model):
    plant_id=models.CharField(max_length=50,unique=True,primary_key=True)
    plant_name=models.CharField(max_length=50)
    plant_desc=models.TextField(max_length=50000)
    plant_img=models.ImageField(upload_to='plant_images/')

    def __str__(self):
        return self.plant_name

class userplant(models.Model):
    # Dropdown options
    PLANT_TYPES = [
        ('Succulent', 'Succulent'),
        ('Fern', 'Fern'),
        ('Cactus', 'Cactus'),
        ('Herb', 'Herb'),
        ('Other', 'Other'),
    ]

    SUNLIGHT_OPTIONS = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    LOCATION_CHOICES = [
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ]

    STATUS_OPTIONS = [
        ('Healthy', 'Healthy'),
        ('Needs Attention', 'Needs Attention'),
        ('Dying', 'Dying'),
        ('Dead', 'Dead'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Core plant details
    nickname = models.CharField(max_length=100, blank=True)
    plant_type = models.CharField(max_length=50, choices=PLANT_TYPES, blank=True)
    custom_image = models.ImageField(upload_to='user_plants/', blank=True, null=True)

    # Environmental preferences
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, blank=True)
    sunlight_available = models.CharField(max_length=10, choices=SUNLIGHT_OPTIONS, blank=True)
    
    # Care tracking
    planted_date = models.DateField(default=date.today, help_text="The date when the plant was planted")
    last_watered = models.DateField(blank=True, null=True)
    watering_frequency = models.PositiveIntegerField(help_text="How often the plant should be watered, in days (e.g., every 3 days).", blank=True, null=True)

    last_fertilized = models.DateField(blank=True, null=True, help_text="Date when the plant was last given fertilizer.")
    fertilizing_frequency = models.PositiveIntegerField(help_text="How often to fertilize, in days.", blank=True, null=True)

    # Plant growth & health
    is_flowering_and_fruiting= models.BooleanField(default=False, help_text="whether the plant is currently flowering.")

    # Misc
    notes = models.TextField(blank=True, help_text="Any additional notes – observations, reminders, or tips.")
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nickname or self.user.username
    
    def soft_delete(self):
        self.deleted = True
        self.deleted_at = now()
        self.save()

class planthistory(models.Model):
    plant = models.ForeignKey(userplant, on_delete=models.CASCADE, related_name='history')
    date = models.DateField()
    action = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plant.user.username} - {self.plant.nickname} was {self.action} on {self.date.strftime('%b %d, %Y')} at {self.timestamp.strftime('%I:%M %p')}"