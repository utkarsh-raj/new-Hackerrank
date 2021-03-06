from django.urls import path

from . import views

app_name = 'miniproject'
urlpatterns = [
	path('',views.index,name='index'),
	path('signupuser',views.signup_view,name='signupuser'),
	path('loginuser',views.login_view,name='loginuser'),
	path('logoutuser',views.logout_view,name='logoutuser'),
	path('new_question',views.newQuestion,name='newQuestion'),
	path('question/<int:question_id>',views.viewQuestion,name='viewQuestion'),
	path('question/<int:question_id>/add_testcase',views.addTestCase,name='addTestCase'),

	# path('add',views.add,name="add"),
	# path('details/<int:todo_id>',views.details,name="details"),
	# path('edit/<int:todo_id>',views.edit,name="edit"),
	# path('delete/<int:todo_id>',views.delete,name="delete")
]