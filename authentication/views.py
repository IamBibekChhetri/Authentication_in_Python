
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from authentication.models import Profile
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from authentication.models import Otp


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user=CustomUser.objects.create_user(username=username,password=password,email=email,phone=phone)
        user.save()
        # print("Your Account has been created successfully!")
        messages.success(request,"Your Account has been created successfully")

        return redirect('/signin')

        
    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password')

       #validation for login

    #    if user.object.filter(email!=email):
    #        messages.error(request,"Email doesn't match! ")
    #        return redirect("home")
       
    #    if user.object.filter(password!=password):
    #        messages.error(request,"Password doesn't match!")
    #        return redirect("home")
       

       user = authenticate(request,email=email, password=password)
    #    print(user)
       if user is not None:
           login(request,user)
           messages.info(request,'You are now logged in!')
           return redirect("home")
       else:
           messages.error(request,'Invalid Credentials!')
           return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"You have been log out successfully")
    return redirect('home')


# Profile Update
@login_required
def profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method == 'POST':
        if 'image' in request.FILES:
            image=request.FILES['image']
            profile.image=image
        Username = request.POST['username']
        Email = request.POST['email']
        Phone = request.POST['phone']
        user = request.user

        user.username = Username
        user.email = Email
        #user.image = image
        user.phone = Phone
        user.save()
        profile.save()
        messages.success(request,"Profile Update Successfully!!!")
        return redirect('profile')
    return render(request, 'authentication/profile.html', {'user': request.user, 'profile':profile})

# Change Password
@login_required
def changePassword(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.user

        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                # Update session authentication hash to prevent logging out the user
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully.')
                return redirect('home')  # Replace 'home' with the desired URL after password change
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Incorrect old password.')

    return render(request, 'authentication/changePassword.html')

# Email verification for resetting password
def emailVerification(request):
    if request.method == 'POST':
        email = request.POST['email']
    # verifying the email first.
        user = CustomUser.objects.filter(email=email).first()
        if user:
            # Generate a random OTP code
            code = get_random_string(length=6, allowed_chars='0123456789')

            # Create an OTP token
            otp_token, create = Otp.objects.get_or_create(user=user)
            otp_token.otp_code = code
            otp_token.save()

            # Compose the email subject and message
            subject = 'OTP Code for Email Verification'
            message = f'Your OTP code for email verification is: {code}'

            # Send the email
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

            # Store the email in the session for verification
            request.session['otp_email'] = email
            # request.session['otp_code'] = otp_token
            # print(otp_token)

            messages.success(request, 'Please check your email for the OTP code.')
            return redirect('otpVerification')  
        # Replace 'verifyOTP' with the desired URL for OTP verification

        else:
            messages.error(request, 'Email address not found.')


    return render(request,'authentication/emailVerification.html')

# Otp Verification

def otpVerification(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp_code')
        if entered_otp == stored_otp:
            email = request.session.get('otp_email')
            user = CustomUser.objects.get(email=email)
            # Perform your desired actions for successful OTP verification
            messages.success(request, 'OTP verified successfully.')
            return redirect('home')  # Replace 'home' with the desired URL after successful verification
        else:
            messages.error(request, 'Invalid OTP code.')
    return render(request,'authentication/otpVerification.html')

# Reset Password
def resetPassword(request):
    '''
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully reset.')
            return redirect('resetPassword')
    else:
        form = SetPasswordForm(user=request.user)'''
    return render(request, 'authentication/resetPassword.html')
#Otp verification after email verification for password reset

    '''
    if request.method == 'POST':
        otp = request.POST['otp_submit']
        print(otp)
        db_otp=Otp.objects.filter('otp_code')
        if otp==db_otp:
            return redirect('resetPassword')'''
    # print("roshni")
    