
from django.contrib import admin
from .models import KitchenLunch, KitchenLate, TerminalLunch, TerminalLate,TerminalSaturdayCleaning, KitchenSpecialcleaningMonday, \
    DryStorageCleaning, WednesdayCleaning, ApartmentCleaning, KitchenLunchTask, KitchenLateTask


@admin.register(KitchenLunch)
class KitchenLunchAdmin(admin.ModelAdmin):
    list_display = ('date', 'location','name', 'today_balls_total','comments')
from django.contrib import admin
from .models import KitchenLunch

@admin.register(KitchenLate)
class KitchenLateAdmin(admin.ModelAdmin):
    list_display = ('date', 'location','name',  'pizza_grade','tomorrow_balls_total','old_balls_total','old_balls_trash','balls_broken_today','pizzas_broken_today','comments')

    class Media:
        css = {
            'all': ('admin/css/admin.css',)  # Correct path to the CSS file
        }
        js = ('admin/js/admin.js',)  # Correct path to the JS file

@admin.register(TerminalLunch)
class TerminalLunchAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','boden_gastraum_cleaned','comments')
@admin.register(TerminalLate)
class TerminalLateAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')
@admin.register(KitchenSpecialcleaningMonday)
class KitchenSpecialCleaningMondayAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')
@admin.register(DryStorageCleaning)
class DryStorageCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')

@admin.register(WednesdayCleaning)
class DryStorageCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')

@admin.register(ApartmentCleaning)
class ApartmentCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')
@admin.register(KitchenLunchTask)
class KitchenLunchTaskAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','task_kitchen_cleaned','task_enough_laundry', 'task_laundry_drying', 'comments')
@admin.register(KitchenLateTask)
class KitchenLateTaskAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','washing_machine_status','washing_machine_person','comments','side','soap_WC_sufficient','toilet_paper_WC_sufficient','grease_remover_kitchen_sufficient','washingup_liquid_kitchen_sufficient','blue_roll_kitchen_sufficient')

    class Media:
        css = {
            'all': ('admin/css/admin.css',)  # Correct path to the CSS file
        }
        js = ('admin/js/admin.js',)  # Correct path to the JS file

from .models import Store, WeeklyDoughAmount

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)


from django.contrib import admin

from .models import WeeklyDoughAmount

class WeeklyDoughAmountAdmin(admin.ModelAdmin):
    list_display = ('store', 'day', 'dough_amount')
    search_fields = ('store__name', 'day')
    list_filter = ('store', 'day')

admin.site.register(WeeklyDoughAmount, WeeklyDoughAmountAdmin)

from pizza_ordering.models import Store, WeeklyDoughAmount, KitchenLate, Comparison
from django.utils import timezone

class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('date', 'store', 'dough_amount', 'get_next_day_old_balls_total', 'comparison_value')

    def get_next_day_old_balls_total(self, obj):
        if obj.date is not None:
            next_day = obj.date + timezone.timedelta(days=1)
            kitchen_late = KitchenLate.objects.filter(location=obj.store.name, date=next_day).first()
            return kitchen_late.old_balls_total if kitchen_late else None
        return None

    get_next_day_old_balls_total.short_description = 'Next Day Old Balls Total'

    def comparison_value(self, obj):
        if obj.date is not None:
            next_day = obj.date + timezone.timedelta(days=1)
            kitchen_late = KitchenLate.objects.filter(location=obj.store.name, date=next_day).first()
            if kitchen_late:
                return obj.dough_amount - kitchen_late.old_balls_total
        return None

    comparison_value.short_description = 'Comparison Value'

admin.site.register(Comparison, ComparisonAdmin)





from django.contrib import admin
from .models import BestBeforeDateCheck

class BestBeforeDateCheckAdmin(admin.ModelAdmin):
    list_display = ('location','date',  'latest_best_before_date', 'expired')
    list_filter = ('location', 'date','cured_meats_checked', 'cheese_checked', 'vegan_cheese_checked', 'expired')
    search_fields = ('location','date', 'expired')

admin.site.register(BestBeforeDateCheck, BestBeforeDateCheckAdmin)


@admin.register(TerminalSaturdayCleaning)
class TerminalSaturdayCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')


from .models import KitchenInventory

