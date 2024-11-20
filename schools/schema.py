import graphene
from graphene_django.types import DjangoObjectType
from .models import School
from accounts.models import CustomUser
from courses.models import Course

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username", "first_name", "last_name")

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ("id", "name", "description", "created_at", "updated_at")

class SchoolType(DjangoObjectType):
    courses = graphene.List(CourseType)  # Add this field to query courses

    class Meta:
        model = School
        fields = ("id", "name", "admin", "created_at", "updated_at","courses")

    def resolve_courses(self, info):
        return self.courses.all()


class Query(graphene.ObjectType):
    all_schools = graphene.List(SchoolType)

    def resolve_all_schools(self, info):
        return School.objects.all()



class CreateSchool(graphene.Mutation):
    school = graphene.Field(SchoolType)

    class Arguments:
        name = graphene.String(required=True)
        admin_id = graphene.ID(required=True)

    def mutate(self, info, name, admin_id):
        admin = CustomUser.objects.get(pk=admin_id)
        if School.objects.filter(name=name).exists():
            raise GraphQLError("A school with this name already exists.")

        school = School(name=name, admin=admin)
        school.save()
        return CreateSchool(school=school)


class UpdateSchool(graphene.Mutation):
    school = graphene.Field(SchoolType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        admin_id = graphene.ID()

    def mutate(self, info, id, name=None, admin_id=None):
        school = School.objects.get(pk=id)
        if name:
            school.name = name
        if admin_id:
            admin = CustomUser.objects.get(pk=admin_id)
            school.admin = admin
        school.save()
        return UpdateSchool(school=school)


class DeleteSchool(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        school = School.objects.get(pk=id)
        school.delete()
        return DeleteSchool(success=True)

class Mutation(graphene.ObjectType):

    create_school = CreateSchool.Field()
    update_school = UpdateSchool.Field()
    delete_school = DeleteSchool.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
