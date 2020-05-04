from django.db import models

# Create your models here.


class Board(models.Model) :
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    # 내가 가리키고 있는 외부 model에서 키를 받아온다 (fcuser.Fcuser 에서 받아오는걸로) 
    # fcuser (가리키는 모델)이 삭제되면? 자기(model) 자신을 어떻게 할건지.. (models.cascade,SET_Null,default)
    writer = models.ForeignKey('fcuser.Fcuser',on_delete=models.CASCADE,
                                verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
  
    # id = models.AutoField(primary_key=True)
    def __str__(self) :
        return self.title

    class Meta :
        db_table = 'fastcampus_board'
        verbose_name = '패스트 캠퍼스 게시글'
        verbose_name_plural = '패스트 캠퍼스 게시글'
        