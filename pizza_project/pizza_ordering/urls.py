from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('department_selection/', views.department_shift_selection, name='department_shift_selection'),  # Department and shift selection page and submission
    # path('kitchenlunch/', views.kitchen_lunch_form, name='kitchen_lunch_form'),  # URL for kitchen lunch form
    path('kitchenlate/', views.kitchen_late_form, name='kitchen_late_form'),  # URL for kitchen late form
    # Define URLs for TerminalLunch and TerminalLate similarly
path('kitchenlunch_submit/', views.kitchen_lunch_submit, name='kitchen_lunch_submit'), # URL for handling kitchen lunch form submission
path('kitchen_lunch_form/', views.kitchen_lunch_form, name='kitchen_lunch_form'),
path('kitchenlunchdashboard/', views.kitchen_lunch_dashboard, name='kitchen_lunch_dashboard'), # Add this URL pattern
path('kitchenlate_submit/', views.kitchen_late_submit, name='kitchen_late_submit'),
path('kitchenlatedashboard/', views.kitchen_late_dashboard, name='kitchen_late_dashboard'), # Add this URL pattern
path('terminallunch/', views.terminal_lunch_form, name='terminal_lunch_form'),
path('terminallunch_submit/', views.terminal_lunch_submit, name='terminal_lunch_submit'),
    path('terminallunchdashboard/', views.terminal_lunch_dashboard, name='terminal_lunch_dashboard'),
    path('terminallate/', views.terminal_late_form, name='terminal_late_form'),
    path('terminallate_submit/', views.terminal_late_submit, name='terminal_late_submit'),
    path('terminallatedashboard/', views.terminal_late_dashboard, name='terminal_late_dashboard'),
    path('kitchenspecialcleaningmonday_submit/', views.kitchen_specialcleaning_monday_submit, name='kitchen_specialcleaning_monday_submit'),
    path('kitchenspecialcleaningmondaydashboard/', views.kitchen_specialcleaning_monday_dashboard, name='kitchen_specialcleaning_monday_dashboard'),
path('kitchen_specialcleaning_monday/', views.kitchen_specialcleaning_monday, name='kitchen_specialcleaning_monday'),


path('drystorage_cleaning_submit/', views.drystorage_cleaning_submit, name='drystorage_cleaning_submit'),
    path('dry_storage_cleaning_form/', views.dry_storage_cleaning_form, name='dry_storage_cleaning_form'),
    path('drystorage_cleaning_dashboard/', views.drystorage_cleaning_dashboard, name='drystorage_cleaning_dashboard'),

path('wednesday_cleaning_submit/', views.wednesday_cleaning_submit, name='wednesday_cleaning_submit'),
    path('wednesday_cleaning_kitchen/', views.wednesday_cleaning_kitchen, name='wednesday_cleaning_kitchen'),
    path('wednesday_cleaning_dashboard/', views.wednesday_cleaning_dashboard, name='wednesday_cleaning_dashboard'),

path('apartment_cleaning_submit/', views.apartment_cleaning_submit, name='apartment_cleaning_submit'),
    path('apartment_cleaning_form/', views.apartment_cleaning_form, name='apartment_cleaning_form'),
    path('apartment_cleaning_dashboard/', views.apartment_cleaning_dashboard, name='apartment_cleaning_dashboard'),

path('kitchen_lunch_task_submit/', views.kitchen_lunch_task_submit, name='kitchen_lunch_task_submit'),
    path('kitchen_lunch_task/', views.kitchen_lunch_task, name='kitchen_lunch_task'),
    path('kitchen_lunch_task_dashboard/', views.kitchen_lunch_task_dashboard, name='kitchen_lunch_task_dashboard'),

path('kitchen_late_task_submit/', views.kitchen_late_task_submit, name='kitchen_late_task_submit'),
    path('kitchen_late_task/', views.kitchen_late_task, name='kitchen_late_task'),
    path('kitchen_late_task_dashboard/', views.kitchen_late_task_dashboard, name='kitchen_late_task_dashboard'),


    path('select_store/', views.select_store, name='select_store'),



    path('management_selection_success/', views.management_selection_success, name='management_selection_success'),
path('management_selection/', views.management_selection, name='management_selection'),
    path('cleanliness_order_kitchen/', views.cleanliness_order_kitchen, name='cleanliness_order_kitchen'),
    path('cleanliness_order_terminal/', views.cleanliness_order_terminal, name='cleanliness_order_terminal'),
    path('cleanliness_order_storage/', views.cleanliness_order_storage, name='cleanliness_order_storage'),
    path('cleanliness_order_apartment/',views.cleanliness_order_apartment, name='cleanliness_order_apartment'),
    path('review_checklists_kitchen/', views.review_checklists_kitchen, name='review_checklists_kitchen'),
    path('review_checklists_terminal/', views.review_checklists_terminal, name='review_checklists_terminal'),
    path('review_checklists_storage/', views.review_checklists_storage, name='review_checklists_storage'),
    path('review_checklists_apartment/', views.review_checklists_apartment, name='review_checklists_apartment'),
path('admin-view/', views.admin_view, name='admin_view'),

    path('best-before-date/', views.best_before_date_check, name='best_before_date_check'),
    path('best-before-date-success/', views.best_before_date_success, name='best_before_date_success'),


    path('terminal_saturday_cleaning_form/', views.terminal_saturday_cleaning_form, name='terminal_saturday_cleaning_form'),
    path('terminal_saturday_cleaning_submit/', views.terminal_saturday_cleaning_submit, name='terminal_saturday_cleaning_submit'),
    path('terminal_saturday_cleaning_dashboard/', views.terminal_saturday_cleaning_dashboard, name='terminal_saturday_cleaning_dashboard'),

    path('inventory_kitchen/', views.inventory_kitchen, name='inventory_kitchen'),
    path('inventory_terminal/', views.inventory_terminal, name='inventory_terminal'),
    path('success_best/', views.success_best, name='success_best'),
    path('doughroom_cleaning/', views.doughroom_cleaning, name='doughroom_cleaning'),
    path('doughroom_cleaning_submit/', views.doughroom_cleaning_submit, name='doughroom_cleaning_submit'),
    path('ebikes_condition_view/', views.ebikes_condition_view, name='ebikes_condition_view'),
    path('special_cleaning/', views.special_cleaning, name='special_cleaning'),



]

