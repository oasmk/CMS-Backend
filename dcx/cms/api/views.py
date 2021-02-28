from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import ProjectSerializer, TestimonialSerializer, InquirySerializer
from cms.models import Project, Inquiry, Testimonial


class AllDisplayProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            queryset = Project.objects.all().filter(on_display=True)
            return queryset
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllAdminProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            queryset = Project.objects.all()
            return queryset
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DetailAdminProjectView(APIView):

    def post(self, request, *args, **kwargs):
        project = Project.objects.create()
        serializer = ProjectSerializer(project, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            submission = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(submission, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            submission = Project.objects.get(pk=pk)
            submission.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def newInquiry(request):
    inquiry = Inquiry.objects.create()
    serializer = InquirySerializer(inquiry, request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllInquiryView(generics.ListAPIView):
    serializer_class = InquirySerializer

    def get_queryset(self):
        try:
            queryset = Inquiry.objects.all()
            return queryset
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllDisplayTestimonialView(generics.ListAPIView):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        try:
            queryset = Testimonial.objects.all().filter(on_display=True)
            return queryset
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllAdminTestimonialView(generics.ListAPIView):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        try:
            queryset = Testimonial.objects.all()
            return queryset
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DetailAdminTestimonialView(APIView):

    def post(self, request, *args, **kwargs):
        project = Testimonial.objects.create()
        serializer = TestimonialSerializer(project, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        project = Testimonial.objects.get(pk=pk)
        serializer = TestimonialSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            submission = Testimonial.objects.get(pk=pk)
            serializer = TestimonialSerializer(submission, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            submission = Testimonial.objects.get(pk=pk)
            submission.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
