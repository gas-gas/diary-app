from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateFrom
from .models import Day

class IndexView(generic.ListView):
    model = Day
    paginate_by = 2

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateFrom
    # 文字列のURLを返却
    success_url = reverse_lazy('diary:index') # http://127.0.0.1:8000/diary/

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateFrom
    success_url = reverse_lazy('diary:index') # http://127.0.0.1:8000/diary/

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index') # http://127.0.0.1:8000/diary/

class DetailView(generic.DetailView):
    model = Day

