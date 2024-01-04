from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('explore', views.explore, name='explore'),
    path('stock/<str:symbol>/', views.stock_details, name='stock'),
    path('stock/<str:symbol>/about', views.stock_about, name='stock_about'),
    path('stock/<str:symbol>/feed', views.stock_feed, name='stock_feed'),
    path('stock/<str:symbol>/news', views.stock_news, name='stock_news'),
    path('stock/<str:symbol>/financials', views.stock_financials, name='stock_financials'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('notifications', views.notifications, name='notifications'),
    path('my_profile', views.profile, name='profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('follow_profile/<int:profile_id>/', views.follow_profile, name='follow_profile'),
    path('stock/<str:symbol>/post', views.post, name='post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('login', views.login, name='login'),
    path('sign_out', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('save_profile', views.save_profile, name='save_profile'),
    path('messages', views.messages, name='messages'),
    path('conversation/<int:conversation_id>/', views.conversation, name='conversation'),
    path('conversation/<int:conversation_id>/send-message', views.send_message, name='send_message'),
    path('polls', views.polls, name='polls'), 
    path('search_polls_assets', views.search_polls_assets, name='search_polls_assets'),
    path('update_poll/<int:asset_id>/<str:poll_type>', views.update_poll, name='update_poll'),
    path('signals', views.signals, name='signals'), 
    path('update_vote/<int:signal_id>/<str:vote_type>', views.update_vote, name='update_vote'),
    path('get_signal_details/<int:signal_id>', views.get_signal_details, name='get_signal_details'),
    path('communities', views.communities, name='communities'),
    path('community/<int:community_id>/', views.view_community, name='view_community'),
    path('community/<int:community_id>/join_community', views.join_community, name='join_community'),
    path('community/<int:community_id>/leave_community', views.leave_community, name='leave_community'),
    path('community/<int:community_id>/delete_community', views.delete_community, name='delete_community'),
    path('community/<int:community_id>/send_community_message', views.send_community_message, name='send_community_message'),
    path('learn', views.learn, name='learn'),
    path('create_signal', views.create_signal, name='create_signal'),
    path('create_community', views.create_community, name='create_community'),
    path('postfeed', views.postfeed, name='postfeed'),
]