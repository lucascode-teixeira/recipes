from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    template_name = 'index.html'

    name = 'David'

    return TemplateResponse(request, template_name, locals())
