from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Article

# 클래스 선언 해줘야함

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    # articles = Article.objects.order_by('pk')
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)
    # templates의 name space


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 로직(메세지를 받아서 데이터베이스에 보낸다)
    # GET은 title=제목?content=내용 -> Query에서 가져와라
    # POST는 HTTP body에 감춘다 ->
    # 원래 수정은 POST로 해야함
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 객체 = 모델의 객체
    article = Article(title=title, content=content)
    # 추가
    article.save()

    # return render(request, 'articles/index.html')
    # render != 요청
    # render == 화면을 띄워줄뿐
    # index함수를 이용해서 정보를 가져오고 띄워줬으면 좋겠는데.........

    return redirect('articles:detail', article.pk)
    # 여기로 갈게


def detail(request, pk):
    # 데이터베이스에서 가져온다
    article = Article.objects.get(pk=pk)  # key=value
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
    # url태그와 redirect 는 ':'


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
