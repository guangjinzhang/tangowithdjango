from django.shortcuts import render
from MyStreet.models import Street, Comment
from datetime import datetime
from MyStreet.bing_search import run_query

def rate_street():
    street_list = Street.objects.all()
    for street in street_list:
        comment_list = street.comment_set.all()
        sum_safety_rate = 0
        sum_business_rate = 0
        sum_infrastructure_rate = 0
        if comment_list:
            for comment in comment_list:
                sum_safety_rate += comment.safety_rate
                sum_business_rate += comment.business_rate
                sum_infrastructure_rate += comment.infrastructure_rate
            street.average_safety_rate = round(sum_safety_rate/comment_list.count())
            street.average_business_rate = round(sum_business_rate/comment_list.count())
            street.average_infrastructure_rate = round(sum_infrastructure_rate/comment_list.count())
            street.average_rate = round((street.average_safety_rate+street.average_business_rate+street.average_infrastructure_rate)/3)
            street.save()


def index(request):
    rate_street()
    street_list = Street.objects.order_by('-average_rate')[:5]
    street_list2 = Street.objects.order_by('-average_rate').reverse()[:5]
    context_dict = {'streets': street_list, 'streets2': street_list2}
    return render(request, 'MyStreet/index.html', context_dict)

def safetylist(request):
    rate_street()
    street_list = Street.objects.order_by('-average_safety_rate')[:5]
    street_list2 = Street.objects.order_by('-average_safety_rate').reverse()[:5]
    context_dict = {'streets': street_list, 'streets2': street_list2}
    return render(request, 'MyStreet/safetylist.html', context_dict)

def businesslist(request):
    rate_street()
    street_list = Street.objects.order_by('-average_business_rate')[:5]
    street_list2 = Street.objects.order_by('-average_business_rate').reverse()[:5]
    context_dict = {'streets': street_list, 'streets2': street_list2}
    return render(request, 'MyStreet/businesslist.html', context_dict)

def infrastructurelist(request):
    rate_street()
    street_list = Street.objects.order_by('-average_infrastructure_rate')[:5]
    street_list2 = Street.objects.order_by('-average_infrastructure_rate').reverse()[:5]
    context_dict = {'streets': street_list, 'streets2': street_list2}
    return render(request, 'MyStreet/infrastructurelist.html', context_dict)

def alllist(request):
    street_list = Street.objects.order_by('-name').reverse()
    context_dict = {'streets': street_list}
    return render(request, 'MyStreet/alllist.html', context_dict)

def about(request):
    return render(request, 'MyStreet/about.html', {})


def street(request, street_name_slug):
    context_dict = {}

    try:
        # Can we find a street name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        street = Street.objects.get(slug=street_name_slug)
        context_dict['street_name'] = street.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        comment = Comment.objects.filter(street=street)

        # Adds our results list to the template context under name pages.
        context_dict['comment'] = comment
        # We also add the street object from the database to the context dictionary.
        # We'll use this in the template to verify that the street exists.
        context_dict['street'] = street
    except Street.DoesNotExist:
        # We get here if we didn't find the specified street.
        # Don't do anything - the template displays the "no street" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'MyStreet/street.html', context_dict)


from MyStreet.forms import StreetForm


def add_street(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = StreetForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new street to the database.
            street = form.save(commit=False)
            street.image = request.FILES['image']
            street.save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = StreetForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'MyStreet/add_street.html', {'form': form})


from MyStreet.forms import CommentForm

def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'MyStreet/search.html', {'result_list': result_list})
def add_comment(request, street_name_slug):

    try:
        cat = Street.objects.get(slug=street_name_slug)
    except Street.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if cat:
                comment = form.save(commit=False)
                comment.rate = round((comment. safety_rate + comment.business_rate + comment.infrastructure_rate) / 3)
                comment.street = cat
                comment.user = request.user
                comment.time = datetime.now()
                comment.save()
                rate_street()
                return street(request, street_name_slug)
        else:
            print form.errors
    else:
        form = CommentForm()

    context_dict = {'form':form, 'street': cat}

    return render(request, 'MyStreet/add_comment.html', context_dict)


from MyStreet.forms import UserForm, UserProfileForm


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'MyStreet/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/MyStreet/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'MyStreet/login.html', {})

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/MyStreet/')