@admin.register(KitchenInventory)
class KitchenInventoryAdmin(admin.ModelAdmin):
    # Add all relevant fields to list_display to show them in the admin panel
    list_display = [
        'date', 'location', 'name',
        'einwegpapier_zickzack', 'einweghandschuhe_m', 'einweghandschuhe_l',
        'blaue_rolle_papierwischtuch', 'fettloeser_packzu', 'spuelmittel_packzu',
        'handseife', 'toilettenpapier', 'waschpulver', 'reiniger_spuelmaschine',
        'muellsack_gross', 'muellsack_klein', 'bodenreiniger','comments'
    ]

    # Optionally add filters or search fields to make it easier to find records
    list_filter = ['date', 'location']
    search_fields = ['location', 'name']

    class Media:
        css = {
            'all': ('admin/css/admin.css',)  # Correct path to the CSS file
        }
        js = ('admin/js/admin.js',)  # Correct path to the JS file



from .models import TerminalInventory


# Customizing the Inventory admin interface
class TerminalInventoryAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = [
        'date',
        'location',
        'name',
        'pizzakarton',
        'pizzapapier',
        'salatschale',
        'salatschale_deckel',
        'dressingschale',
        'dressingschale_deckel',
        'serviette_gast',
        'dip_becher',
        'dip_deckel',
        'bonrollen',
        'kugelschreiber',
        'textmarker_gelb',
        'filzstift_schwarz',
        'kellnerblock',
        'tesa_rollen',
        'etiketten_tiramisu',
        'etiketten_gn',
        'aufkleber_rot',
        'einwegloeffel',
        'einweggabel',
        'desinfektionsmittel',
        'salz_spuelmaschine',
        'speisekarte_blau',
        'menu_gelb',
        'trueffel_mayo',
        'dip_tuete',

        'zwiebel_chutney',
        # 'kuerbiskerne',
        'pflaster',
        'blaue_rolle',
        'tomatendose_pumarole_dolce',  # New field
        'tomatendose_san_marzano_dop',  # New field
        'comments'
    ]

    # Fields to search by in the search bar
    search_fields = ['name', 'location', 'date']

    # Fields to filter by in the admin interface
    list_filter = ['location', 'date']


    class Media:
        css = {
            'all': ('admin/css/admin.css',)  # Correct path to the CSS file
        }
        js = ('admin/js/admin.js',)  # Correct path to the JS file



# Register the Inventory model with the custom admin interface
admin.site.register(TerminalInventory, TerminalInventoryAdmin)

from .models import DoughroomCleaning

@admin.register(DoughroomCleaning)
class DoughroomCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','name','comments')

# from .models import EBikeCondition
# @admin.register(EBikeCondition)
# class EBikeConditionAdmin(admin.ModelAdmin):
#     list_display = ('location', 'name','calendar_week', 'bike_condition')
#     search_fields = ('location','name', 'calendar_week', 'bike_condition')
#     list_filter = ('location', 'calendar_week')

# from .models import Sonderreinigung

# class SonderreinigungAdmin(admin.ModelAdmin):
#     list_display = ('date','name', 'location', 'ventilation', 'spiderwebs', 'washer','comments')
#     list_filter = ('location', 'name','date')
#     search_fields = ('location', 'date')

# admin.site.register(Sonderreinigung,SonderreinigungAdmin)




# from django.contrib import admin
# from .models import CleanlinessOrderKitchen

# @admin.register(CleanlinessOrderKitchen)
# class CleanlinessOrderKitchenAdmin(admin.ModelAdmin):
#     list_display = (
#         'calendar_week',
#         'name',
#         'location',
#         'tiles',
#         'tables_downstairs',
#         'refrigerators_back',
#         'bottom_sink',
#         'extractor_hood',
#         'refrigerator',
#         'kav',
#         'created_at'
#     )
#     list_filter = ('calendar_week', 'location', 'created_at')
#     search_fields = ('name', 'location')
#     readonly_fields = ('created_at',)
#     fieldsets = (
#         ('General Information', {
#             'fields': ('calendar_week', 'name', 'location', 'created_at')
#         }),
#         ('Tiles', {
#             'fields': ('tiles', 'tiles_comment', 'tiles_rating', 'tiles_image')
#         }),
#         ('Tables Downstairs', {
#             'fields': ('tables_downstairs', 'tables_downstairs_comment', 'tables_downstairs_rating', 'tables_downstairs_image')
#         }),
#         ('Refrigerators Back', {
#             'fields': ('refrigerators_back', 'refrigerators_back_comment', 'refrigerators_back_rating', 'refrigerators_back_image')
#         }),
#         ('Bottom Sink', {
#             'fields': ('bottom_sink', 'bottom_sink_comment', 'bottom_sink_rating', 'bottom_sink_image')
#         }),
#         ('Extractor Hood', {
#             'fields': ('extractor_hood', 'extractor_hood_comment', 'extractor_hood_rating', 'extractor_hood_image')
#         }),
#         ('Refrigerator', {
#             'fields': ('refrigerator', 'refrigerator_comment', 'refrigerator_rating', 'refrigerator_image')
#         }),
#         ('KAV', {
#             'fields': ('kav', 'kav_comment', 'kav_rating', 'kav_image')
#         }),
#         ('Additional Measures', {
#             'fields': ('measures',)
#         }),
#     )

