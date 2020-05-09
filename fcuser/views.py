from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.
def home(request) :
    # user_id = request.session.get('user') # 2 <= 1

    # if user_id :
        # fcuser = Fcuser.objects.get(pk=user_id) # 모델안에서 id를 가져옴 (pk = primary_key) model에서 fcuser.id 가져오고 
        # return HttpResponse(fcuser.username) #세션에 저장해뒀다가 다시 그 세션에 저장된 id랑 모델 id랑 맞는 걸 fcuser에 저장해서 fc.username 출력하네?                             

    # return HttpResponse('Home!')
    return render(request, 'home.html') 

def logout(request) :
    if request.session.get('user') :
        del(request.session['user'])
    
    return redirect('/')

def login(request) :
    if request.method == 'POST':
        form = LoginForm(request.POST) # 폼에 데이터 넣고
        if form.is_valid(): # 데이터가 정상정인지 확인하고 정상이면..
            #session
            request.session['user'] = form.user_id
            return redirect('/')
    else :
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

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
