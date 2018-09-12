from django_filters.rest_framework import DjangoFilterBackend


# Filtro usado na view de registro (infelizmente só por url)
class RegisterFilter(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset