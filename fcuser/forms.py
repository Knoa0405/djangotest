from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

class LoginForm(forms.Form) :
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages= {
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self) :
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password :
            fcuser = Fcuser.objects.get(username=username)
            # user = Fcuser.objects.all() # 쿼리문 전체 테이블 데이터 할당 [<{key :value},{key :value}>,<{}>
            # fcuser = user.get(username=username)
            #  # username 가진 row 한줄 가져옴 <{key :value},{key :value}>
            # # if fcuser not in user : # dict = dict 으로 비교 해야됌 -? 쿼리문을 dict으로 나타내야됨
            # #     self.add_error('username','등록아이디가 아닙니다.')
            # if not fcuser :
            #     raise ValidationError('등록된 아이디가 없습니다.')
            if not check_password(password,fcuser.password) :
                self.add_error('password','비밀번호가 틀렸습니다.')
            else:
                self.user_id = fcuser.id