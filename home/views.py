from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

<<<<<<< HEAD
#def detail(request, title, year,  year, month, day):
#    project = get_object_or_404(Project, title=title, date__year=year, date__month=month, date__day=day)
#    return render(request, "detail.html", {"project":project})

=======
>>>>>>> 5b0ec2f14d578abcdb46f8bec82403243ca7a263
def detail(request, title, year, month, day):
    project = get_object_or_404(Project, title=title, date__year=year, date__month=month, date__day=day)
    return render(request, "detail.html", {"project":project})
def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")
