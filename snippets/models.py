from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# about authentication & permission
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]  # 词法分析器
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    # 再次添加新字段要重新生成迁移文件。
    # python manage.py makemigrations snippets
    # python manage.py migrate
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(default='codeX')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    #  设置owner 和 存储 highlight
    #  这里owner没有设置默认值，在生成迁移文件时要设置默认值。
    #  猜测：这里定义的变量就是创建一张表。
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField(default='')

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

# 乱写的User类，其实django就内置有了一个User类，就是在主页看到的。
# class User(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     username = models.CharField(max_length=100, blank=True, default='')
#     snippets = Snippet(models.Model)
#
#     class Meta:
#         ordering = ['created']
