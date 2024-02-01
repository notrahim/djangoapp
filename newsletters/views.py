# views.py

from django.http import JsonResponse
from .forms import SubscriberForm
from .models import Subscriber

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            _, created = Subscriber.objects.get_or_create(email=email)
            if created:
                # If a new subscriber was created
                return JsonResponse({'message': 'Thank you for subscribing!'}, status=200)
            else:
                # If the subscriber already exists
                return JsonResponse({'message': 'You are already subscribed.'}, status=200)
        else:
            # Form is not valid
            return JsonResponse({'message': 'Please enter a valid email address.'}, status=400)
    else:
        # Not a POST request
        return JsonResponse({'message': 'Invalid request'}, status=400)
