from django.shortcuts import render, redirect

def headerpartial(request, *args, **kwargs):
    context={
        "test": "ورود"
    }

    return render(request, 'shared/header.html', context)
def footerpartial(request, *args, **kwargs):
    context = {

    }

    return render(request, 'shared/footer.html', context)

def homepage (request):

    return render(request, "homepage.html", {})

def aboutus(request):

    context = {}

    return render(request, "aboutus.html", context)
