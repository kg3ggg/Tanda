from django.urls import path
from .views.tanda import QuestionListAPIView
from .views.professions import ProfessionViewSet
from .views.top_profession import TopProfessionAPIView

urlpatterns = [
    path("", QuestionListAPIView.as_view(), name="tanda-list"),
    path("professions/", ProfessionViewSet.as_view(), name="Profession-list"),
    path("top-profession/", TopProfessionAPIView.as_view(), name="top-profession"),
]
