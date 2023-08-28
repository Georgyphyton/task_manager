from django import forms
from statuses.models import Statuses
from tasks.models import Tasks
from users.models import CustomUser
from labels.models import Labels
import django_filters


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']


class SearchFilter(django_filters.FilterSet):
    def choose_author(self, queryset, name, value):
        if value:
            author = self.request.user
            return queryset.filter(author=author)
        return queryset

    status = django_filters.ModelChoiceFilter(
        queryset=Statuses.objects.all()
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all()
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Labels.objects.all()
    )
    author = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(),
        label="Только свои задачи",
        method='choose_author')
