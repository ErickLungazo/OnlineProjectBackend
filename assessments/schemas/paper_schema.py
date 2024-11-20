import graphene
from graphene_django.types import DjangoObjectType

from ..models import Paper


class PaperType(DjangoObjectType):
    class Meta:
        model = Paper
        fields = ('id', 'unit', 'assessment', 'lecturer', 'created_at', 'updated_at')


class PaperType(DjangoObjectType):
    class Meta:
        model = Paper
        fields = ('id', 'unit', 'assessment', 'lecturer', 'created_at', 'updated_at')


class Query(graphene.ObjectType):
    all_papers = graphene.List(PaperType)
    paper = graphene.Field(PaperType, id=graphene.Int())

    def resolve_all_papers(self, info):
        return Paper.objects.all()

    def resolve_paper(self, info, id):
        return Paper.objects.get(id=id)


class CreatePaper(graphene.Mutation):
    class Arguments:
        unit_id = graphene.Int(required=True)
        assessment_id = graphene.Int(required=True)
        lecturer_id = graphene.Int(required=True)

    paper = graphene.Field(PaperType)

    def mutate(self, info, unit_id, assessment_id, lecturer_id):
        unit = Unit.objects.get(id=unit_id)
        assessment = Assessment.objects.get(id=assessment_id)
        lecturer = CustomUser.objects.get(id=lecturer_id)
        paper = Paper.objects.create(
            unit=unit,
            assessment=assessment,
            lecturer=lecturer
        )
        return CreatePaper(paper=paper)


class UpdatePaper(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        unit_id = graphene.Int()
        assessment_id = graphene.Int()
        lecturer_id = graphene.Int()

    paper = graphene.Field(PaperType)

    def mutate(self, info, id, unit_id=None, assessment_id=None, lecturer_id=None):
        paper = Paper.objects.get(id=id)
        if unit_id:
            paper.unit = Unit.objects.get(id=unit_id)
        if assessment_id:
            paper.assessment = Assessment.objects.get(id=assessment_id)
        if lecturer_id:
            paper.lecturer = CustomUser.objects.get(id=lecturer_id)
        paper.save()
        return UpdatePaper(paper=paper)


class DeletePaper(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            paper = Paper.objects.get(id=id)
            paper.delete()
            return DeletePaper(success=True)
        except Paper.DoesNotExist:
            return DeletePaper(success=False)


class Mutation(graphene.ObjectType):
    create_paper = CreatePaper.Field()
    update_paper = UpdatePaper.Field()
    delete_paper = DeletePaper.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
