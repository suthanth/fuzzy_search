from rest_framework.response import Response
from rest_framework.views import APIView

from fuzzy_search.fuzzy_search_api.fuzzy_word_search import sorting, search


class FuzzySearch(APIView):

    def get(self, request, *args, **kwargs):
        try:
            word = request.GET.get('word')
            search_results = sorting(search(word.lower()), word.lower())
            return Response(
                data=search_results
            )

        except Exception as exception:
            print(str(exception))
