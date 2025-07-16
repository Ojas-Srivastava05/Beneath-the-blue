from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Pledge(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    eliminate_plastics = models.BooleanField(default=False)
    sustainable_seafood = models.BooleanField(default=False)
    join_cleanups = models.BooleanField(default=False)
    reduce_footprint = models.BooleanField(default=False)
    support_conservation = models.BooleanField(default=False)
    personal_promise = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pledge by {self.name}"

class Idea(models.Model):
    CATEGORY_CHOICES = [
        ('pollution', 'Pollution Solutions'),
        ('research', 'Marine Research'),
        ('education', 'Ocean Education'),
        ('tech', 'Conservation Tech'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Idea: {self.title} by {self.name}"

class Feedback(models.Model):
    FEEDBACK_TYPE = [
        ('explorer', 'Depth Explorer'),
        ('education', 'Learning Content'),
        ('action', 'Take Action'),
        ('general', 'General Feedback'),
    ]
    
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    feedback_type = models.CharField(max_length=50, choices=FEEDBACK_TYPE)
    message = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback ({self.get_feedback_type_display()}) - Rating: {self.rating}"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email