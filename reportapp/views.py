from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Activity




def index(request):
    return render(request, 'index.html')  



def activity(request):
    if request.method == "POST":
        # Check if the action is 'delete'
        if request.POST.get('action') == 'delete':
            activity_id = request.POST.get('activity_id')
            if activity_id:
                try:
                    activity_to_delete = Activity.objects.get(id=activity_id)
                    activity_to_delete.delete()  # Delete the activity from the database
                except Activity.DoesNotExist:
                    pass  # Handle the case where the activity doesn't exist
        else:
            # Handle form submission for adding an activity
            date = request.POST.get('date')
            client = request.POST.get('client')
            activity = request.POST.get('activity')
            status = request.POST.get('status')

            # Save the data to the database if all fields are present
            if date and client and activity and status:
                new_activity = Activity(date=date, client=client, activity=activity, status=status)
                new_activity.save()

        # Redirect to the same page to show the updated list
        return redirect('activity')

    # Fetch all activity entries from the database to display
    activities = Activity.objects.all()
    return render(request, 'activity.html', {'activities': activities})




def Portfolio(request):
    return render(request, 'Portfolio.html')  