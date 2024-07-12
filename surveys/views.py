from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Import necessary functions from Django

def home(request):
  """Renders the home page template"""
  return render(request, "home.html")

# Renders the home.html template for the home page

def signup(request):
  """Handles user signup logic"""
  if request.method == "POST":
    email = request.POST['email']
    pass1 = request.POST['password1']
    pass2 = request.POST['password2']

    # Check if email already exists
    if User.objects.filter(email=email).exists():
      messages.error(request, "Email Already Registered!!")
      return redirect('signup')

    # Check if passwords match
    if pass1 != pass2:
      messages.error(request, "Passwords do not match!")
      return redirect('signup')

    # Create user object
    myuser = User.objects.create_user(email, email, pass1)
    myuser.email = email
    myuser.is_active = True  # Set to True for simplification, normally you would send an email confirmation
    myuser.save()

    messages.success(request, "Your Account has been created successfully!! Please log in.")
    return redirect('home')

  return render(request, "signup.html")

# Handles user signup. Checks for existing email, matching passwords, creates user object, 
# sends success/error messages, and redirects to home page

def signin(request):
  """Handles user signin logic"""
  if request.method == 'POST':
    email = request.POST['email']
    pass1 = request.POST['password']

    user = authenticate(username=email, password=pass1)

    if user is not None:
      login(request, user)
      return redirect('dashboard')
    else:
      messages.error(request, "Invalid credentials!")
      return redirect('login')

  return render(request, "login.html")

# Handles user signin. Authenticates user based on email and password, logs user in 
# on success, sends error messages on failure, and redirects accordingly

def signout(request):
  """Logs out the user"""
  logout(request)
  messages.success(request, "Logged Out Successfully!!")
  return redirect('home')

# Logs out the user, sends success message, and redirects to home page

def dashboard(request):
  """Renders the dashboard page template"""
  return render(request, "dashboard.html")

def fromscratch(request):
  return render(request, "fromscratch.html")

# Renders the dashboard.html template for the dashboard page
