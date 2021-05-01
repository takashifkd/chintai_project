from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm


def index(request):
    return render(request, "index.html")


def inquiry_form(request):
    form = InquiryForm
    return render(request, "inquiry.html", {
        'form': form
    })


"""
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
"""
