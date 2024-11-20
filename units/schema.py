import graphene
from graphene_django.types import DjangoObjectType
from .models import Unit
from courses.models import Course
class UnitType(DjangoObjectType):
    class Meta:
        model = Unit
        fields = ("id", "name", "description", "course", "created_at", "updated_at")
class Query(graphene.ObjectType):
    all_units = graphene.List(UnitType)
    units_by_course = graphene.List(UnitType, course_id=graphene.Int(required=True))

    def resolve_all_units(self, info):
        return Unit.objects.all()

    def resolve_units_by_course(self, info, course_id):
        return Unit.objects.filter(course_id=course_id)
class CreateUnit(graphene.Mutation):
    unit = graphene.Field(UnitType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        course_id = graphene.Int(required=True)

    def mutate(self, info, name, description, course_id):
        course = Course.objects.get(pk=course_id)
        unit = Unit(
            name=name,
            description=description,
            course=course,
        )
        unit.save()
        return CreateUnit(unit=unit)


class UpdateUnit(graphene.Mutation):
    unit = graphene.Field(UnitType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name=None, description=None):
        unit = Unit.objects.get(pk=id)
        if name:
            unit.name = name
        if description:
            unit.description = description
        unit.save()
        return UpdateUnit(unit=unit)


class DeleteUnit(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        unit = Unit.objects.get(pk=id)
        unit.delete()
        return DeleteUnit(success=True)
class Mutation(graphene.ObjectType):
    create_unit = CreateUnit.Field()
    update_unit = UpdateUnit.Field()
    delete_unit = DeleteUnit.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)