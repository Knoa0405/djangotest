from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.
def home(request) :
    user_id = request.session.get('user') # 2 <= 1

    if user_id :
        fcuser = Fcuser.objects.get(pk=user_id) # 모델안에서 id를 가져옴 (pk = primary_key) model에서 fcuser.id 가져오고 
                                                #세션에 저장해뒀다가 다시 그 세션에 저장된 id랑 모델 id랑 맞는 걸 fcuser에 저장해서 fc.username 출력하네?
        return HttpResponse(fcuser.username)

    return HttpResponse('Home!')

def logout(request) :
    if request.session.get('user') :
        del(request.session['user'])
    
    return redirect('/')

def login(request) :
    if request.method == 'GET' :
        return render(request, 'login.html')
    elif request.method == 'POST' :
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        res_data = {}
        if not(username and password) : 
            res_data['error'] = '모든 값을 입력해야합니다.'
        else :
            fcuser = Fcuser.objects.get(username=username) # model 에서 username(field(열)) 에서 입력받은 username과 같은 하나의 row 만 가져와서 fcuser에 저장 
            if check_password(password, fcuser.password) :
                
                # 비밀번호가 일치, 로그인 처리
                # 세션
                request.session['user'] = fcuser.id # 1 ? 왠 id 인가 했더니 모델에서 클래스 정의 후 테이블 생성시 id 값은 자동으로 생성된다. 
                                                    # 처음에 세션으로 값을 넣을 때는 id 형태로 넣는다. 그럼 세션 id로 변경하여 쿠키에 저장된다. 바로 username 넣는건 좀,,
                                                    # 세션 id는 브라우저마다 다르기 때문에 세션 id 별로 세션 공간이 있다. ({세션 id : fcuser.id}형태로 저장)
                # 홈으로 가는 redirect               
                return redirect('/')
            else :
                res_data['error'] = '비밀번호가 틀렸습니다.'
        return render(request, 'login.html', res_data)

def register(request) :
    if request.method == 'GET' :
        return render(request, 'register.html')
    elif request.method == 'POST' :
        # username = request.POST['username'] # register.html 에 작성된 form 에서 POST 방식으로 input 의 name 값을 키값으로 해서 전달
        # password = request.POST['password']
        # re_password = request.POST['re-password']
        username = request.POST.get('username',None)
        user_email = request.POST.get('user-email', None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        res_data ={}

        if not (username and password and re_password and user_email) :
            res_data['error'] = '모든 값을 입력해야합니다.'

        elif password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        fcuser = Fcuser(
            username = username,
            user_email = user_email,
            password = make_password(password)
        )

        fcuser.save()
        return render(request, 'register.html', res_data)