# from django.contrib import admin
# from .models import CleanlinessOrderTerminal

# @admin.register(CleanlinessOrderTerminal)
# class CleanlinessOrderTerminalAdmin(admin.ModelAdmin):
#     list_display = (
#         'calendar_week',
#         'name',
#         'location',
#         'floor',
#         'tiles',
#         'refrigerator',
#         'counter',
#         'lamps',
#         'tables_chairs',
#         'windows',
#         'created_at',
#     )
#     list_filter = ('calendar_week', 'location', 'created_at')
#     search_fields = ('name', 'location')
#     readonly_fields = ('created_at',)
#     fieldsets = (
#         ('General Information', {
#             'fields': ('calendar_week', 'name', 'location', 'created_at')
#         }),
#         ('Floor', {
#             'fields': ('floor', 'floor_comment', 'floor_rating', 'floor_image')
#         }),
#         ('Tiles', {
#             'fields': ('tiles', 'tiles_comment', 'tiles_rating', 'tiles_image')
#         }),
#         ('Refrigerator', {
#             'fields': ('refrigerator', 'refrigerator_comment', 'refrigerator_rating', 'refrigerator_image')
#         }),
#         ('Counter', {
#             'fields': ('counter', 'counter_comment', 'counter_rating', 'counter_image')
#         }),
#         ('Lamps', {
#             'fields': ('lamps', 'lamps_comment', 'lamps_rating', 'lamps_image')
#         }),
#         ('Tables and Chairs', {
#             'fields': ('tables_chairs', 'tables_chairs_comment', 'tables_chairs_rating', 'tables_chairs_image')
#         }),
#         ('Windows', {
#             'fields': ('windows', 'windows_comment', 'windows_rating', 'windows_image')
#         }),
#         ('Additional Measures', {
#             'fields': ('measures',)
#         }),
#     )
# from django.contrib import admin
# from .models import CleanlinessOrderStorage

# @admin.register(CleanlinessOrderStorage)
# class CleanlinessOrderStorageAdmin(admin.ModelAdmin):
#     list_display = (
#         'calendar_week',
#         'name',
#         'location',
#         'floor',
#         'garbage',
#         'tidiness',
#         'inventory',
#         'created_at',
#     )
#     list_filter = ('calendar_week', 'location', 'created_at')
#     search_fields = ('name', 'location')
#     readonly_fields = ('created_at',)
#     fieldsets = (
#         ('General Information', {
#             'fields': ('calendar_week', 'name', 'location', 'created_at')
#         }),
#         ('Floor', {
#             'fields': ('floor', 'floor_comment', 'floor_rating', 'floor_image')
#         }),
#         ('Garbage', {
#             'fields': ('garbage', 'garbage_comment', 'garbage_rating', 'garbage_image')
#         }),
#         ('Tidiness', {
#             'fields': ('tidiness', 'tidiness_comment', 'tidiness_rating', 'tidiness_image')
#         }),
#         ('Inventory', {
#             'fields': ('inventory', 'inventory_comment', 'inventory_rating', 'inventory_image')
#         }),
#         ('Additional Measures', {
#             'fields': ('measures',)
#         }),
#     )
#     from django.contrib import admin
# from .models import CleanlinessOrderApartment

