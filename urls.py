from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect(reverse('converter:upload_file'))),  # 기본 루트를 리디렉션
    path('converter/', include('converter.urls')),  # 'converter' 앱의 URL 포함
    path('ranking/', include('ranking.urls')),  # 랭킹 추적기 URL 포함
    path('invoice/', include('invoice.urls')),  # 인보이스 URL 포함
    path('keywords/', include('keywords.urls')),  # 키워드 URL 포함
    path('accounts/', include('accounts.urls')),  # 계정 관리 URL 포함
    path('chaser/', include('chaser.urls')),  # 추격자 URL 포함
    path('keywordextractor/', include('keywordextractor.urls', namespace='keywordextractor')),

]
