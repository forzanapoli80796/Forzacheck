# your_app/management/commands/populate_comparison.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from pizza_ordering.models import Store, WeeklyDoughAmount, KitchenLate, Comparison

class Command(BaseCommand):
    help = 'Populate the Comparison table with data'

    def handle(self, *args, **kwargs):
        stores = Store.objects.all()
        for store in stores:
            kitchen_lates = KitchenLate.objects.filter(location=store.name).order_by('date')

            for kitchen_late in kitchen_lates:
                previous_date = kitchen_late.date - timezone.timedelta(days=1)
                previous_day_name = previous_date.strftime('%A')

                previous_day_dough_amount = WeeklyDoughAmount.objects.filter(
                    store=store,
                    day=previous_day_name
                ).first()

                if previous_day_dough_amount:
                    comparison_value = previous_day_dough_amount.dough_amount - kitchen_late.old_balls_total
                    comparison, created = Comparison.objects.get_or_create(
                        store=store,
                        date=previous_date,  # Use previous_date here
                        defaults={
                            'dough_amount': previous_day_dough_amount.dough_amount,
                            'old_balls_total': kitchen_late.old_balls_total,
                        }
                    )
                    if not created:
                        comparison.dough_amount = previous_day_dough_amount.dough_amount
                        comparison.old_balls_total = kitchen_late.old_balls_total
                        comparison.save()

                    if created:
                        self.stdout.write(self.style.SUCCESS(
                            f"Successfully created comparison for {store.name} on {previous_date}"
                        ))
                    else:
                        self.stdout.write(self.style.WARNING(
                            f"Comparison already exists for {store.name} on {previous_date}"
                        ))
                else:
                    self.stdout.write(self.style.ERROR(
                        f"No WeeklyDoughAmount entry for {store.name} on {previous_day_name}"
                    ))
