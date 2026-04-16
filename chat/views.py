from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message


@login_required
def chat_view(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages})


@login_required
def send_message(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        image = request.FILES.get('image')

        if not text and not image:
            return JsonResponse({'error': 'Empty message'})

        message = Message.objects.create(
            sender=request.user,
            text=text,
            image=image
        )

        return JsonResponse({
            'sender': message.sender.username,
            'text': message.text,
            'image': message.image.url if message.image else None,
            'timestamp': message.timestamp.strftime('%H:%M')
        })

    return JsonResponse({'error': 'Invalid request'})