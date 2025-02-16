from django.db import models

class KitchenLunch(models.Model):
    date = models.DateField()
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES,default='JP23')
    comments=models.TextField(null=True,blank=True)

    today_balls_total = models.IntegerField()
    # yesterday_balls_total = models.IntegerField()

    class Meta:
        verbose_name = "Kitchen Department Lunch Shift(Quantity)"
        verbose_name_plural = "Kitchen Department Lunch Shift(Quantity)"

class KitchenLate(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    pizza_grade = models.IntegerField()
    tomorrow_balls_total = models.IntegerField()
    old_balls_total = models.IntegerField(verbose_name="How many of these are new", null=True, blank=True)
    old_balls_trash = models.IntegerField(verbose_name="How many old balls went in the trash", null=True, blank=True)
    balls_broken_today = models.IntegerField()
    pizzas_broken_today = models.IntegerField()

    class Meta:
        verbose_name = "Kitchen Department Late Shift(Quantity)"
        verbose_name_plural = "Kitchen Department Late Shift(Quantity)"


from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)

class TerminalLunch(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    Boden_Gastraum_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    boden_gastraum_cleaned=models.CharField(max_length=3, choices=Boden_Gastraum_CHOICES , blank=True, null=True)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Terminal Department Lunch Shift"
        verbose_name_plural = "Terminal Department Lunch Shift"


class TerminalLate(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    # HALLWAY_MOPPED_CHOICES = [
    #     ('yes', 'YES'),
    #     ('no', 'NO'),
    # ]
    # CELLAR_TIDY_CHOICES = [
    #     ('yes', 'YES'),
    #     ('no', 'NO'),
    # ]
    # REPLENISHED_CHOICES = [
    #     ('yes', 'YES'),
    #     ('no', 'NO'),
    # ]


    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)


    class Meta:
        verbose_name = "Terminal Department Late Shift"
        verbose_name_plural = "Terminal Department Late Shift"

class KitchenSpecialcleaningMonday(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Kitchen Department Specialcleaning(Monday)"
        verbose_name_plural = "Kitchen Department Specialcleaning(Monday)"

class DryStorageCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Dry Storage Cleaning(Wednesday)"
        verbose_name_plural = "Dry Storage Cleaning(Wednesday)"

class WednesdayCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Kitchen Special Cleaning(Wednesday)"
        verbose_name_plural = "Kitchen Special Cleaning(Wednesday)"

class ApartmentCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Apartment Cleaning(Wednesday)"
        verbose_name_plural = "Apartment Cleaning(Wednesday)"

class KitchenLunchTask(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    KITCHEN_CLEANED_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    ENOUGH_LAUNDRY_CHOICES=[
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    LAUNDRY_HUNG_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    task_kitchen_cleaned = models.CharField(max_length=3, choices=KITCHEN_CLEANED_CHOICES, blank=True, null=True,verbose_name="Kitchen cleaned according to instructions")
    task_enough_laundry=models.CharField(max_length=3, choices=ENOUGH_LAUNDRY_CHOICES, blank=True, null=True,verbose_name="Was there enough laundry")
    task_laundry_drying = models.CharField(max_length=3, choices=LAUNDRY_HUNG_CHOICES, blank=True, null=True,
                                         verbose_name="Fresh laundry hung to dry")
    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Kitchen Department Lunch Shift(Task)"
        verbose_name_plural = "Kitchen Department Lunch Shift(Task)"

class KitchenLateTask(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]

    SIDE_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    soap_WC_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    toilet_paper_WC_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]

    grease_remover_kitchen_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    washingup_liquid_kitchen_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    blue_roll_kitchen_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    YES_NO_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES,default=False) # New side field
    comments = models.TextField(null=True, blank=True)
    soap_WC_sufficient = models.CharField(max_length=3, choices=soap_WC_sufficient_CHOICES, blank=True, null=True)
    toilet_paper_WC_sufficient=models.CharField(max_length=3, choices=toilet_paper_WC_sufficient_CHOICES, blank=True, null=True)
    grease_remover_kitchen_sufficient=models.CharField(max_length=3, choices=grease_remover_kitchen_sufficient_CHOICES, blank=True, null=True)
    washingup_liquid_kitchen_sufficient=models.CharField(max_length=3, choices=washingup_liquid_kitchen_sufficient_CHOICES, blank=True, null=True)
    blue_roll_kitchen_sufficient=models.CharField(max_length=3, choices=blue_roll_kitchen_sufficient_CHOICES, blank=True, null=True)

    # New fields for washing machine status and person
    washing_machine_status = models.CharField(max_length=3, choices=YES_NO_CHOICES, blank=True, null=True,
                                              verbose_name="Washing machine started")
    washing_machine_person = models.CharField(max_length=100, blank=True, null=True,
                                              verbose_name="Name of the person who started the washing machine today")

    class Meta:
        verbose_name = "Kitchen Department Late Shift(Task)"
        verbose_name_plural = "Kitchen Department Late Shift(Task)"


class Store(models.Model):
    STORE_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    name = models.CharField(max_length=50, choices=STORE_CHOICES, unique=True)

    def __str__(self):
        return self.name
from django.utils.translation import gettext_lazy as _
class WeeklyDoughAmount(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='weekly_dough_amounts')
    dough_amount = models.IntegerField()
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK,null=True)

    class Meta:
        unique_together = ('store', 'day')

    def __str__(self):
        return f"{self.store.name} - {self.dough_amount} on {self.day}"

class Comparison(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    dough_amount = models.IntegerField()
    old_balls_total = models.IntegerField()
    comparison_value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.store.name} - {self.date} - Comparison Value: {self.comparison_value}"



from django.db import models

LOCATION_CHOICES = [
    ('JP23', 'JP23'),
    ('KP5', 'KP5'),
    ('TS17', 'TS17'),
]

def get_calendar_week(date):
    return date.isocalendar()[1]
from django.core.validators import MinValueValidator, MaxValueValidator
class CleanlinessOrderKitchen(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    tiles = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    tiles_comment = models.TextField(blank=True, null=True)  # Comment for tiles

    tiles_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    tiles_image = models.ImageField(upload_to='tiles_images/', blank=True, null=True)  # Image for tiles

    # Tables downstairs
    tables_downstairs = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    tables_downstairs_comment = models.TextField(blank=True, null=True)  # Comment for tables downstairs
    tables_downstairs_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    tables_downstairs_image = models.ImageField(upload_to='tables_downstairs_images/', blank=True,
                                                null=True)  # Image for tables downstairs

    # Refrigerators back
    refrigerators_back = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    refrigerators_back_comment = models.TextField(blank=True, null=True)  # Comment for refrigerators back
    refrigerators_back_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    refrigerators_back_image = models.ImageField(upload_to='refrigerators_back_images/', blank=True,
                                                 null=True)  # Image for refrigerators back

    # Bottom sink
    bottom_sink = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    bottom_sink_comment = models.TextField(blank=True, null=True)  # Comment for bottom sink
    bottom_sink_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    bottom_sink_image = models.ImageField(upload_to='bottom_sink_images/', blank=True,
                                          null=True)  # Image for bottom sink

    # Extractor hood
    extractor_hood = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    extractor_hood_comment = models.TextField(blank=True, null=True)  # Comment for extractor hood
    extractor_hood_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    extractor_hood_image = models.ImageField(upload_to='extractor_hood_images/', blank=True,
                                             null=True)  # Image for extractor hood

    # Refrigerator
    refrigerator = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    refrigerator_comment = models.TextField(blank=True, null=True)  # Comment for refrigerator
    refrigerator_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    refrigerator_image = models.ImageField(upload_to='refrigerator_images/', blank=True,
                                           null=True)  # Image for refrigerator

    # KAV
    kav = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    kav_comment = models.TextField(blank=True, null=True)  # Comment for KAV
    kav_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    kav_image = models.ImageField(upload_to='kav_images/', blank=True, null=True)  # Image for KAV

    measures = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"Review Checklists for Apartment on {self.calendar_week}"


class CleanlinessOrderTerminal(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    floor = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    floor_comment = models.TextField(blank=True, null=True)
    floor_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    floor_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    tiles = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    tiles_comment = models.TextField(blank=True, null=True)
    tiles_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    tiles_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    refrigerator = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    refrigerator_comment = models.TextField(blank=True, null=True)
    refrigerator_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    refrigerator_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    counter = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    counter_comment = models.TextField(blank=True, null=True)
    counter_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    counter_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    lamps = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    lamps_comment = models.TextField(blank=True, null=True)
    lamps_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    lamps_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    tables_chairs = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    tables_chairs_comment = models.TextField(blank=True, null=True)
    tables_chairs_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    tables_chairs_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    windows = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    windows_comment = models.TextField(blank=True, null=True)
    windows_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True
    )
    windows_image = models.ImageField(upload_to='cleanliness_images/', blank=True, null=True)

    measures = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Cleanliness Order for Terminal on {self.calendar_week}"

class CleanlinessOrderStorage(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    floor = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    garbage = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    tidiness = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    inventory = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    floor_comment = models.TextField(blank=True, null=True)  # Comment field for floor
    garbage_comment = models.TextField(blank=True, null=True)  # Comment field for garbage
    tidiness_comment = models.TextField(blank=True, null=True)  # Comment field for tidiness
    inventory_comment = models.TextField(blank=True, null=True)  # Comment field for inventory
    floor_rating = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    garbage_rating = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    tidiness_rating = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    inventory_rating = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    floor_image = models.ImageField(upload_to='images/floor/', blank=True, null=True)
    garbage_image = models.ImageField(upload_to='images/garbage/', blank=True, null=True)
    tidiness_image = models.ImageField(upload_to='images/tidiness/', blank=True, null=True)
    inventory_image = models.ImageField(upload_to='images/inventory/', blank=True, null=True)


    measures = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Cleanliness Order for Storage on {self.calendar_week}"

class CleanlinessOrderApartment(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    floor = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    shelf = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    garbage = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    cold_room = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    washroom_kitchen = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    wc = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    floor_comment = models.TextField(blank=True, null=True)  # Comment for floor
    shelf_comment = models.TextField(blank=True, null=True)  # Comment for shelf
    garbage_comment = models.TextField(blank=True, null=True)  # Comment for garbage
    cold_room_comment = models.TextField(blank=True, null=True)  # Comment for cold room
    washroom_kitchen_comment = models.TextField(blank=True, null=True)  # Comment for washroom/kitchen
    wc_comment = models.TextField(blank=True, null=True)  # Comment for WC

    floor_rate = models.IntegerField(blank=True, null=True)  # New field
    shelf_rate = models.IntegerField(blank=True, null=True)  # New field
    garbage_rate = models.IntegerField(blank=True, null=True)  # New field
    cold_room_rate = models.IntegerField(blank=True, null=True)  # New field
    washroom_kitchen_rate = models.IntegerField(blank=True, null=True)  # New field
    wc_rate = models.IntegerField(blank=True, null=True)

    floor_image = models.ImageField(upload_to='floor_images/', blank=True, null=True)
    shelf_image = models.ImageField(upload_to='cleanliness/shelf/', blank=True, null=True)
    garbage_image = models.ImageField(upload_to='cleanliness/garbage/', blank=True, null=True)
    cold_room_image = models.ImageField(upload_to='cleanliness/cold_room/', blank=True, null=True)
    washroom_kitchen_image = models.ImageField(upload_to='cleanliness/washroom_kitchen/', blank=True, null=True)
    wc_image = models.ImageField(upload_to='cleanliness/wc/', blank=True, null=True)

    measures = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Cleanliness Order for Apartment on {self.calendar_week}"

class ReviewChecklistsKitchen(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    fulfillment_rate = models.CharField(max_length=4, choices=[
        ('75%', '75%'),
        ('85%', '85%'),
        ('90%', '90%'),
        ('95%', '95%'),
        ('100%', '100%')
    ])
    measures = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Review Checklists for Kitchen on {self.calendar_week}"

class ReviewChecklistsTerminal(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    fulfillment_rate = models.CharField(max_length=4, choices=[
        ('75%', '75%'),
        ('85%', '85%'),
        ('90%', '90%'),
        ('95%', '95%'),
        ('100%', '100%')
    ])
    measures = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Review Checklists for Terminal on {self.calendar_week}"

class ReviewChecklistsStorage(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    fulfillment_rate = models.CharField(max_length=4, choices=[
        ('75%', '75%'),
        ('85%', '85%'),
        ('90%', '90%'),
        ('95%', '95%'),
        ('100%', '100%')
    ])
    measures = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Review Checklists for Storage on {self.calendar_week}"

class ReviewChecklistsApartment(models.Model):
    calendar_week = models.PositiveIntegerField(null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    fulfillment_rate = models.CharField(max_length=4, choices=[
        ('75%', '75%'),
        ('85%', '85%'),
        ('90%', '90%'),
        ('95%', '95%'),
        ('100%', '100%')
    ])
    measures = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Review Checklists for Apartment on {self.calendar_week}"



class BestBeforeDateCheck(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField(null=True)
    cured_meats_checked = models.BooleanField(default=False)
    cheese_checked = models.BooleanField(default=False)
    vegan_cheese_checked = models.BooleanField(default=False)
    latest_best_before_date = models.DateField()
    expired = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.location} - {self.latest_best_before_date}"


class TerminalSaturdayCleaning(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=100,null=True, blank=True)
    comments = models.TextField(null=True, blank=True)



    def __str__(self):
        return f"{self.date} - {self.location}"


class CalendarWeekNotification(models.Model):
    calendar_week = models.IntegerField(unique=True)  # Unique week number
    notification_sent = models.BooleanField(default=False)  # Track if notification is sent

    def __str__(self):
        return f"Week {self.calendar_week} - Notification Sent: {self.notification_sent}"


class KitchenInventory(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    date = models.DateField()  # Date when the inventory was taken
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    name = models.CharField(max_length=100)  # Name of the person submitting the inventory
    comments=models.TextField(null=True,blank=True)

    # Items in the inventory
    einwegpapier_zickzack = models.PositiveIntegerField(default=0, verbose_name='Einwegpapier ZickZack (Einheit 100 St.)')
    einweghandschuhe_m = models.PositiveIntegerField(default=0, verbose_name='Einweghandschuhe M (Einheit)')
    einweghandschuhe_l = models.PositiveIntegerField(default=0, verbose_name='Einweghandschuhe L (Einheit)')
    blaue_rolle_papierwischtuch = models.PositiveIntegerField(default=0, verbose_name='Blaue Rolle Papierwischtuch (Stück)')
    fettloeser_packzu = models.PositiveIntegerField(default=0, verbose_name='Fettlöser PackZu (Stück)')
    spuelmittel_packzu = models.PositiveIntegerField(default=0, verbose_name='Spülmittel PackZu (Stück)')
    handseife = models.PositiveIntegerField(default=0, verbose_name='Handseife (Stück)')
    toilettenpapier = models.PositiveIntegerField(default=0, verbose_name='Toilettenpapier (Stück)')
    waschpulver = models.PositiveIntegerField(default=0, verbose_name='Waschpulver (Stück)')
    reiniger_spuelmaschine = models.PositiveIntegerField(default=0, verbose_name='Reiniger Spülmaschine (Stück)')
    muellsack_gross = models.PositiveIntegerField(default=0, verbose_name='Müllsack groß (Stück)')
    muellsack_klein = models.PositiveIntegerField(default=0, verbose_name='Müllsack klein (Stück)')
    bodenreiniger = models.PositiveIntegerField(default=0, verbose_name='Bodenreiniger (Stück)')

    def __str__(self):
        return f"Inventory on {self.date} at {self.location} by {self.name}"
    class Meta:
        verbose_name = "Kitchen Inventory(Non-Food)"
        verbose_name_plural = "Kitchen Inventory(Non-Food)"

class TerminalInventory(models.Model):
    # Define location choices
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]

    # General fields
    date = models.DateField(verbose_name="Datum")
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, verbose_name="Standort")
    name = models.CharField(max_length=100, verbose_name="Name")
    comments=models.TextField(null=True,blank=True)

    # PERGANO section
    pizzakarton = models.PositiveIntegerField(default=0, verbose_name="Pizzakarton (Einheit 100 St.)")
    pizzapapier = models.PositiveIntegerField(default=0, verbose_name="Pizzapapier (Einheit 1000 St.)")
    salatschale = models.PositiveIntegerField(default=0, verbose_name="Salatschale (Einheit 50 St.)")
    salatschale_deckel = models.PositiveIntegerField(default=0, verbose_name="Salatschale Deckel (Einheit 50 St.)")
    dressingschale = models.PositiveIntegerField(default=0, verbose_name="Dressingschale (Einheit 100 St.)")
    dressingschale_deckel = models.PositiveIntegerField(default=0, verbose_name="Dressingschale Deckel (Einheit 100 St.)")
    serviette_gast = models.PositiveIntegerField(default=0, verbose_name="Serviette Gast (Einheit 100 St.)")
    dip_becher= models.PositiveIntegerField(default=0, verbose_name="Dip Becher (Einheit)")
    dip_deckel= models.PositiveIntegerField(default=0, verbose_name="Dip Deckel (Einheit)")

    # AMAZON section
    bonrollen = models.PositiveIntegerField(default=0, verbose_name="Bonrollen (Stück)")
    kugelschreiber = models.PositiveIntegerField(default=0, verbose_name="Kugelschreiber (Stück)")
    textmarker_gelb = models.PositiveIntegerField(default=0, verbose_name="Textmarker gelb (Stück)")
    filzstift_schwarz = models.PositiveIntegerField(default=0, verbose_name="Filzstift schwarz (Stück)")
    kellnerblock = models.PositiveIntegerField(default=0, verbose_name="Kellnerblock (Stück)")
    tesa_rollen = models.PositiveIntegerField(default=0, verbose_name="Tesa Rollen (Stück)")
    etiketten_tiramisu = models.PositiveIntegerField(default=0, verbose_name="Etiketten Warenauszeichner (Stück)")
    etiketten_gn = models.PositiveIntegerField(default=0, verbose_name="Etiketten Datum GN (Stück)")
    aufkleber_rot = models.PositiveIntegerField(default=0, verbose_name="Aufkleber rot MHD (Stück)")
    einwegloeffel = models.PositiveIntegerField(default=0, verbose_name="Einweglöffel (Stück)")
    einweggabel = models.PositiveIntegerField(default=0, verbose_name="Einweggabel (Stück)")
    desinfektionsmittel = models.PositiveIntegerField(default=0, verbose_name="Desinfektionsmittel (Einheit)")
    salz_spuelmaschine = models.PositiveIntegerField(default=0, verbose_name="Salz Spülmaschine (Einheit)")

    trueffel_mayo = models.PositiveIntegerField(default=0, verbose_name="Trüffel Mayo (Flasche)")
    dip_tuete = models.PositiveIntegerField(default=0, verbose_name="Dip Tüte (Einheit 50 St.)")
    zwiebel_chutney = models.PositiveIntegerField(default=0, verbose_name="Zwiebel Chutney (Glas)")
    # kuerbiskerne = models.PositiveIntegerField(default=0, verbose_name="Kürbiskerne (Tüte)")

    pflaster=models.PositiveIntegerField(default=0, verbose_name="Pflaster (Stück)")
    blaue_rolle=models.PositiveIntegerField(default=0, verbose_name="Blaue Rolle (Stück)")


    # FLYER section
    speisekarte_blau = models.PositiveIntegerField(default=0, verbose_name="Speisekarte blau (Einheit)")
    menu_gelb = models.PositiveIntegerField(default=0, verbose_name="Menú gelb (Einheit)")

    tomatendose_pumarole_dolce = models.PositiveIntegerField(default=0, verbose_name="Tomatendose Pumarole Dolce")
    tomatendose_san_marzano_dop = models.PositiveIntegerField(default=0, verbose_name="Tomatendose San Marzano D.O.P.")


    def __str__(self):
        return f"{self.location} - {self.date} - {self.name}"

    class Meta:
        verbose_name = "Terminal Inventory(Non-Food)"
        verbose_name_plural = "Terminal Inventory(Non-Food)"

class DoughroomCleaning(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments = models.TextField(blank=True)

    # Task fields (you can adjust names and types as needed)
    # table_no_flour = models.BooleanField(default=False)
    # table_surface_cleaned = models.BooleanField(default=False)
    # table_lower_shelf_cleaned = models.BooleanField(default=False)
    # shelf_cleaned = models.BooleanField(default=False)
    # dough_machine_inside_cleaned = models.BooleanField(default=False)
    # dough_machine_outside_cleaned = models.BooleanField(default=False)
    # scale_cleaned_connected = models.BooleanField(default=False)
    # sink_surface_cleaned = models.BooleanField(default=False)
    # floor_swept = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Dough Room Cleaning"
        verbose_name_plural = "Dough Room Cleanings"
        ordering = ['-date']  # Order by date descending

    def __str__(self):
        return f"{self.date} - {self.name}"

class EBikeCondition(models.Model):
    STORE_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]

    date = models.DateField(help_text="The date the condition was reported")
    calendar_week = models.CharField(max_length=20, help_text="The calendar week based on the selected date")
    location = models.CharField(max_length=10, choices=STORE_CHOICES, help_text="The store where the bikes are located")
    name = models.CharField(max_length=100, null=True, blank=True)
    bike_condition = models.TextField(help_text="The condition of the bikes and actions to be taken")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    bike_rate = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    bike_image = models.ImageField(upload_to='bike_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.location} - CW {self.calendar_week} ({self.date})"

    class Meta:
        verbose_name = "E-Bike Condition"
        verbose_name_plural = "E-Bike Conditions"
        ordering = ['-date']

class Sonderreinigung(models.Model):
    STORE_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Ja'),
        ('no', 'Nein'),
    ]

    date = models.DateField(verbose_name="Datum")
    location = models.CharField(max_length=10, choices=STORE_CHOICES, verbose_name="Store")
    name = models.CharField(max_length=100, null=True, blank=True)
    ventilation = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Lüftungsgitter Kühlzelle")
    spiderwebs = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Spinnweben Eingangsbereich")
    washer = models.CharField(max_length=3, choices=YES_NO_CHOICES, verbose_name="Waschmaschine Flusensieb reinigen")
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    ventilation_rate = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    ventilation_image = models.ImageField(upload_to='ventilation_images/', blank=True, null=True)
    spiderwebs_rate = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    spiderwebs_image = models.ImageField(upload_to='spiderwebs_images/', blank=True, null=True)
    washer_rate = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True
    )
    washer_image = models.ImageField(upload_to='washer_images/', blank=True, null=True)




    class Meta:
        verbose_name = "Sonderreinigung"
        verbose_name_plural = "Sonderreinigungen"
        ordering = ['-date']

    def __str__(self):
        return f"{self.location} - {self.date}"