# @admin.register(CleanlinessOrderApartment)
# class CleanlinessOrderApartmentAdmin(admin.ModelAdmin):
#     list_display = (
#         'calendar_week',
#         'name',
#         'location',
#         'floor',
#         'shelf',
#         'garbage',
#         'cold_room',
#         'washroom_kitchen',
#         'wc',
#         'created_at',
#     )
#     list_filter = ('calendar_week', 'location', 'created_at')
#     search_fields = ('name', 'location')
#     readonly_fields = ('created_at',)
#     fieldsets = (
#         ('General Information', {
#             'fields': ('calendar_week', 'name', 'location', 'created_at')
#         }),
#         ('Floor', {
#             'fields': ('floor', 'floor_comment', 'floor_rate', 'floor_image')
#         }),
#         ('Shelf', {
#             'fields': ('shelf', 'shelf_comment', 'shelf_rate', 'shelf_image')
#         }),
#         ('Garbage', {
#             'fields': ('garbage', 'garbage_comment', 'garbage_rate', 'garbage_image')
#         }),
#         ('Cold Room', {
#             'fields': ('cold_room', 'cold_room_comment', 'cold_room_rate', 'cold_room_image')
#         }),
#         ('Washroom / Kitchen', {
#             'fields': ('washroom_kitchen', 'washroom_kitchen_comment', 'washroom_kitchen_rate', 'washroom_kitchen_image')
#         }),
#         ('WC', {
#             'fields': ('wc', 'wc_comment', 'wc_rate', 'wc_image')
#         }),
#         ('Additional Measures', {
#             'fields': ('measures',)
#         }),
#     )
# from django.contrib import admin
# from .models import EBikeCondition

# @admin.register(EBikeCondition)
# class EBikeConditionAdmin(admin.ModelAdmin):
#     # Fields to display in the list view
#     list_display = ('date', 'calendar_week', 'location', 'name', 'bike_rate', 'created_at')

#     # Filters available in the sidebar
#     list_filter = ('location', 'calendar_week', 'date')

#     # Search functionality for the admin
#     search_fields = ('name', 'location', 'bike_condition')

#     # Ordering of entries in the list view
#     ordering = ('-date',)

#     # Fields that cannot be edited directly
#     readonly_fields = ('created_at',)

#     # Grouping fields into sections in the detail view
#     fieldsets = (
#         (None, {
#             'fields': ('date', 'calendar_week', 'location', 'name', 'bike_condition', 'bike_rate', 'bike_image', 'created_at')
#         }),
#         ('Advanced options', {
#             'classes': ('collapse',),
#             'fields': (),  # Leave empty or include other advanced fields if needed
#         }),
#     )

# from django.contrib import admin
# from .models import Sonderreinigung

# @admin.register(Sonderreinigung)
# class SonderreinigungAdmin(admin.ModelAdmin):
#     # Fields to display in the list view
#     list_display = (
#         'date',
#         'location',
#         'name',
#         'ventilation',
#         'spiderwebs',
#         'washer',
#         'created_at',
#     )

#     # Filters available in the sidebar
#     list_filter = (
#         'location',
#         'date',
#         'ventilation',
#         'spiderwebs',
#         'washer',
#     )

#     # Search functionality for the admin
#     search_fields = (
#         'name',
#         'location',
#         'comments',
#     )

#     # Ordering of entries in the list view
#     ordering = ('-date',)

#     # Fields that cannot be edited directly
#     readonly_fields = ('created_at',)

#     # Grouping fields into sections in the detail view
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'date',
#                 'location',
#                 'name',
#                 'ventilation',
#                 'ventilation_rate',
#                 'ventilation_image',
#                 'spiderwebs',
#                 'spiderwebs_rate',
#                 'spiderwebs_image',
#                 'washer',
#                 'washer_rate',
#                 'washer_image',
#                 'comments',
#                 'created_at',
#             )
#         }),
#         ('Advanced options', {
#             'classes': ('collapse',),
#             'fields': (),
#         }),
#     )
from django.contrib import admin
from .models import Sonderreinigung

@admin.register(Sonderreinigung)
class SonderreinigungAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'name', 'ventilation', 'spiderwebs', 'washer', 'created_at')
    list_filter = ('location', 'date', 'ventilation', 'spiderwebs', 'washer')
    search_fields = ('name', 'location', 'comments')
    ordering = ('-date',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('date', 'location', 'name', 'comments')
        }),
        ('Ventilation Details', {
            'fields': ('ventilation', 'ventilation_rate', 'ventilation_image')
        }),
        ('Spiderwebs Details', {
            'fields': ('spiderwebs', 'spiderwebs_rate', 'spiderwebs_image')
        }),
        ('Washer Details', {
            'fields': ('washer', 'washer_rate', 'washer_image')
        }),
        ('Other Information', {
            'fields': ('created_at',)
        }),
    )
