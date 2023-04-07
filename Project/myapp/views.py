from django.shortcuts import render , redirect
from .models import User
# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})

		except:
			if request.POST['password']==request.POST['cpassword']:

				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						usertype=request.POST['usertype'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic'],
														
					)

				msg="User Registered successfully"
				return render(request,"signup.html",{'msg':msg})
			else:
				msg="Password and confirm password doesn't matched"
				return render(request,"signup.html",{'msg':msg})


	else:
		return render(request,'signup.html')

def login(request):
	try:
		user=User.objects.get(email=request.POST['email'])
		if user.password==request.POST['password']:
			if user.usertype=="buyer":
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'index.html')

			else:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'seller-index.html')

		else:
			msg="Incorrect Password"
			return render(request,'login.html',{'msg':msg})
	except:
		msg="Email not Registered"
		return render(request,'login.html',{'msg':msg})



	return render(request,'login.html')

def logout(request):

	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')
			else:
				if user.usertype=="buyer":
					msg="New password and Confirm new password doesn't matched"
					return render(request,"change-password.html",{'msg':msg})

				else:
					msg="New password and Confirm new password doesn't matched"
					return render(request,"seller-change-password.html",{'msg':msg})
		else:
			if user.usertype=="buyer":
				msg="Old password doesn't matched"
				return render(request,"change-password.html",{'msg':msg})
			else:
				msg="Old password doesn't matched"
				return render(request,"seller-change-password.html",{'msg':msg})

	else:
		if user.usertype=="buyer":
			return render(request,"change-password.html")
		else:
			return render(request,"seller-change-password.html")


def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']

		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		msg="Profile Updated Successfully"
		return render(request,'profile.html',{'user':user,"msg":msg})
	else:
		return render(request,'profile.html',{'user':user})














