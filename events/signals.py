from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import EventRegistration


@receiver(post_save, sender=EventRegistration)
def send_event_registration_email(sender, instance, created, **kwargs):
    if created:
        event = instance.event
        user = instance.user
        send_mail(
            subject=f"{event.title} - {event.location}",
            message=f"Hello! {user.username},"
                    f" \n\nYou have successfully registered for the event '"
                    f"{event.title}' on {event.date} at {event.location}.",
            from_email="noreply@eventapp.com",
            recipient_list=[user.email],
            fail_silently=False,
        )
