'''
 from とか import で始まる行は全部、他のファイルから何かをちょこっとずつ追加する行です。
 なので色んなファイルから必要な部分をコピペする代わりに from ... import ... で必要部分を
入れることができます。
'''
from django.db import models
from django.utils import timezone

'''
classはオブジェクトを定義してますよ、ということを示すキーワードです。
Post はモデルの名前で、他の名前をつけることもできます（が、特殊文字と
空白は避けなければいけません）。モデルの名前は大文字で始めます。
models.Model はポストがDjango Modelだという意味で、Djangoが、これは
データベースに保存すべきものだと分かるようにしています。
'''
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #他のモデルへのリンク
    title = models.CharField(max_length=200)                            #文字数が制限されたテキストを定義するフィールド
    text = models.TextField()                                           #これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ
    created_date = models.DateTimeField(                                #日付と時間のフィールド
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
'''
def publish(self): は何かと言うと、 これこそが先程お話ししたブログを
公開するメソッドそのものです。 def は、これはファンクション（関数）/
メソッドという意味です。publish はメソッドの名前で、 変えることも
できます。
 メソッドの名前に使っていいのは、英小文字とアンダースコアで、アンダー
スコアはスペースの代わりに使います。 （例えば、平均価格を計算する
メソッドは calculate_average_price っていう名前にします）
 メソッドは通常何かを return します。 一つの例が __str__ メソッドに
あります。 このシナリオでは、__str__() を呼ぶと、ポストのタイトルの
テキスト（string）が返ってきます。
 '''
def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title