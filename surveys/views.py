from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from .models import Survey, Question
from django.http import JsonResponse

# Import necessary functions from Django

def home(request):
  """Renders the home page template"""
  return render(request, "surveys/home.html")

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

  return render(request, "surveys/signup.html")

# Handles user signup. Checks for existing email, matching passwords, creates user object, 
# sends success/error messages, and redirects to home page
@transaction.atomic
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

  return render(request, "surveys/login.html")

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
  return render(request, "surveys/dashboard.html")


def fromscratch(request):
    if request.method == 'POST':
        # Handle survey creation
        if 'surveyName' in request.POST and 'surveyDescription' in request.POST:
            survey_name = request.POST['surveyName']
            survey_description = request.POST['surveyDescription']
            survey = Survey(name=survey_name, description=survey_description)
            survey.save()

            return JsonResponse({
                'survey_name': survey.name,
                'survey_description': survey.description,
                'survey_id': survey.id  # Return the survey ID
            })

        # Handle adding questions dynamically
        if 'addQuestionText' in request.POST and 'addOptions' in request.POST:
            survey_id = request.POST.get('survey_id')
            survey = Survey.objects.get(id=survey_id)

            question_text = request.POST['addQuestionText']
            options = request.POST['addOptions']

            if question_text and options:
                option_list = [option.strip() for option in options.split(',') if option.strip()]
                question = Question(survey=survey, question_text=question_text, options=option_list)
                question.save()

                return JsonResponse({
                    'question_text': question.question_text,
                    'options': option_list  # Return the list of options
                })

    return render(request, "surveys/fromscratch.html")