from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import EventRegistration

@receiver(post_save, sender=EventRegistration)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Event Registration Confirmation',
            f'You registered for {instance.event.title}',
            'event_management@example.com',
            [instance.user.email],
        )
