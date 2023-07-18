from django.shortcuts import render, redirect

from .forms import ContactUsForm


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

            # Redirect to a success page or show a pop-up message here
    else:
        form = ContactUsForm()
    return render(request, 'contact-us.html', {'form': form})


def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')
