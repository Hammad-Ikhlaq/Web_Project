from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Cart, Products

AllProducts = [
    {
        'name': 'Milk 1 kg',
        'price': 95,
        'image_url': '/media/p1.jpg',
    },
    {
        'name': 'Yogurt 1 kg',
        'price': 95,
        'image_url': '/media/p2.jpg',
    },
    {
        'name': 'Butter 1 kg',
        'price': 111,
        'image_url': '/media/p3.jpg',
    },
    {
        'name': 'Cream 1 kg',
        'price': 95,
        'image_url': '/media/p4.jpg',
    },
    {
        'name': 'Cheese 1 kg',
        'price': 95,
        'image_url': '/media/p5.jpg',
    },
    {
        'name': 'Barfi 1 kg',
        'price': 95,
        'image_url': '/media/p6.jpg',
    },
    {
        'name': 'Ice Cream 1 kg',
        'price': 111,
        'image_url': '/media/p7.jpg',
    },
    {
        'name': 'Ghee 1 kg',
        'price': 105,
        'image_url': '/media/p8.jpg',
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

@login_required
def cart(request):
    cart_obj, new_obj=Cart.objects.new_or_get(request)
    products=cart_obj.products.all()
    total=0
    for x in products:
        total=x.price
    print(total)
    cart_obj.total=total
    cart_obj.save()
    return render(request, 'homepage/cart.html')

@login_required
def products(request):
    context = {
        'products': AllProducts,
        'title': 'Our Products'
    }
    return render(request, 'homepage/products.html', context)

@login_required
def feedback(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Feedback'
    }
    return render(request, 'homepage/feedback.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'homepage/feedback.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/feedback/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False