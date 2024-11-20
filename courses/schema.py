import graphene
from graphene_django.types import DjangoObjectType
from .models import Course

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ("id", "name", "description", "school", "created_at", "updated_at")

class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)
    courses_by_school = graphene.List(CourseType, school_id=graphene.Int(required=True))

    def resolve_all_courses(self, info):
        return Course.objects.all()

    def resolve_courses_by_school(self, info, school_id):
        return Course.objects.filter(school_id=school_id)

class CreateCourse(graphene.Mutation):
    course = graphene.Field(CourseType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        school_id = graphene.Int(required=True)

    def mutate(self, info, name, description, school_id):
        from schools.models import School  # Avoid circular imports

        school = School.objects.get(pk=school_id)

        course = Course(
            name=name,
            description=description,
            school=school,
        )
        course.save()
        return CreateCourse(course=course)


class UpdateCourse(graphene.Mutation):
    course = graphene.Field(CourseType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name=None, description=None):
        course = Course.objects.get(pk=id)
        if name:
            course.name = name
        if description:
            course.description = description
        course.save()
        return UpdateCourse(course=course)


class DeleteCourse(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        course = Course.objects.get(pk=id)
        course.delete()
        return DeleteCourse(success=True)

class Mutation(graphene.ObjectType):
    create_course = CreateCourse.Field()
    update_course = UpdateCourse.Field()
    delete_course = DeleteCourse.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
