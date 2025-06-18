from django.urls import path
from .views import JobListCreateAPIView, JobDetailAPIView, job_list_view, job_detail_view,logout_view
from .views import about_us_view, post_job_view,login_view

urlpatterns = [
    # API endpoints
    path('list', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('list/<int:id>/', JobDetailAPIView.as_view(), name='job-detail'),

    # Web page views
    path('', job_list_view, name='job-list-web'),
    path('web/<int:id>/', job_detail_view, name='job-detail-web'),
    path('about/', about_us_view, name='about-us'),
    path('login/', login_view, name='login'),
    path('post/', post_job_view, name='post-job'),
    path('logout/', logout_view, name='logout'),
]