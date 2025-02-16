from django.shortcuts import render, redirect
from .models import KitchenLunch, KitchenLate, TerminalLunch, TerminalLate, KitchenSpecialcleaningMonday, \
    DryStorageCleaning, WednesdayCleaning, ApartmentCleaning, KitchenLunchTask, KitchenLateTask

def login(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == '0001':
            return redirect('department_shift_selection')  # Replace with your actual URL name
        elif code == '0005':
            return redirect('management_selection')
        elif code == 'Forza19':
            return redirect('admin_view')
        else:
            return render(request, 'pizza_ordering/login.html', {'error_message': 'Invalid code. Please try again.'})

    return render(request, 'pizza_ordering/login.html')
def department_shift_selection(request):
    if request.method == 'POST':

        selected_department = request.POST.get('department')
        selected_shift = request.POST.get('shift')
        selected_section = request.POST.get('section')
        selected_action=request.POST.get('action')
        selected_food_category=request.POST.get('food_category')

        if selected_department == 'kitchen' and selected_shift == 'lunch':
            if selected_action == 'quantity':
                return redirect('kitchen_lunch_form')# Corrected redirection
            elif selected_action== 'task':
                return redirect('kitchen_lunch_task')
        elif selected_department == 'kitchen' and selected_shift == 'late':
            if selected_action == 'quantity':
                return redirect('kitchen_late_form')
            elif selected_action== 'task':
                return redirect('kitchen_late_task')
        elif selected_department == 'terminal' and selected_shift == 'lunch':
            return redirect('terminal_lunch_form')
        elif selected_department == 'terminal' and selected_shift == 'late':
            return redirect('terminal_late_form')
        elif selected_department == 'terminal' and selected_shift == 'saturday_cleaning':
            return redirect('terminal_saturday_cleaning_form')
        elif selected_department == 'kitchen' and selected_shift == 'specialcleaningmonday':
            return redirect('kitchen_specialcleaning_monday')
        elif selected_department == 'doughroom' and selected_shift == 'cleaning':
            return redirect('doughroom_cleaning')

        elif selected_department == 'kitchen' and selected_shift == 'best_before_date':
            return redirect('best_before_date_check')
        elif selected_department == 'doughroom' and selected_shift == 'weekly_dough_amount':
            return redirect('select_store')
        elif selected_department == 'kitchen' and selected_shift == 'specialcleaningwednesday':
            if selected_section == 'kitchen':
                return redirect('wednesday_cleaning_kitchen')
            elif selected_section == 'dry_storage':
                return redirect('dry_storage_cleaning_form')
            elif selected_section == 'apartment':
                return redirect('apartment_cleaning_form')
        elif selected_department == 'kitchen' and selected_shift == 'inventory':
            if selected_food_category == 'non_food':
                return redirect('inventory_kitchen')

        elif selected_department == 'terminal' and selected_shift == 'terminalinventory':
            if selected_food_category == 'non_food':
                return redirect('inventory_terminal')
        else:
            # If no conditions are met, re-render the form with an error message
            return render(request, 'pizza_ordering/department_selection.html', {
                'error_message': 'Invalid selection. Please try again.'
            })

    # Render the form if the request method is not POST
    return render(request, 'pizza_ordering/department_selection.html')


def management_selection(request):
    if request.method == 'POST':
        selected_category = request.POST.get('category')
        # selected_store = request.POST.get('store')
        selected_department = request.POST.get('department')

        if selected_category == 'cleanliness_order':
            if selected_department == 'Kitchen':
                return redirect('cleanliness_order_kitchen')
            elif selected_department == 'Terminal':
                return redirect('cleanliness_order_terminal')
            elif selected_department == 'Storage/cellar/garage':
                return redirect('cleanliness_order_storage')
            elif selected_department == 'Apartment':
                return redirect('cleanliness_order_apartment')
            elif selected_department == 'E-Bikes':
                return redirect('ebikes_condition_view')
            elif selected_department == 'Special Cleaning':
                return redirect('special_cleaning')
        elif selected_category == 'review_checklists':
            if selected_department == 'Kitchen':
                return redirect('review_checklists_kitchen')
            elif selected_department == 'Terminal':
                return redirect('review_checklists_terminal')
            elif selected_department == 'Storage/cellar/garage':
                return redirect('review_checklists_storage')
            elif selected_department == 'Apartment':
                return redirect('review_checklists_apartment')

        # If none of the above conditions are met, show an error message
        return render(request, 'pizza_ordering/management_selection.html', {
            'error_message': 'Invalid selection. Please try again.'
        })

    # Render the form if the request method is not POST
    return render(request, 'pizza_ordering/management_selection.html')

def management_selection_success_view(request):
    return HttpResponse("Management selection form submitted successfully!")





def kitchen_lunch_form(request):
    if request.method == 'POST':
        KitchenLunch.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],

            today_balls_total=request.POST['today_balls_total'],
            # yesterday_balls_total=request.POST['yesterday_balls_total']
        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenlunch.html')
