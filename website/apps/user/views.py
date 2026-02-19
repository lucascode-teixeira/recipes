from django.template.response import TemplateResponse


# Create your views here.
def login(request):
    template_name = 'user/login.html'

    return TemplateResponse(request, template_name, locals())