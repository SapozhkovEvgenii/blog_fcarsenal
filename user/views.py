from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from user.forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


class RegisterUser(FormView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_page')

    
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home_page')


def logout_user(request):
    logout(request)
    return redirect("login_user")