def kitchen_lunch_task(request):
    if request.method == 'POST':
        KitchenLunchTask.objects.create(
            date=request.POST['date'],
            name=request.POST['name'],
            location=request.POST['location'],

            task_kitchen_cleaned=request.POST['task_kitchen_cleaned'],
            task_enough_laundry=request.POST['task_enough_laundry'],
            comments=request.POST['comments'],

        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenlunchtask.html')

def kitchen_late_task(request):
    if request.method == 'POST':
        KitchenLateTask.objects.create(
            date=request.POST['date'],
            name=request.POST['name'],
            location=request.POST['location'],
            comments=request.POST['comments'],
            side=request.POST['side'],
            soap_WC_sufficient=request.POST['soap_WC_sufficient'],
            toilet_paper_WC_sufficient=request.POST['toilet_paper_WC_sufficient'],
            grease_remover_kitchen_sufficient=request.POST['grease_remover_kitchen_sufficient'],
            washingup_liquid_kitchen_sufficient=request.POST['washingup_liquid_kitchen_sufficient'],
            blue_roll_kitchen_sufficient=request.POST['blue_roll_kitchen_sufficient'],


        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenlatetask.html')

def kitchen_late_form(request):
    if request.method == 'POST':
        KitchenLate.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],

            pizza_grade=request.POST['pizza_grade'],
            tomorrow_balls_total=request.POST['tomorrow_balls_total'],
            old_balls_total=request.POST['old_balls_total'],
            old_balls_trash=request.POST['old_balls_trash'],
            balls_broken_today=request.POST['balls_broken_today'],
            pizzas_broken_today=request.POST['pizzas_broken_today']
        )
        return redirect(' ')
    return render(request, 'pizza_ordering/kitchenlate.html')
# from django.shortcuts import render, redirect
# from .models import KitchenLunch
def kitchen_specialcleaning_monday(request):
    if request.method == 'POST':
        KitchenSpecialcleaningMonday.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments']

        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenspecialcleaningmonday.html')


def terminal_lunch_form(request):
    if request.method == 'POST':
        TerminalLunch.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
            boden_gastraum_cleaned=request.POST['boden_gastraum_cleaned'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/terminallunch.html')
def terminal_late_form(request):
    if request.method == 'POST':
        TerminalLate.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],

            # cellar_tidy=request.POST['cellar_tidy'],
            # replenished=request.POST['replenished'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/terminallate.html')


