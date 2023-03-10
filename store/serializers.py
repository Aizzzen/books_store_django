from rest_framework.serializers import ModelSerializer

from store.models import Books, UserBookRelation


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class UserBooksRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
