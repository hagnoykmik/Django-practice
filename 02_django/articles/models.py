from django.db import models

# Create your models here.
# models의 Model 클래스를 상속받을 것
class Article(models.Model):
    # 상속받은 것을 그대로 이용한다
    # 우리는 테이블만 정의(column)

    # 클래스 변수가 하나의 필드가 된다
    # 필드 이름 = 타입 -> 스키마를 만들어 보자(설계도)

    title = models.CharField(max_length=10)  # max_length=가 필수
    content = models.TextField()  # 길이 제한이 덜하다(길게 가능)
    created_at = models.DateTimeField(auto_now_add=True)  #
    updated_at = models.DateTimeField(auto_now=True) # 수정시간 
    