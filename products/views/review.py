from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from products.forms import ReviewForm
from products.models import Review, Product


class ReviewListView(ListView):
    template_name = 'product_view.html'
    model = Review
    context_object_name = 'reviews'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'reviews/product_review_add.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        self.object: Review = form.save(commit=False)
        product_pk = self.kwargs.get('pk')
        self.object.product = get_object_or_404(Product, pk=product_pk)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ReviewUpdateView(UpdateView):
    template_name = 'reviews/review_update.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'reviews'

    def get_success_url(self):
        return reverse('index')


class ReviewDeleteView(DeleteView):
    template_name = 'product_view.html'
    context_object_name = 'review'
    model = Review
    success_url = reverse_lazy('index')
