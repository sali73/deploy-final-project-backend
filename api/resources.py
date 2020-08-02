from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from api.models import Students , Offering , Course , Instructor
from tastypie.authorization import Authorization

class StudentsResource(ModelResource):
    class Meta:
        queryset = Students.objects.all()
        resource_name = 'Student'
        authorization = Authorization()

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        authorization = Authorization()

class InstructorResource(ModelResource):
    class Meta:
        queryset = Instructor.objects.all()
        resource_name = 'instructor'
        authorization = Authorization()

class OfferingResource(ModelResource):
    course = fields.ForeignKey(CourseResource, 'course')
    instructor = fields.ForeignKey(InstructorResource, 'instructor')
    class Meta:
        queryset = Offering.objects.all()
        resource_name = 'offering'
        authorization = Authorization()



