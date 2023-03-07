from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, CompanyInfo, AcademicsInfo
from django.contrib.auth.decorators import login_required
from .forms import StepZeroForm, StepOneForm, StepTwoForm, StepThreeForm, EditUserProfile
from django.contrib import messages


def profileView(request, pk):

    user = User.objects.get(email = pk)
    academics = AcademicsInfo.objects.get(user = user)
    company = CompanyInfo.objects.get(user = user)

    context = { 'user' : user, 'academics' : academics, 'company' : company }
    return render(request, "user/profile.html", context)
    

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('feeds:index')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.object.get(email = email)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, email = email, password = password)


        if user is not None:
            login(request, user)
            return redirect('feeds:index')

        else:
            messages.error(request, 'Username or password is incorrect!!!')

    return render(request, 'user/login.html',{})

def logoutPage(request):
    logout(request)
    return redirect('user:login')

def signupStepZero(request):
    form = StepZeroForm()

    if request.method == 'POST':
        form = StepZeroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('user:signup-step1')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'user/signup_step0.html', context)

def signupStepOne(request):
    form = StepOneForm()

    if request.method == 'POST':
        form = StepOneForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('user:signup-step2')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'user/signup_step1.html', context)

def signupStepTwo(request):
    form = StepTwoForm()

    if request.method == 'POST':
        form = StepTwoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('user:signup-step3')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'user/signup_step2.html', context)

def signupStepThree(request):
    form = StepThreeForm()

    if request.method == 'POST':
        form = StepThreeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('user:login')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'user/signup_step3.html', context)

@login_required(login_url = 'login')
def goBackStepZero(request):
    user = request.user
    form = StepZeroForm(instance = user)

    if request.method == 'POST':
        form = StepZeroForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('user:signup-step1')
    
    context = {'form': form }
    return render(request, 'user/signup_step0.html', context)

@login_required(login_url = 'login')
def goBackStepOne(request):
    user = request.user
    form = StepOneForm(instance = user)

    if request.method == 'POST':
        form = StepOneForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('user:signup-step2')
    
    context = {'form': form }
    return render(request, 'user/signup_step1.html', context)

@login_required(login_url = 'login')
def goBackStepTwo(request):
    user = request.user
    academics = AcademicsInfo.objects.get(user = user)
    form = StepTwoForm(instance = academics)

    if request.method == 'POST':
        form = StepTwoForm(request.POST, request.FILES, instance = academics)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('user:signup-step3')
    
    context = {'form': form }
    return render(request, 'user/signup_step2.html', context)




@login_required(login_url = 'login')
def editProfile(request):
    user = request.user
    academics = AcademicsInfo.objects.get(user = user)
    company = CompanyInfo.objects.get(user = user)
    form1 = EditUserProfile(instance = user)
    form2 = StepTwoForm(instance = academics)
    form3 = StepThreeForm(instance = company)

    if request.method == 'POST':
        form1 = EditUserProfile(request.POST, request.FILES, instance = user)
        form2 = StepTwoForm(request.POST, request.FILES, instance = academics)
        form3 = StepThreeForm(request.POST, request.FILES, instance = company)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form_userInfo = form1.save(commit=False)
            form_userInfo.user = request.user
            form_userInfo.save()
            form_academicInfo = form2.save(commit=False)
            form_academicInfo.user = request.user
            form_academicInfo.save()
            form_companyInfo = form3.save(commit=False)
            form_companyInfo.user = request.user
            form_companyInfo.save()
            

            return redirect('user:profile', pk = user.email)
    
    context = {'user':user, 'form1': form1, 'form2': form2, 'form3' : form3 }
    return render(request, 'user/edit-profile.html', context)


