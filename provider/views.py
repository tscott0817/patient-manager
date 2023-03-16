from django.shortcuts import render, redirect, get_object_or_404
# from .models import Provider
# from .forms import ProviderForm

# Create your views here.

# def home(request):
#     queryset = Provider.objects.all().order_by('name')
#     context = {
#         'queryset': queryset
#     }
#     return render(request, 'app/base.html', context)
#
#
# def create(request):
#     form = ProviderForm(request.POST or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect ('home')
#     context = {
#         "form":form
#     }
#     return render(request, 'app/createform.html', context)
