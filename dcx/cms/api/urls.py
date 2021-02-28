from django.urls import path
from .views import AllAdminProjectView, AllDisplayProjectView, DetailAdminProjectView, AllAdminTestimonialView, \
    AllDisplayTestimonialView, DetailAdminTestimonialView, AllInquiryView, newInquiry

urlpatterns = [
    path('admin/projects/', AllAdminProjectView.as_view(), name='allSubmissions'),
    path('admin/project/<int:pk>/', DetailAdminProjectView.as_view(), name='detailSubmission'),
    path('admin/project/', DetailAdminProjectView.as_view(), name='adminCompleted'),
    path('projects/', AllDisplayProjectView.as_view(), name='mySubmissions'),
    # testimonials
    path('admin/testimonials/', AllAdminTestimonialView.as_view(), name='allSubmissions'),
    path('admin/testimonial/<int:pk>/', DetailAdminTestimonialView.as_view(), name='detailSubmission'),
    path('admin/testimonial/', DetailAdminTestimonialView.as_view(), name='adminCompleted'),
    path('testimonials/', AllDisplayTestimonialView.as_view(), name='mySubmissions'),
    # inquiries
    path('admin/inquiries/', AllInquiryView.as_view(), name='allSubmissions'),
    path('admin/inquiry/', newInquiry, name='detailSubmission'),
]
