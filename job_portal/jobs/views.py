from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import JobForm



def job_list_view(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail_view(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def about_us_view(request):
    return render(request, 'jobs/about_us.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff

# Only staff (admin) users can access this view
@login_required
@user_passes_test(is_admin)
def post_job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job-list-web')  # Change to your job list page name
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]  # Only admin can post
        return [permissions.AllowAny()]  # Anyone can view


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]  # Optional: Allow all to view



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('job-list-web')  # Redirect after login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'jobs/login.html')

def logout_view(request):
    logout(request)
    return redirect('job-list-web')
