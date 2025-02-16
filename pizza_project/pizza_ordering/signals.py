from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta

from .models import KitchenLate, WeeklyDoughAmount, Comparison, Store

@receiver(post_save, sender=KitchenLate)
def create_or_update_comparison(sender, instance, created, **kwargs):
    store_name = instance.location
    store = Store.objects.get(name=store_name)

    # Assuming instance.date is a string in 'YYYY-MM-DD' format, convert it to date object
    if isinstance(instance.date, str):
        instance_date = datetime.strptime(instance.date, '%Y-%m-%d').date()
    else:
        instance_date = instance.date

    previous_date = instance_date - timedelta(days=1)
    previous_day_name = previous_date.strftime('%A')

    previous_day_dough_amount = WeeklyDoughAmount.objects.filter(
        store=store,
        day=previous_day_name
    ).first()

    if previous_day_dough_amount:
        # Ensure old_balls_total is an integer
        if isinstance(instance.old_balls_total, str):
            old_balls_total = int(instance.old_balls_total)
        else:
            old_balls_total = instance.old_balls_total

        # Ensure dough_amount is an integer
        if isinstance(previous_day_dough_amount.dough_amount, str):
            dough_amount = int(previous_day_dough_amount.dough_amount)
        else:
            dough_amount = previous_day_dough_amount.dough_amount

        comparison_value = dough_amount - old_balls_total

        Comparison.objects.update_or_create(
            store=store,
            date=previous_date,  # Use previous_date here
            defaults={
                'dough_amount': dough_amount,
                'old_balls_total': old_balls_total,
                'comparison_value': comparison_value
            }
        )



from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import (
    CleanlinessOrderKitchen,
    CleanlinessOrderTerminal,
    CleanlinessOrderStorage,
    CleanlinessOrderApartment,
    ReviewChecklistsKitchen,
    ReviewChecklistsTerminal,
    ReviewChecklistsStorage,
    ReviewChecklistsApartment,
    CalendarWeekNotification  # Import the new model
)

# Helper function to send an email
def send_new_week_email():
    subject = "Notification: New Calendar Week Available"
    message = (
        f"Dear Team,\n\n"
        f"We would like to inform you that a new calendar week has started.\n\n"
        f"Please review the tasks for the week and ensure all necessary actions are taken.\n\n"
        f"Best regards,\n"
        f"Forzacheck\n"

    )

    send_mail(
        subject=subject,
        message=message,
        from_email='forzanapoli.de@gmail.com',  # Update with the 'from' email
        recipient_list=['forzanapoli.de@gmail.com'],  # Update with recipient email(s)
        fail_silently=False,
    )

# Signal to handle cleanliness and review checklist entries
@receiver(post_save, sender=CleanlinessOrderKitchen)
@receiver(post_save, sender=CleanlinessOrderTerminal)
@receiver(post_save, sender=CleanlinessOrderStorage)
@receiver(post_save, sender=CleanlinessOrderApartment)
@receiver(post_save, sender=ReviewChecklistsKitchen)
@receiver(post_save, sender=ReviewChecklistsTerminal)
@receiver(post_save, sender=ReviewChecklistsStorage)
@receiver(post_save, sender=ReviewChecklistsApartment)
def cleanliness_order_post_save(sender, instance, created, **kwargs):
    if created:
        # Check if an email for the current calendar week has been sent
        current_week = instance.calendar_week  # Assuming you have this field in all related models
        week_notification, created = CalendarWeekNotification.objects.get_or_create(calendar_week=current_week)

        # If no notification has been sent, send email and mark the notification as sent
        if not week_notification.notification_sent:
            send_new_week_email()
            week_notification.notification_sent = True  # Mark notification as sent
            week_notification.save()

