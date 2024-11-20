import graphene

from assessments.schemas.assessment_schema import Query as AssessmentQuery, Mutation as AssessmentMutation
from assessments.schemas.paper_schema import Query as PaperQuery, Mutation as PaperMutation
from courses.schema import Query as CourseQuery, Mutation as CourseMutation
from schools.schema import Query as SchoolQuery, Mutation as SchoolMutation
from units.schema import Query as UnitQuery, Mutation as UnitMutation


class Query(SchoolQuery,
            CourseQuery,
            UnitQuery,
            AssessmentQuery,
            PaperQuery,
            graphene.ObjectType):
    pass


class Mutation(SchoolMutation,
               CourseMutation,
               UnitMutation,
               AssessmentMutation,
               PaperMutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
