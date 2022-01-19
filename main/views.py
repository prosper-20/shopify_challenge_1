from itertools import product
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product, Order
from .forms import OrderForm, ProductForm
from django.contrib.auth.models import User


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'main/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'quantity', 'category', 'seller']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'quantity', 'category', 'seller']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def new_index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            
            return redirect("new")
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }

    return render(request, "main/.index.html", context)