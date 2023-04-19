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
def detail(request, title, year, month, day):
    project = get_object_or_404(Project, title=title, date__year=year, date__month=month, date__day=day)
    return render(request, "detail.html", {"project":project})
>>>>>>> 3ca69f6e44e5e6d3246cfd70921715694b38d464
def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")
