from rest_framework import serializers
from cms.models import Project, Testimonial, Inquiry


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = '__all__'


class InquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = '__all__'
