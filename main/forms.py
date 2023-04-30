from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import ProductReview,UserAddressBook,OrderAnon

class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')
		labels={
           "first_name": "Имя",
	   		'last_name':'Фамилия',
			'email':'Email',
			'username':'Имя пользователя',
			'password1':'Пароль',
			'password2':'Повторный пароль',
       }

# Review Add Form
class ReviewAdd(forms.ModelForm):
	class Meta:
		model=ProductReview
		fields=('review_text','review_rating')
		labels={
           "review_text": "Комментарий ",
	   	   'review_rating':'Оценка',
       }

# AddressBook Add Form
class AddressBookForm(forms.ModelForm):
	class Meta:
		model=UserAddressBook
		labels={
           "address": "Адрес ",
	   	   'mobile':'Мобильный телефон',
		   "status":'Cостояние',  
       }
		fields=('address','mobile','status')

# ProfileEdit
class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')