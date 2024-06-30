from django.shortcuts import render


def about(request):
<<<<<<< HEAD
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')
=======
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
>>>>>>> 6f61790 (index)
