from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

class SnippetSerializer(serializers.ModelSerializer):  # tutorial 继承的是serializers.HyperlinkedModelSerializer类，但目前该类也能使用
    # 添加两个serializer属性。
    # owner 通过serializers对象，获取owner表中的username。
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight添加后怎么获得url? 通过hyperlink 链接到snippet-highlight路由。
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        # serializer包括的变量属性有：继承的serializer的、model中定义的、自定义serializer中的。
        model = Snippet

        # 添加‘url’和‘highlight’类型，get snippet时会出现url，highlight属性。
        fields = ['owner', 'highlight', 'url', 'id', 'title', 'code', 'linenos', 'language', 'style']
        # fields = '__all__'

        # 在这里添加的owner属性没什么用。
        owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    # 换一个还有perlinkedRelatedField类型的属性。
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        # 添加‘url'属性，则get User时会多一个snippets属性。
        # url 添加后自动获得该对象的url? snippets ?
        fields = ['url', 'id', 'username', 'snippets']
        # fields = '__all__'
