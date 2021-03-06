from django.shortcuts import render
from .models import NewsData

def news(request):
    '''
    news 리스트 출력
    '''
    news_list = NewsData.objects.order_by('-id')[:10]
    context = {'news_list': news_list}
    return render(request, 'news/news_list.html', context)
