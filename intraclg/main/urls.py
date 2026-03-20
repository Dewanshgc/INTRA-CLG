from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('admissions/', views.admissions, name='admissions'),
    path('placements/', views.placements, name='placements'),
    path('achievements/', views.achievements, name='achievements'),
    path('role-selection/', views.role_selection, name='role_selection'),
    path('select-role/<str:role>/', views.set_user_role, name='set_user_role'),
    path('signup/', views.signup_view, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('login/', views.login_view, name='login'),
    path('select-role/student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('select-role/faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('select-role/alumni/dashboard/', views.alumni_dashboard, name='alumni_dashboard'),
    path('select-role/admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('select-role/admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('select-role/admin/profile/', views.admin_profile, name='admin_profile'),
    path('select-role/admin/update-profile/', views.admin_update_profile, name='admin_update_profile'),
    path('select-role/admin/users/', views.manage_users, name='manage_users'),
    path('select-role/admin/departments/', views.departments, name='departments'),
    path('select-role/admin/reports/', views.admin_reports, name='admin_reports'),
    path('select-role/admin/settings/', views.site_settings, name='site_settings'),

    # Student Dashboard URLs
    path('select-role/student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('select-role/student/profile/', views.student_profile, name='student_profile'),
    path('select-role/student/update-profile/', views.student_update_profile, name='student_update_profile'),
    

    path('select-role/student/feed/', views.student_feed, name='student_feed'),
    path('select-role/student/study/', views.student_study, name='student_study'),
    path('select-role/student/events/', views.student_events, name='student_events'),
    path('select-role/student/marketplace/', views.student_marketplace, name='student_marketplace'),
    path('select-role/student/tutoring/', views.student_tutoring, name='student_tutoring'),

    # Universal Chat Page
    path('chat/', views.universal_chat, name='universal_chat'),

    # Alumni Dashboard URLs
    path('select-role/alumni/dashboard/', views.alumni_dashboard, name='alumni_dashboard'),
    path('select-role/alumni/profile/', views.alumni_profile, name='alumni_profile'),
    path('select-role/alumni/update-profile/', views.alumni_update_profile, name='alumni_update_profile'),
    path('select-role/alumni/jobs/', views.alumni_jobs, name='alumni_jobs'),
    path('select-role/alumni/mentorship/', views.alumni_mentorship, name='alumni_mentorship'),
    path('select-role/alumni/events/', views.alumni_events, name='alumni_events'),

    # Faculty Dashboard URLs
    path('select-role/faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('select-role/faculty/profile/', views.faculty_profile, name='faculty_profile'),
    path('select-role/faculty/update-profile/', views.faculty_update_profile, name='faculty_update_profile'),
    path('select-role/faculty/feedback/', views.faculty_feedback, name='faculty_feedback'),
    path('select-role/faculty/materials/', views.faculty_materials, name='faculty_materials'),
    path('select-role/faculty/events/', views.faculty_events, name='faculty_events'),
    path('select-role/faculty/reports/', views.faculty_reports, name='faculty_reports'),

    # Universal Chat
    path('chat/', views.universal_chat, name='universal_chat'),

    path('logout/', views.logout_view, name='logout'),

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
