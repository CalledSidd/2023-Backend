from django.shortcuts import render,redirect
from django.views import View


from . forms import LoginForm, CreateUserForm

# Create your views here.

class IndexView(View):
    pass

class LoginView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        context = {
            'form' : form,
            'message': message
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                )
            if user is not None:
                login(request, user)
                return redirect('index')
            message = 'Invalid Credentials'

            context = {
            'form' : form,
            'message': message
            }
            return render(request, self.template_name, context)


class SignupView(View):
    template = 'authentication/signup.html'
    form_class = CreateUserForm
    def get(self, request):
        form = self.form_class
        context = {
            'form' : form
        }
        return render(request, self.template, context)
