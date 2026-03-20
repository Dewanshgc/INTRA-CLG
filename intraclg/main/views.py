import sys
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage, UserProfile
from .forms import ChatForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage, UserProfile
from .forms import ChatForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from .models import UserProfile
import sys

from django.contrib.auth.decorators import login_required
from .models import UserProfile
import sys
import sys
print("📂 views.py loaded", file=sys.stderr)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import sys






@login_required
def universal_chat(request):
    # Get all users except self
    users = User.objects.exclude(id=request.user.id)

    selected_role = request.GET.get('role')
    if selected_role:
        users = users.filter(userprofile__role=selected_role)

    messages = ChatMessage.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('timestamp')

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = request.user
            chat.save()
            return redirect('universal_chat')
    else:
        form = ChatForm()

    context = {
        'form': form,
        'users': users,  # <-- used to show user list
        'messages': messages,
        'roles': UserProfile.ROLE_CHOICES,
        'selected_role': selected_role
    }
    return render(request, 'main/chat.html', context)


@login_required
def universal_chat(request):
    # Get selected role filter from query string (e.g., ?role=student)
    selected_role = request.GET.get('role')
    
    # Exclude current user and filter by role if selected
    users = User.objects.exclude(id=request.user.id)
    if selected_role:
        users = users.filter(userprofile__role=selected_role)

    # Get all messages involving the current user
    messages = ChatMessage.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('timestamp')

    # Handle chat form submission
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = request.user
            chat.save()
            return redirect('universal_chat')
    else:
        form = ChatForm()

    context = {
        'form': form,
        'users': users,
        'messages': messages,
        'roles': UserProfile.ROLE_CHOICES,
        'selected_role': selected_role
    }
    return render(request, 'main/chat.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def student_dashboard(request):
    return render(request, 'main/student_dashboard.html')

@login_required
def faculty_dashboard(request):
    return render(request, 'main/faculty_dashboard.html')

@login_required
def alumni_dashboard(request):
    return render(request, 'main/alumni_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def events(request):
    return render(request, 'main/events.html')

def admissions(request):
    return render(request, 'main/admissions.html')



def achievements(request):
    return render(request, 'main/achievements.html')

def login_view(request):
    return render(request, 'main/login.html')

def signup_view(request):
    return render(request, 'main/signup.html')

def role_selection(request):
    return render(request, 'main/role_selection.html')

from django.shortcuts import render

def placements(request):
    companies = [
        {"name": "tcs", "ext": "jpeg"},
        {"name": "infosys", "ext": "png"},
        {"name": "wipro", "ext": "jpeg"},
        {"name": "hcl", "ext": "jpg"},
        {"name": "capgemini", "ext": "jpg"},
        {"name": "zoho", "ext": "webp"},
        {"name": "l&t", "ext": "jpeg"},
        {"name": "cognizant", "ext": "jpg"},
    ]

    stats = [
        {"branch": "Computer Science", "placed": 78, "highest": 12, "average": 4.2},
        {"branch": "ECE", "placed": 65, "highest": 10, "average": 3.8},
        {"branch": "EEE", "placed": 52, "highest": 8, "average": 3.5},
        {"branch": "Mechanical", "placed": 40, "highest": 6, "average": 3.2},
        {"branch": "MCA", "placed": 30, "highest": 7.5, "average": 3.9},
        {"branch": "MBA", "placed": 25, "highest": 6.8, "average": 4.1},
    ]

    return render(request, 'main/placements.html', {
        "companies": companies,
        "stats": stats
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # ✅ allow login immediately
            user.save()

            # Send verification email anyway
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            activation_link = f"http://127.0.0.1:8000/activate/{uid}/{token}/"

            subject = 'Verify your IntraClg email'
            message = render_to_string('main/email_activation.html', {
                'user': user,
                'activation_link': activation_link
            })

            send_mail(subject, message, None, [user.email])
            return render(request, 'main/email_sent.html', {'email': user.email})
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'main/activation_success.html')
    else:
        return render(request, 'main/activation_failed.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('role_selection')  # or any dashboard URL
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def set_user_role(request, role):
    valid_roles = ['student', 'faculty', 'alumni', 'admin']
    if role in valid_roles:
        request.session['user_role'] = role  # 🔒 optional for future use

        if role == 'student':
            return redirect('student_dashboard')
        elif role == 'faculty':
            return redirect('faculty_dashboard')
        elif role == 'alumni':
            return redirect('alumni_dashboard')
        elif role == 'admin':
            return redirect('admin_dashboard')
    else:
        messages.error(request, "Invalid role selected.")
        return redirect('role_selection')
    

# Admin Views
@login_required
def admin_users(request):
    return render(request, 'main/admin_dashboard/users.html', {'profile': request.user.userprofile})

def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')

def admin_profile(request):
    return render(request, 'main/admin_dashboard/profile.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
import sys

@login_required
def admin_update_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.mobile = request.POST.get('mobile')
        profile.interests = request.POST.get('interests')

        # Update User model email
        user.email = request.POST.get('email')
        user.save()

        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']

        profile.save()
        print("✅ Admin profile updated:", profile.full_name, file=sys.stderr)
        return redirect('admin_profile')

    return render(request, 'main/admin_dashboard/updateprofile.html', {'profile': profile})

def manage_users(request):
    return render(request, 'main/admin_dashboard/users.html')

def departments(request):
    return render(request, 'main/admin_dashboard/departments.html')

def admin_reports(request):
    return render(request, 'main/admin_dashboard/reports.html')

def site_settings(request):
    return render(request, 'main/admin_dashboard/site_settings.html')


# Student Views
def student_dashboard(request):
    return render(request, 'main/student_dashboard.html')

def student_profile(request):
    return render(request, 'main/student_dashboard/profile.html')

from django.contrib.auth.decorators import login_required
from .models import UserProfile
import sys

@login_required
def student_update_profile(request):
    print("✅ View reached!", file=sys.stderr)

    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        print("📩 Form submitted", file=sys.stderr)

        profile.full_name = request.POST.get('full_name')
        profile.department = request.POST.get('department')
        profile.year = request.POST.get('year')
        profile.interests = request.POST.get('interests')

        if 'photo' in request.FILES:
            print("🖼️ Image uploaded", file=sys.stderr)
            profile.photo = request.FILES['photo']

        profile.save()
        print("✅ Profile saved:", profile.full_name, file=sys.stderr)
        return redirect('student_profile')

    return render(request, 'main/student_dashboard/updateprofile.html', {'profile': profile})


def student_feed(request):
    return render(request, 'main/student_dashboard/feed.html')

def student_study(request):
    return render(request, 'main/student_dashboard/study.html')

def student_events(request):
    return render(request, 'main/student_dashboard/events.html')

def student_marketplace(request):
    return render(request, 'main/student_dashboard/marketplace.html')

def student_tutoring(request):
    return render(request, 'main/student_dashboard/tutoring.html')

# Universal Chat View
def universal_chat(request):
    return render(request, 'main/chat.html') 



# Alumni Views
def alumni_dashboard(request):
    return render(request, 'main/alumni_dashboard.html')

def alumni_profile(request):
    return render(request, 'main/alumni_dashboard/profile.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
import sys

@login_required
def alumni_update_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.year = request.POST.get('year')
        profile.branch = request.POST.get('branch')
        profile.company = request.POST.get('company')
        profile.bio = request.POST.get('bio')

        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']

        profile.save()
        print("✅ Alumni profile updated:", profile.full_name, file=sys.stderr)
        return redirect('alumni_profile')

    return render(request, 'main/alumni_dashboard/updateprofile.html', {'profile': profile})


def alumni_jobs(request):
    return render(request, 'main/alumni_dashboard/jobs.html')

def alumni_mentorship(request):
    return render(request, 'main/alumni_dashboard/mentorship.html')

def alumni_events(request):
    return render(request, 'main/alumni_dashboard/events.html')


# Faculty Views
def faculty_dashboard(request):
    return render(request, 'main/faculty_dashboard.html')

def faculty_profile(request):
    return render(request, 'main/faculty_dashboard/profile.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
import sys

@login_required
def faculty_update_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.department = request.POST.get('department')
        profile.mobile = request.POST.get('mobile')
        profile.interests = request.POST.get('interests')

        # Optional: update user model email too
        user.email = request.POST.get('email')
        user.save()

        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']

        profile.save()
        print("✅ Faculty profile updated:", profile.full_name, file=sys.stderr)
        return redirect('faculty_profile')

    return render(request, 'main/faculty_dashboard/updateprofile.html', {'profile': profile})


def faculty_feedback(request):
    return render(request, 'main/faculty_dashboard/feedback.html')

def faculty_materials(request):
    return render(request, 'main/faculty_dashboard/materials.html')

def faculty_events(request):
    return render(request, 'main/faculty_dashboard/events.html')

def faculty_reports(request):
    return render(request, 'main/faculty_dashboard/reports.html')

# Universal Chat View
def universal_chat(request): return render(request, 'main/chat.html')