def kitchen_late_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location=request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')


        pizza_grade = request.POST.get('pizza_grade')
        tomorrow_balls_total = request.POST.get('tomorrow_balls_total')
        old_balls_total = request.POST.get('old_balls_total')
        old_balls_trash = request.POST.get('old_balls_trash')
        balls_broken_today = request.POST.get('balls_broken_today')
        pizzas_broken_today = request.POST.get('pizzas_broken_today')
        # Create a new instance of KitchenLunch model and save the data
        KitchenLate.objects.create(
            date=date,
            location=location,
            name=name,
            comments=comments,

            pizza_grade=pizza_grade,
            tomorrow_balls_total=tomorrow_balls_total,
            old_balls_total=old_balls_total,
            old_balls_trash=old_balls_trash,
            balls_broken_today=balls_broken_today ,
            pizzas_broken_today=pizzas_broken_today

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_late_dashboard')
    else:
        # Handle GET requests if needed
        pass

def kitchen_specialcleaning_monday_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        KitchenSpecialcleaningMonday.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_specialcleaning_monday_dashboard')
    else:
        # Handle GET requests if needed
        pass
def terminal_lunch_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')
        boden_gastraum_cleaned=request.POST.get('boden_gastraum_cleaned')

        TerminalLunch.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,
            boden_gastraum_cleaned=boden_gastraum_cleaned,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('terminal_lunch_dashboard')
    else:
        # Handle GET requests if needed
        pass


def terminal_late_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # cellar_tidy=request.POST.get('cellar_tidy')
        # replenished=request.POST.get('replenished')

        TerminalLate.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

            # cellar_tidy=cellar_tidy,
            # replenished=replenished,
        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('terminal_late_dashboard')
    else:
        # Handle GET requests if needed
        pass
from django.shortcuts import render, redirect
from .models import KitchenLunch


def kitchen_lunch_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        today_balls_total = request.POST.get('today_balls_total')
        # yesterday_balls_total = request.POST.get('yesterday_balls_total')

        # Create a new instance of KitchenLunch model and save the data
        KitchenLunch.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

            today_balls_total=today_balls_total,
            # yesterday_balls_total=yesterday_balls_total
        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_lunch_dashboard')
    else:
        # Handle GET requests if needed
        pass
def kitchen_lunch_task_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')

        task_kitchen_cleaned=request.POST.get('task_kitchen_cleaned')
        task_enough_laundry=request.POST.get('task_enough_laundry')
        comments = request.POST.get('comments')



        # Create a new instance of KitchenLunch model and save the data
        KitchenLunchTask.objects.create(
            date=date,
            name=name,
            location=location,

            task_kitchen_cleaned=task_kitchen_cleaned,
            task_enough_laundry=task_enough_laundry,
            comments=comments,


        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_lunch_task_dashboard')
    else:
        # Handle GET requests if needed
        pass

def kitchen_late_task_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')
        side= request.POST.get('side')
        soap_WC_sufficient= request.POST.get('soap_WC_sufficient')
        toilet_paper_WC_sufficient=request.POST.get('toilet_paper_WC_sufficient')
        grease_remover_kitchen_sufficient=request.POST.get('grease_remover_kitchen_sufficient')
        washingup_liquid_kitchen_sufficient=request.POST.get('washingup_liquid_kitchen_sufficient')
        blue_roll_kitchen_sufficient=request.POST.get('blue_roll_kitchen_sufficient')


        # Create a new instance of KitchenLunch model and save the data
        KitchenLateTask.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,
            side=side,
            soap_WC_sufficient=soap_WC_sufficient,
            toilet_paper_WC_sufficient=toilet_paper_WC_sufficient,
            grease_remover_kitchen_sufficient=grease_remover_kitchen_sufficient,
            washingup_liquid_kitchen_sufficient=washingup_liquid_kitchen_sufficient,
            blue_roll_kitchen_sufficient=blue_roll_kitchen_sufficient


        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_late_task_dashboard')
    else:
        # Handle GET requests if needed
        pass
def kitchen_lunch_dashboard(request):
    kitchen_lunchs = KitchenLunch.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/kitchenlunchdashboard.html', {'kitchen_lunchs': kitchen_lunchs})
def kitchen_lunch_task_dashboard(request):
    kitchen_lunchs_task = KitchenLunchTask.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/kitchenlunchtaskdashboard.html', {'kitchen_lunchs_task': kitchen_lunchs_task})
from django.shortcuts import render
from .models import KitchenLunch

from django.shortcuts import render
from .models import KitchenLate

def kitchen_late_dashboard(request):
    kitchen_lates = KitchenLate.objects.all().order_by('-date')  # Fetch all KitchenLate objects from the database, ordered by date descending
    return render(request, 'pizza_ordering/kitchenlatedashboard.html', {'kitchen_lates': kitchen_lates})

def kitchen_late_task_dashboard(request):
    kitchen_lates_task = KitchenLateTask.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/kitchenlatetaskdashboard.html', {'kitchen_lates_task': kitchen_lates_task})

def terminal_lunch_dashboard(request):
    terminal_lunches = TerminalLunch.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/terminallunchdashboard.html', {'terminal_lunches': terminal_lunches})
def terminal_late_dashboard(request):
    terminal_lates = TerminalLate.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/terminallatedashboard.html', {'terminal_lates': terminal_lates})
def kitchen_specialcleaning_monday_dashboard(request):
    kitchen_specialcleanings_monday = KitchenSpecialcleaningMonday.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/kitchenspecialcleaningmondaydashboard.html', {'kitchen_specialcleanings_monday': kitchen_specialcleanings_monday})



def dry_storage_cleaning_form(request):
    if request.method == 'POST':
        DryStorageCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/drystoragecleaning.html')
def drystorage_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # Create a new instance of KitchenLunch model and save the data
        DryStorageCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('drystorage_cleaning_dashboard')
    else:
        # Handle GET requests if needed
        pass

def drystorage_cleaning_dashboard(request):
    dry_storage_cleanings_form = DryStorageCleaning.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/drystoragecleaningdashboard.html', {'dry_storage_cleanings_form': dry_storage_cleanings_form})

def wednesday_cleaning_kitchen(request):
    if request.method == 'POST':
        WednesdayCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/wednesdaycleaning.html')
def wednesday_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # Create a new instance of KitchenLunch model and save the data
        WednesdayCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('wednesday_cleaning_dashboard')
    else:
        # Handle GET requests if needed
        pass

def wednesday_cleaning_dashboard(request):
    wednesday_cleaning_kitchens = WednesdayCleaning.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/wednesdaycleaningdashboard.html', {'wednesday_cleaning_kitchens': wednesday_cleaning_kitchens})

def apartment_cleaning_form(request):
    if request.method == 'POST':
        ApartmentCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/apartmentcleaning.html')
def apartment_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # Create a new instance of KitchenLunch model and save the data
        ApartmentCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('apartment_cleaning_dashboard')
    else:
        # Handle GET requests if needed
        pass

def apartment_cleaning_dashboard(request):
    apartment_cleaning_forms = ApartmentCleaning.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/apartmentcleaningdashboard.html', {'apartment_cleaning_forms': apartment_cleaning_forms})


from .models import Store, WeeklyDoughAmount
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render

def select_store(request):
    stores = Store.objects.all()
    selected_store = None
    selected_date = None
    selected_store_latest_dough_amount = None

    if request.method == 'POST':
        store_name = request.POST.get('store')
        selected_date = request.POST.get('date')

        if store_name:
            selected_store = Store.objects.get(name=store_name)
            if selected_date:
                selected_date = timezone.datetime.strptime(selected_date, '%Y-%m-%d').date()
                selected_day = selected_date.strftime('%A')  # Get the day of the week (e.g., 'Monday', 'Tuesday', etc.)

                # Get the latest dough amount for the selected store and selected day
                latest_dough_amount = WeeklyDoughAmount.objects.filter(
                    store=selected_store,
                    day=selected_day
                ).order_by('-id').first()

                if latest_dough_amount:
                    selected_store_latest_dough_amount = latest_dough_amount.dough_amount

    return render(request, 'pizza_ordering/select_store.html', {
        'stores': stores,
        'selected_store': selected_store,
        'selected_date': selected_date,
        'selected_store_latest_dough_amount': selected_store_latest_dough_amount
    })



from django.shortcuts import render, redirect
from .models import CleanlinessOrderKitchen,CleanlinessOrderApartment,CleanlinessOrderStorage,CleanlinessOrderTerminal,ReviewChecklistsApartment,ReviewChecklistsTerminal,ReviewChecklistsStorage,ReviewChecklistsKitchen
# from .forms import CleanlinessOrderKitchenForm
import datetime

def cleanliness_order_kitchen(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        tiles = request.POST.get('tiles')
        tiles_comment = request.POST.get('tiles_comment')
        tiles_rating = request.POST.get('tiles_rating')  # Rating for tiles
        tiles_image = request.FILES.get('tiles_image')  # Image for tiles

        tables_downstairs = request.POST.get('tables_downstairs')
        tables_downstairs_comment = request.POST.get('tables_downstairs_comment')
        tables_downstairs_rating = request.POST.get('tables_downstairs_rating')  # Rating for tables downstairs
        tables_downstairs_image = request.FILES.get('tables_downstairs_image')  # Image for tables downstairs

        refrigerators_back = request.POST.get('refrigerators_back')
        refrigerators_back_comment = request.POST.get('refrigerators_back_comment')
        refrigerators_back_rating = request.POST.get('refrigerators_back_rating')  # Rating for refrigerators back
        refrigerators_back_image = request.FILES.get('refrigerators_back_image')  # Image for refrigerators back

        bottom_sink = request.POST.get('bottom_sink')
        bottom_sink_comment = request.POST.get('bottom_sink_comment')
        bottom_sink_rating = request.POST.get('bottom_sink_rating')  # Rating for bottom sink
        bottom_sink_image = request.FILES.get('bottom_sink_image')  # Image for bottom sink

        extractor_hood = request.POST.get('extractor_hood')
        extractor_hood_comment = request.POST.get('extractor_hood_comment')
        extractor_hood_rating = request.POST.get('extractor_hood_rating')  # Rating for extractor hood
        extractor_hood_image = request.FILES.get('extractor_hood_image')  # Image for extractor hood

        refrigerator = request.POST.get('refrigerator')
        refrigerator_comment = request.POST.get('refrigerator_comment')
        refrigerator_rating = request.POST.get('refrigerator_rating')  # Rating for refrigerator
        refrigerator_image = request.FILES.get('refrigerator_image')  # Image for refrigerator

        kav = request.POST.get('kav')
        kav_comment = request.POST.get('kav_comment')
        kav_rating = request.POST.get('kav_rating')  # Rating for KAV
        kav_image = request.FILES.get('kav_image')  # Image for KAV

        measures = request.POST.get('measures')

        location = request.POST.get('location')

        # Convert date to calendar week
        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]

        # Save form data to the database
        CleanlinessOrderKitchen.objects.create(
            calendar_week=calendar_week,
            name=name,
            tiles=tiles,
            tiles_comment=tiles_comment,
            tiles_rating=tiles_rating,  # Save tiles rating
            tiles_image=tiles_image,  # Save tiles image
            tables_downstairs=tables_downstairs,
            tables_downstairs_comment=tables_downstairs_comment,
            tables_downstairs_rating=tables_downstairs_rating,  # Save tables downstairs rating
            tables_downstairs_image=tables_downstairs_image,  # Save tables downstairs image
            refrigerators_back=refrigerators_back,
            refrigerators_back_comment=refrigerators_back_comment,
            refrigerators_back_rating=refrigerators_back_rating,  # Save refrigerators back rating
            refrigerators_back_image=refrigerators_back_image,  # Save refrigerators back image
            bottom_sink=bottom_sink,
            bottom_sink_comment=bottom_sink_comment,
            bottom_sink_rating=bottom_sink_rating,  # Save bottom sink rating
            bottom_sink_image=bottom_sink_image,  # Save bottom sink image
            extractor_hood=extractor_hood,
            extractor_hood_comment=extractor_hood_comment,
            extractor_hood_rating=extractor_hood_rating,  # Save extractor hood rating
            extractor_hood_image=extractor_hood_image,  # Save extractor hood image
            refrigerator=refrigerator,
            refrigerator_comment=refrigerator_comment,
            refrigerator_rating=refrigerator_rating,  # Save refrigerator rating
            refrigerator_image=refrigerator_image,  # Save refrigerator image
            kav=kav,
            kav_comment=kav_comment,
            kav_rating=kav_rating,  # Save KAV rating
            kav_image=kav_image,  # Save KAV image
            measures=measures,
            location=location
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/cleanliness_order_kitchen.html')

def cleanliness_order_terminal(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        floor = request.POST.get('floor')
        floor_comment = request.POST.get('floor_comment')
        floor_rating = request.POST.get('floor_rating')

        # Floor fields
        floor = request.POST.get('floor')
        floor_comment = request.POST.get('floor_comment')
        floor_rating = request.POST.get('floor_rating')
        floor_image = request.FILES.get('floor_image')

        # Tiles fields
        tiles = request.POST.get('tiles')
        tiles_comment = request.POST.get('tiles_comment')
        tiles_rating = request.POST.get('tiles_rating')
        tiles_image = request.FILES.get('tiles_image')

        # Refrigerator fields
        refrigerator = request.POST.get('refrigerator')
        refrigerator_comment = request.POST.get('refrigerator_comment')
        refrigerator_rating = request.POST.get('refrigerator_rating')
        refrigerator_image = request.FILES.get('refrigerator_image')

        # Counter fields
        counter = request.POST.get('counter')
        counter_comment = request.POST.get('counter_comment')
        counter_rating = request.POST.get('counter_rating')
        counter_image = request.FILES.get('counter_image')

        # Lamps fields
        lamps = request.POST.get('lamps')
        lamps_comment = request.POST.get('lamps_comment')
        lamps_rating = request.POST.get('lamps_rating')
        lamps_image = request.FILES.get('lamps_image')

        # Tables and Chairs fields
        tables_chairs = request.POST.get('tables_chairs')
        tables_chairs_comment = request.POST.get('tables_chairs_comment')
        tables_chairs_rating = request.POST.get('tables_chairs_rating')
        tables_chairs_image = request.FILES.get('tables_chairs_image')

        # Windows fields
        windows = request.POST.get('windows')
        windows_comment = request.POST.get('windows_comment')
        windows_rating = request.POST.get('windows_rating')
        windows_image = request.FILES.get('windows_image')

        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        CleanlinessOrderTerminal.objects.create(
            calendar_week=calendar_week,
            name=name,
            floor=floor,
            floor_comment=floor_comment,
            floor_rating=floor_rating,
            floor_image=floor_image,  # Save floor image
            tiles=tiles,
            tiles_comment=tiles_comment,
            tiles_rating=tiles_rating,
            tiles_image=tiles_image,  # Save tiles image
            refrigerator=refrigerator,
            refrigerator_comment=refrigerator_comment,
            refrigerator_rating=refrigerator_rating,
            refrigerator_image=refrigerator_image,  # Save refrigerator image
            counter=counter,
            counter_comment=counter_comment,
            counter_rating=counter_rating,
            counter_image=counter_image,  # Save counter image
            lamps=lamps,
            lamps_comment=lamps_comment,
            lamps_rating=lamps_rating,
            lamps_image=lamps_image,  # Save lamps image
            tables_chairs=tables_chairs,
            tables_chairs_comment=tables_chairs_comment,
            tables_chairs_rating=tables_chairs_rating,
            tables_chairs_image=tables_chairs_image,  # Save tables and chairs image
            windows=windows,
            windows_comment=windows_comment,
            windows_rating=windows_rating,
            windows_image=windows_image,  # Save windows image
            measures=measures,
            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/cleanliness_order_terminal.html')

def cleanliness_order_storage(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        floor = request.POST.get('floor')
        garbage = request.POST.get('garbage')
        tidiness = request.POST.get('tidiness')
        inventory = request.POST.get('inventory')
        floor_comment = request.POST.get('floor_comment')
        garbage_comment = request.POST.get('garbage_comment')
        tidiness_comment = request.POST.get('tidiness_comment')
        inventory_comment = request.POST.get('inventory_comment')
        floor_rating = request.POST.get('floor_rating')  # Retrieve floor rating
        garbage_rating = request.POST.get('garbage_rating')  # Retrieve garbage rating
        tidiness_rating = request.POST.get('tidiness_rating')  # Retrieve tidiness rating
        inventory_rating = request.POST.get('inventory_rating')  # Retrieve inventory rating
        floor_image = request.FILES.get('floor_image')  # Get uploaded image for floor
        garbage_image = request.FILES.get('garbage_image')  # Get uploaded image for garbage
        tidiness_image = request.FILES.get('tidiness_image')  # Get uploaded image for tidiness
        inventory_image = request.FILES.get('inventory_image')  # Get uploaded image for inventory

        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field
        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        CleanlinessOrderStorage.objects.create(
            calendar_week=calendar_week,
            name=name,
            floor=floor,
            garbage=garbage,
            tidiness=tidiness,
            inventory=inventory,
            floor_comment=floor_comment,  # Save comment for floor
            garbage_comment=garbage_comment,  # Save comment for garbage
            tidiness_comment=tidiness_comment,  # Save comment for tidiness
            inventory_comment=inventory_comment,  # Save comment for inventory
            floor_rating=floor_rating,  # Save floor rating
            garbage_rating=garbage_rating,  # Save garbage rating
            tidiness_rating=tidiness_rating,  # Save tidiness rating
            inventory_rating=inventory_rating,  # Save inventory rating
            floor_image=floor_image,  # Save uploaded image for floor
            garbage_image=garbage_image,  # Save uploaded image for garbage
            tidiness_image=tidiness_image,  # Save uploaded image for tidiness
            inventory_image=inventory_image,  # Save uploaded image for inventory
            measures=measures,

            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/cleanliness_order_storage.html')

def cleanliness_order_apartment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        floor = request.POST.get('floor')
        shelf = request.POST.get('shelf')
        garbage = request.POST.get('garbage')
        cold_room = request.POST.get('cold_room')
        washroom_kitchen = request.POST.get('washroom_kitchen')
        wc = request.POST.get('wc')
        floor_comment = request.POST.get('floor_comment')
        shelf_comment = request.POST.get('shelf_comment')
        garbage_comment = request.POST.get('garbage_comment')
        cold_room_comment = request.POST.get('cold_room_comment')
        washroom_kitchen_comment = request.POST.get('washroom_kitchen_comment')
        wc_comment = request.POST.get('wc_comment')

        floor_rate = request.POST.get('floor_rate')
        shelf_rate = request.POST.get('shelf_rate')
        garbage_rate = request.POST.get('garbage_rate')
        cold_room_rate = request.POST.get('cold_room_rate')
        washroom_kitchen_rate = request.POST.get('washroom_kitchen_rate')
        wc_rate = request.POST.get('wc_rate')
        floor_image = request.FILES.get('floor_image')
        shelf_image = request.FILES.get('shelf_image')
        garbage_image = request.FILES.get('garbage_image')
        cold_room_image = request.FILES.get('cold_room_image')
        washroom_kitchen_image = request.FILES.get('washroom_kitchen_image')
        wc_image = request.FILES.get('wc_image')

        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        CleanlinessOrderApartment.objects.create(
            calendar_week=calendar_week,
            name=name,
            floor=floor,
            shelf=shelf,
            garbage=garbage,
            cold_room=cold_room,
            washroom_kitchen=washroom_kitchen,
            wc=wc,
            floor_comment=floor_comment,  # Save comment for floor
            shelf_comment=shelf_comment,  # Save comment for shelf
            garbage_comment=garbage_comment,  # Save comment for garbage
            cold_room_comment=cold_room_comment,  # Save comment for cold room
            washroom_kitchen_comment=washroom_kitchen_comment,  # Save comment for washroom/kitchen
            wc_comment=wc_comment , # Save comment for WC

            floor_rate=floor_rate,  # Save rating for floor
            shelf_rate=shelf_rate,  # Save rating for shelf
            garbage_rate=garbage_rate,  # Save rating for garbage
            cold_room_rate=cold_room_rate,  # Save rating for cold room
            washroom_kitchen_rate=washroom_kitchen_rate,  # Save rating for washroom/kitchen
            wc_rate=wc_rate,
            floor_image=floor_image,  # Save image for floor
            shelf_image=shelf_image,  # Save image for shelf
            garbage_image=garbage_image,  # Save image for garbage
            cold_room_image=cold_room_image,  # Save image for cold room
            washroom_kitchen_image=washroom_kitchen_image,  # Save image for washroom/kitchen
            wc_image=wc_image,

            measures=measures,
            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/cleanliness_order_apartment.html')

from datetime import datetime
def review_checklists_kitchen(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        fulfillment_rate = request.POST.get('fulfillment_rate')
        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        ReviewChecklistsKitchen.objects.create(
            calendar_week=calendar_week,
            name=name,
            fulfillment_rate=fulfillment_rate,
            measures=measures,
            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/review_checklists_kitchen.html')

def review_checklists_terminal(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        calendar_week = request.POST.get('calendar_week')
        fulfillment_rate = request.POST.get('fulfillment_rate')
        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        ReviewChecklistsTerminal.objects.create(
            calendar_week=calendar_week,
            name=name,
            fulfillment_rate=fulfillment_rate,
            measures=measures,
            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/review_checklists_terminal.html')

def review_checklists_storage(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        fulfillment_rate = request.POST.get('fulfillment_rate')
        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        ReviewChecklistsStorage.objects.create(
            calendar_week=calendar_week,
            name=name,
            fulfillment_rate=fulfillment_rate,
            measures=measures,
            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/review_checklists_storage.html')

def review_checklists_apartment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        calendar_week = request.POST.get('calendar_week')
        name = request.POST.get('name')
        fulfillment_rate = request.POST.get('fulfillment_rate')
        measures = request.POST.get('measures')
        location = request.POST.get('location')  # New field

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            calendar_week = date_obj.isocalendar()[1]


        # Save form data to the database
        ReviewChecklistsApartment.objects.create(
            calendar_week=calendar_week,
            name=name,
            fulfillment_rate=fulfillment_rate,
            measures=measures,
            location=location  # Save new field
        )

        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/review_checklists_apartment.html')


from django.http import HttpResponse
def management_selection_success(request):
    return render(request, 'pizza_ordering/success.html')

# views.py
from django.shortcuts import render
from .models import (
    CleanlinessOrderKitchen,
    CleanlinessOrderTerminal,
    CleanlinessOrderStorage,
    CleanlinessOrderApartment,
    ReviewChecklistsKitchen,
    ReviewChecklistsTerminal,
    ReviewChecklistsStorage,
    ReviewChecklistsApartment,
)

def get_latest_entries(queryset):
    latest_entries = {}
    for entry in queryset:
        location = entry.location
        if location not in latest_entries or entry.created_at > latest_entries[location].created_at:
            latest_entries[location] = entry
    return latest_entries.values()

def admin_view(request):
    cleanliness_order_kitchen = get_latest_entries(CleanlinessOrderKitchen.objects.all())
    cleanliness_order_terminal = get_latest_entries(CleanlinessOrderTerminal.objects.all())
    cleanliness_order_storage = get_latest_entries(CleanlinessOrderStorage.objects.all())
    cleanliness_order_apartment = get_latest_entries(CleanlinessOrderApartment.objects.all())
    review_checklists_kitchen = get_latest_entries(ReviewChecklistsKitchen.objects.all())
    review_checklists_terminal = get_latest_entries(ReviewChecklistsTerminal.objects.all())
    review_checklists_storage = get_latest_entries(ReviewChecklistsStorage.objects.all())
    review_checklists_apartment = get_latest_entries(ReviewChecklistsApartment.objects.all())

    ebike_condition_view = get_latest_entries(EBikeCondition.objects.all())
    special_cleaning=get_latest_entries(Sonderreinigung.objects.all())

    context = {
        'cleanliness_order_kitchen': cleanliness_order_kitchen,
        'cleanliness_order_terminal': cleanliness_order_terminal,
        'cleanliness_order_storage': cleanliness_order_storage,
        'cleanliness_order_apartment': cleanliness_order_apartment,
        'review_checklists_kitchen': review_checklists_kitchen,
        'review_checklists_terminal': review_checklists_terminal,
        'review_checklists_storage': review_checklists_storage,
        'review_checklists_apartment': review_checklists_apartment,

        'ebike_condition_view':ebike_condition_view,
        'special_cleaning':special_cleaning,
    }

    return render(request, 'email_template.html', context)



from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import BestBeforeDateCheck

def best_before_date_check(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        date = request.POST.get('date')
        cured_meats_checked = request.POST.get('cured_meats_checked') == 'on'
        cheese_checked = request.POST.get('cheese_checked') == 'on'
        vegan_cheese_checked = request.POST.get('vegan_cheese_checked') == 'on'
        latest_best_before_date = request.POST.get('latest_best_before_date')
        expired = request.POST.get('expired')



        # Save the data to the database
        BestBeforeDateCheck.objects.create(
            location=location,
            date=date,
            cured_meats_checked=cured_meats_checked,
            cheese_checked=cheese_checked,
            vegan_cheese_checked=vegan_cheese_checked,
            latest_best_before_date=latest_best_before_date,
            expired=expired
        )

        # Redirect to the corresponding HTML page if "Best Before Date" option was selected
        if request.POST.get('best_before_date_option') == 'true':  # Adjust this condition based on your logic
            return redirect(reverse('best_before_date_page'))  # Replace with your actual HTML page URL name

        # Redirect to a success page or back to the form with a success message
        return redirect(reverse('best_before_date_success'))

    return render(request, 'pizza_ordering/best_before_date_form.html')


def best_before_date_success(request):
    return render(request, 'pizza_ordering/successbest.html')


def terminal_saturday_cleaning_dashboard(request):
    terminal_saturday_cleanings = TerminalSaturdayCleaning.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/terminal_saturday_cleaning_dashboard.html', {'terminal_saturday_cleanings': terminal_saturday_cleanings})


from django.shortcuts import render, redirect
from .models import TerminalSaturdayCleaning

def terminal_saturday_cleaning_form(request):
    if request.method == 'POST':
        TerminalSaturdayCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments']
        )
        # Redirect to a specific page after successful submission
        return redirect('terminal_saturday_cleaning_dashboard')  # Assuming this is the URL name for the dashboard
    return render(request, 'pizza_ordering/terminal_saturday_cleaning.html')

def terminal_saturday_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        TerminalSaturdayCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,
        )

        # Redirect to the dashboard page after form submission
        return redirect('terminal_saturday_cleaning_dashboard')
    else:
        # Optionally handle GET requests if required
        return render(request, 'pizza_ordering/terminal_saturday_cleaning.html')

from django.shortcuts import render, redirect
from .models import KitchenInventory  # Assuming this model is defined
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# View to handle the kitchen inventory form submission
def inventory_kitchen(request):
    if request.method == 'POST':
        # Collecting data from POST request for each inventory item
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments=request.POST.get('comments')

        # Matching form field names with the model fields
        einwegpapier_zickzack = request.POST.get('einwegpapier_zickzack')
        einweghandschuhe_m = request.POST.get('einweghandschuhe_m')
        einweghandschuhe_l = request.POST.get('einweghandschuhe_l')
        blaue_rolle_papierwischtuch = request.POST.get('blaue_rolle_papierwischtuch')
        fettloeser_packzu = request.POST.get('fettloeser_packzu')
        spuelmittel_packzu = request.POST.get('spuelmittel_packzu')
        handseife = request.POST.get('handseife')
        toilettenpapier = request.POST.get('toilettenpapier')
        waschpulver = request.POST.get('waschpulver')
        reiniger_spuelmaschine = request.POST.get('reiniger_spuelmaschine')
        muellsack_gross = request.POST.get('muellsack_gross')
        muellsack_klein = request.POST.get('muellsack_klein')
        bodenreiniger = request.POST.get('bodenreiniger')

        # Creating a new instance of KitchenInventory and saving form data
        KitchenInventory.objects.create(
            date=date,
            location=location,
            name=name,
            comments=comments,
            einwegpapier_zickzack=einwegpapier_zickzack,
            einweghandschuhe_m=einweghandschuhe_m,
            einweghandschuhe_l=einweghandschuhe_l,
            blaue_rolle_papierwischtuch=blaue_rolle_papierwischtuch,
            fettloeser_packzu=fettloeser_packzu,
            spuelmittel_packzu=spuelmittel_packzu,
            handseife=handseife,
            toilettenpapier=toilettenpapier,
            waschpulver=waschpulver,
            reiniger_spuelmaschine=reiniger_spuelmaschine,
            muellsack_gross=muellsack_gross,
            muellsack_klein=muellsack_klein,
            bodenreiniger=bodenreiniger,
        )

        subject = 'Kitchen Inventory Update Notification'
        message = f"""
            Dear Team,

                We would like to inform you that the following inventory has been submitted:
                Date: {date}
                Location: {location}
                Submitted by: {name}

                    Best regards,
                    Forzacheck
            """
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['forzanapoli.de@gmail.com']   # Replace with the actual recipient email(s)

        try:
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Inventory data submitted successfully and notification email sent.")
        except Exception as e:
            messages.error(request, f"Data submitted, but an error occurred while sending email: {str(e)}")


        # Redirecting after form submission
        return redirect('success_best')  # Replace with the appropriate dashboard URL
    else:
        # Render the form page if the request method is GET
        return render(request, 'pizza_ordering/inventorykitchen.html')  # Replace with your template name

def success_best(request):
    return render(request, 'pizza_ordering/successbest.html')


from django.shortcuts import render, redirect
from .models import TerminalInventory  # Assuming this model is defined
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings



# View to handle the terminal inventory form submission
def inventory_terminal(request):
    if request.method == 'POST':
        # Collecting data from POST request for each inventory item
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments=request.POST.get('comments')

        # PERGANO Section
        pizzakarton = request.POST.get('pizzakarton')
        pizzapapier = request.POST.get('pizzapapier')
        salatschale = request.POST.get('salatschale')
        salatschale_deckel = request.POST.get('salatschale_deckel')
        dressingschale = request.POST.get('dressingschale')
        dressingschale_deckel = request.POST.get('dressingschale_deckel')
        serviette_gast = request.POST.get('serviette_gast')
        dip_becher=request.POST.get('dip_becher')
        dip_deckel=request.POST.get('dip_deckel')

        # AMAZON Section
        bonrollen = request.POST.get('bonrollen')
        kugelschreiber = request.POST.get('kugelschreiber')
        textmarker_gelb = request.POST.get('textmarker_gelb')
        filzstift_schwarz = request.POST.get('filzstift_schwarz')
        kellnerblock = request.POST.get('kellnerblock')
        tesa_rollen = request.POST.get('tesa_rollen')
        etiketten_tiramisu = request.POST.get('etiketten_tiramisu')
        etiketten_gn = request.POST.get('etiketten_gn')
        aufkleber_rot = request.POST.get('aufkleber_rot')
        einwegloeffel = request.POST.get('einwegloeffel')
        einweggabel = request.POST.get('einweggabel')
        desinfektionsmittel = request.POST.get('desinfektionsmittel')
        salz_spuelmaschine = request.POST.get('salz_spuelmaschine')
        trueffel_mayo = request.POST.get('trueffel_mayo')
        dip_tuete = request.POST.get('dip_tuete')
        zwiebel_chutney = request.POST.get('zwiebel_chutney')
        # kuerbiskerne = request.POST.get('kuerbiskerne')
        pflaster = request.POST.get('pflaster')
        blaue_rolle= request.POST.get('blaue_rolle')

        # FLYER Section
        speisekarte_blau = request.POST.get('speisekarte_blau')
        menu_gelb = request.POST.get('menu_gelb')

        tomatendose_pumarole_dolce = request.POST.get('tomatendose_pumarole_dolce')
        tomatendose_san_marzano_dop = request.POST.get('tomatendose_san_marzano_dop')


        # Creating a new instance of Inventory and saving the form data
        TerminalInventory.objects.create(
            date=date,
            location=location,
            name=name,
            comments=comments,
            pizzakarton=pizzakarton,
            pizzapapier=pizzapapier,
            salatschale=salatschale,
            salatschale_deckel=salatschale_deckel,
            dressingschale=dressingschale,
            dressingschale_deckel=dressingschale_deckel,
            serviette_gast=serviette_gast,
            dip_becher=dip_becher,
            dip_deckel=dip_deckel,
            bonrollen=bonrollen,
            kugelschreiber=kugelschreiber,
            textmarker_gelb=textmarker_gelb,
            filzstift_schwarz=filzstift_schwarz,
            kellnerblock=kellnerblock,
            tesa_rollen=tesa_rollen,
            etiketten_tiramisu=etiketten_tiramisu,
            etiketten_gn=etiketten_gn,
            aufkleber_rot=aufkleber_rot,
            einwegloeffel=einwegloeffel,
            einweggabel=einweggabel,
            desinfektionsmittel=desinfektionsmittel,
            salz_spuelmaschine=salz_spuelmaschine,
            trueffel_mayo=trueffel_mayo,
            dip_tuete=dip_tuete,
            zwiebel_chutney=zwiebel_chutney,
            # kuerbiskerne=kuerbiskerne,
            pflaster=pflaster,
            blaue_rolle=blaue_rolle,
            speisekarte_blau=speisekarte_blau,
            menu_gelb=menu_gelb,
            tomatendose_pumarole_dolce=tomatendose_pumarole_dolce,
            tomatendose_san_marzano_dop=tomatendose_san_marzano_dop,
        )

        subject = 'Terminal Inventory Update Notification'
        message = f"""
            Dear Team,

                We would like to inform you that the following inventory has been submitted:
                Date: {date}
                Location: {location}
                Submitted by: {name}

                    Best regards,
                    Forzacheck
            """
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['forzanapoli.de@gmail.com']  # Replace with the actual recipient email(s)

        try:
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Inventory data submitted successfully and notification email sent.")
        except Exception as e:
            messages.error(request, f"Data submitted, but an error occurred while sending email: {str(e)}")



        # Redirecting after form submission
        return redirect('success_best')  # Replace with the appropriate dashboard URL
    else:
        # Render the form page if the request method is GET
        return render(request, 'pizza_ordering/inventoryterminal.html')  # Replace with your template name

from .models import DoughroomCleaning
def doughroom_cleaning(request):
    if request.method == 'POST':
        DoughroomCleaning.objects.create(
            date=request.POST['date'],

            name=request.POST['name'],
            comments=request.POST['comments']
        )
        # Redirect to a specific page after successful submission
        return redirect('success_best')  # Assuming this is the URL name for the dashboard
    return render(request, 'pizza_ordering/doughroom_cleaning.html')

def doughroom_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')

        name = request.POST.get('name')
        comments = request.POST.get('comments')

        DoughroomCleaning.objects.create(
            date=date,
            name=name,

            comments=comments,
        )

        # Redirect to the dashboard page after form submission
        return redirect('success_best')
    else:
        # Optionally handle GET requests if required
        return render(request, 'pizza_ordering/doughroom_cleaning.html')

from django.utils import timezone
from .models import EBikeCondition
from datetime import datetime

# Helper function to calculate the calendar week
def get_calendar_week(date):
    return date.strftime('%U')  # %U returns the week number (Sunday as the first day of the week)

def ebikes_condition_view(request):
    if request.method == 'POST':
        # Get form data
        selected_date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        bike_condition = request.POST.get('bike_condition')
        bike_rate = request.POST.get('bike_rate')  # Rating for tiles
        bike_image = request.FILES.get('bike_image')  # Image for tiles


        if selected_date:
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            calendar_week = get_calendar_week(date)
        else:
            date = timezone.now().date()
            calendar_week = get_calendar_week(date)

        # Create and save the EBikeCondition entry
        EBikeCondition.objects.create(
            date=date,
            calendar_week=calendar_week,
            location=location,
            name=name,
            bike_condition=bike_condition,
            bike_rate=bike_rate,
            bike_image=bike_image,
        )

        # Redirect to a success page or the same form
        return redirect('management_selection_success')  # or another appropriate view

    return render(request, 'pizza_ordering/ebikes.html')

from django.shortcuts import render, redirect
from .models import Sonderreinigung
from django.utils import timezone

def special_cleaning(request):
    if request.method == 'POST':
        # Collecting data from POST request
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        ventilation = request.POST.get('ventilation')
        ventilation_rate = request.POST.get('ventilation_rate')
        ventilation_image = request.FILES.get('ventilation_image')
        spiderwebs = request.POST.get('spiderwebs')
        spiderwebs_rate = request.POST.get('spiderwebs_rate')
        spiderwebs_image = request.FILES.get('spiderwebs_image')
        washer = request.POST.get('washer')
        washer_rate = request.POST.get('washer_rate')
        washer_image = request.FILES.get('washer_image')
        comments = request.POST.get('comments')

        # Creating a new instance of SpecialCleaning and saving form data
        Sonderreinigung.objects.create(
            date=date,
            location=location,
            name=name,
            ventilation=ventilation,
            ventilation_rate=ventilation_rate,
            ventilation_image=ventilation_image,
            spiderwebs=spiderwebs,
            spiderwebs_rate=spiderwebs_rate,
            spiderwebs_image=spiderwebs_image,
            washer=washer,
            washer_rate=washer_rate,
            washer_image=washer_image,
            comments=comments,
        )

        # Redirect to a success page or back to the form after submission
        return redirect('success_best')  # Assuming you have a success URL

    return render(request, 'pizza_ordering/SONDERREINIGUNG.html')

