from django.shortcuts import render ,redirect

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, ' Account created for username '+ str(username))
            return redirect('post_list')
        # else:
            # return render(request, 'users/register.html',{'form': form})
    else:
        form = UserRegisterForm()
        return render(request ,'users/register.html' , {'form':form})
# Create your views here.

