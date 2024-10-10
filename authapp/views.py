from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact, MembershipPlan, Trainer, Enrollment, Gallery, Attendance,Trainerimg
# Create your views here.
def Home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.info(request,"Password is not matching")
            return redirect('/signup')
        if len(username) != 10:
            messages.info(request,"Phone Number Must be 10 digits")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass  

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass 

        myuser=User.objects.create_user(username,email,pass1)  
        myuser.save()
        messages.success(request,"User is created Please Login")
        return redirect('/login')
            
    return render(request,"signup.html")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")    
            return redirect('/login')
    return render(request,"login.html")

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/login')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery = Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()
        messages.info(request,"Thanks for contacting us we will get back you soon")
        return redirect('/contact')
    
    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    Membership = MembershipPlan.objects.all()
    Selecttrainer = Trainer.objects.all()
    context = {"Membership":Membership,"Selecttrainer":Selecttrainer}
    if request.method == "POST":
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        Phonenumber = request.POST.get('Phonenumber')
        DOB = request.POST.get('DOB')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        reference =request.POST.get('reference') 
        address = request.POST.get('address')
        query = Enrollment(Fullname=Fullname,Email=email,Gender=gender,Phonenumber=Phonenumber,DOB=DOB,Selectmembershipplan=member,Selecttrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks for Enrollment!")
        return redirect('/join')
    return render(request,"enroll.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone = request.user
    posts = Enrollment.objects.filter(Phonenumber=user_phone)
    attendance = Attendance.objects.filter(phonenumber=user_phone)
    context = {"posts":posts, "attendance":attendance}
    return render(request,"profile.html",context)

def gallery(request):
    posts = Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    Selecttrainer = Trainer.objects.all()
    context = {"Selecttrainer":Selecttrainer}
    if request.method == "POST":
        Phonenumber = request.POST.get('Phonenumber')
        Login = request.POST.get('logintime')
        Logout = request.POST.get('logouttime')
        Selectworkout = request.POST.get('workout')
        Trainedby = request.POST.get('trainer')
        query = Attendance(phonenumber=Phonenumber,Login=Login,Logout=Logout,Selectworkout=Selectworkout,Trainedby=Trainedby)
        query.save()
        messages.success(request,"Attendance Applied Successfully")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def trainer(request):
    posts = Trainerimg.objects.all()
    context={"posts":posts}
    return render(request,"trainers.html",context)

def biceps(request):
    return render(request,"bicep.html")

def back(request):
    return render(request,"back.html")

def shoulder(request):
    return render(request,"shoulder.html")

def chest(request):
    return render(request,"chest.html")

def legs(request):
    return render(request,"legs.html") 

def triceps(request):
    return render(request,"triceps.html")   