from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Information, Work, Cv

class IndexView(ListView):
    model = Work
    template_name = 'core/index.html'
    queryset = Work.objects.filter(is_public=True).order_by('-production_year')[:4]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['information_list'] = Information.objects.filter(is_public=True).order_by('-published_at')[:4]
        return context

class WorksView(ListView):
    model = Work
    template_name = 'core/works_list.html'
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True).order_by('-published_at')

class WorkDetailView(DetailView):
    model = Work

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public:
            raise Http404
        return obj

class InformationIndexView(ListView):
    model = Information
    template_name = 'core/information_list.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True).order_by('-published_at')


class CvView(ListView):
    model = Cv
    template_name = "core/cv.html"

    def get_queryset(self):
        qs = super().get_queryset().filter(is_public=True).order_by('start_at')
        order = ['グループ展', '個展',
                 '本', 'アプリ', '受賞歴など']
        return sorted(qs, key=lambda x: order.index(x.genre))

class StatementView():
    def index(request):
        return render(request, 'core/statement.html')

class ContactFormView(FormView):
    template_name = 'core/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'core/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context
