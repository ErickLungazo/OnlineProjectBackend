import graphene
from graphene_django.types import DjangoObjectType

from assessments.models import Assessment
from schools.models import School


class AssessmentType(DjangoObjectType):
    class Meta:
        model = Assessment
        fields = ('id', 'name', 'start_date', 'end_date', 'created_at', 'updated_at', 'school')


class Query(graphene.ObjectType):
    all_assessments = graphene.List(AssessmentType)
    assessment = graphene.Field(AssessmentType, id=graphene.Int())

    def resolve_all_assessments(self, info):
        return Assessment.objects.all()

    def resolve_assessment(self, info, id):
        return Assessment.objects.get(id=id)


class CreateAssessment(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        start_date = graphene.DateTime(required=True)
        end_date = graphene.DateTime(required=True)
        school_id = graphene.Int(required=True)

    assessment = graphene.Field(AssessmentType)

    def mutate(self, info, name, start_date, end_date, school_id):
        school = School.objects.get(id=school_id)
        assessment = Assessment.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            school=school
        )
        return CreateAssessment(assessment=assessment)


class UpdateAssessment(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()

    assessment = graphene.Field(AssessmentType)

    def mutate(self, info, id, name=None, start_date=None, end_date=None):
        assessment = Assessment.objects.get(id=id)
        if name:
            assessment.name = name
        if start_date:
            assessment.start_date = start_date
        if end_date:
            assessment.end_date = end_date
        assessment.save()
        return UpdateAssessment(assessment=assessment)


class DeleteAssessment(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)  # The ID of the assessment to delete

    success = graphene.Boolean()  # Return a boolean to indicate success

    def mutate(self, info, id):
        try:
            # Fetch the assessment object and delete it
            assessment = Assessment.objects.get(id=id)
            assessment.delete()
            return DeleteAssessment(success=True)
        except Assessment.DoesNotExist:
            # If the assessment doesn't exist, return success as False
            return DeleteAssessment(success=False)


class Mutation(graphene.ObjectType):
    create_assessment = CreateAssessment.Field()
    update_assessment = UpdateAssessment.Field()
    delete_assessment = DeleteAssessment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
