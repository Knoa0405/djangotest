from django.db import models

# Create your models here.

# 모델 클래스 정의 후 테이블 생성시 자동으로 id field 가 저장된다.
class Fcuser(models.Model) :
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    user_email = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
    # id = models.AutoField(primary_key=True)
    def __str__(self) :
        return self.username

    class Meta :
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트 캠퍼스 사용자'
        verbose_name_plural = '패스트 캠퍼스 사용자'
        