# fuzzy_search
A HTTP service that provides an endpoint for fuzzy search of English words.

A Django rest based Word Search Application. This Application basically provides an API to search for a word in a dataset containing 333,333 English words and the frequency of their usage in some corpus.

Requirements to build the project locally

Django==2.2
djangorestframework==3.9.2
requests==2.21

Additional requirements to deploy to heroku

psycopg2==2.8.2
django_heroku
Gunicorn==19.9.0

API is hosted on the heroku. Please use any API testing tools like POSTMAN to test the API.

API Endpoints:

GET https://fuzzy-search-application.herokuapp.com/search?word=proc

Other Example like:

GET https://fuzzy-search-application.herokuapp.com/search?word=imprac

GET https://fuzzy-search-application.herokuapp.com/search?word=proc

GET https://fuzzy-search-application.herokuapp.com/search?word=rose

In the above endpoint "word" is request parameter where you can send the word string to search in the Dataset

This endpoint finally returns a response which is of JSON array containing 25 results, ranked by criteria (see below):

Matches occurs anywhere in the string, not just at the beginning. For example, eryx matches archaeopteryx (among others). Matches at the start of a word ranks higher, For example, for the input pract, the result practical ranks higher than impractical. Common words (those with a higher usage count) ranks higher than rare words. Short words ranks higher than long words. For example, given the input environ, the result environment ranks higher than environmentalism. An exact match should always be ranked as the first result.
