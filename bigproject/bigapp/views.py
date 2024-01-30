from django.shortcuts import render
from django.contrib.auth.models import User

def myenjoy(request):
    if request.method == "POST":
        # Handle the POST request as before
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = User.objects.filter(email=email)

        if user:
            msg = "User already exists"
            return render(request, "register.html", {'msg': msg})
        else:
            if password == cpassword:
                newuser = User.objects.create(first_name=fname, last_name=lname, email=email, password=password)
                message = "User registered successfully"
                return render(request, 'login.html', {'msg': message})
            else:
                msg = "Password and confirm password do not match"
                return render(request, 'register.html', {'msg': msg})





