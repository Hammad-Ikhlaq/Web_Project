from django.shortcuts import render

AllProducts = [
    {
        'name': 'Milk',
        'price': '110 per litre',
        'quantity': '500',
    },
    {
        'name': 'Butter',
        'price': '800 per kg',
        'quantity': '200',
    }
]

AllBranches = [
    {
        'city': 'Okara',
        'supervisor': 'Majid Bhatti',
        'area': '6 kanal',
        'contactNumber': '033333467',
        'address': 'Neelam Road 32 Okara',
        'since': '1992'
    },
    {
        'city': 'Lahore',
        'supervisor':'Hammad Ikhlaq',
        'area': '4 kanal',
        'contactNumber': '0302403012',
        'address': '136/1 M DHA Lahore Cantt',
        'since': '1999'
    }
]


def home(request):
    return render(request, 'homepage/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})

def careers(request):
    return render(request, 'homepage/careers.html', {'title': 'Careers'})

def branches(request):
    context = {
        'branches': AllBranches,
        'title': 'Branches'
    }
    return render(request, 'homepage/branches.html', context)

def products(request):
    context = {
        'products': AllProducts,
        'title': 'Our Products'
    }
    return render(request, 'homepage/products.html', context)

def feedback(request):
    return render(request, 'homepage/feedback.html', {'title': 'Feedback'})