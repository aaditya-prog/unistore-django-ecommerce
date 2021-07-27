from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Help form"
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['artdityadulal@gmail.com'])
            except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            return redirect ("home:index")
    form = ContactForm()
    return render(request, "contacts/index.html", {"form":form})