from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class CallRequest(models.Model):

    # Validate Phone Number
    # Source: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # Fields
    created_at = models.DateTimeField(auto_now_add=True)
    your_name = models.CharField(max_length=150)
    your_phone_number = models.CharField(validators=[phoneRegex], max_length=25, blank=True)  # validators should be a list
    CALL_STATUS = (
        ('r', 'requested'),
        ('c', 'completed'),
        ('f', 'failed'),
    )
    call_status = models.CharField(max_length=1, choices=CALL_STATUS, blank=True, default='r', help_text='Call Status')

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.your_name
