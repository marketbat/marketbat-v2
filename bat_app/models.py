from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count
from collections import Counter
import random

class Assets(models.Model):
    BULLISH = 'Bullish'
    BEARISH = 'Bearish'
    NEUTRAL = 'Neutral'

    SENTIMENT_CHOICES = (
            (BULLISH, 'Bullish'),
            (BEARISH, 'Bearish'),
            (NEUTRAL, 'Neutral')
    )

    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=100, choices=SENTIMENT_CHOICES, default=NEUTRAL)
    insights = models.TextField(blank=True)
    market_price =  models.CharField(max_length=100, default="-")
    logo = models.ImageField(upload_to='asset_logo', blank=True)
    icon = models.ImageField(upload_to='asset_icon', blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    list_date = models.DateField(default="")
    locale = models.CharField(max_length=100, blank=True)
    market_cap = models.IntegerField(blank=True, default=0)
    phone_number = models.CharField(max_length=100, blank=True)
    exchange = models.CharField(max_length=100, blank=True)
    employees = models.IntegerField(blank=True, default=0)
    ticker_type = models.CharField(max_length=100, blank=True)
    subscribers = models.ManyToManyField('Profile', related_name='subscribers', blank=True)
    trending = models.BooleanField(default=False)
    posts = models.ManyToManyField('Posts', related_name='asset_post', blank=True)
    profiles_voted_bullish = models.ManyToManyField('Profile', related_name='bullish_assets', blank=True)
    profiles_voted_bearish = models.ManyToManyField('Profile', related_name='bearish_assets', blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def total_polls(self):
        return self.profiles_voted_bullish.count() + self.profiles_voted_bearish.count()

    def percent_bullish(self):
        total = self.total_polls()
        if total > 0:
            return (self.profiles_voted_bullish.count() / total) * 100
        else:
            return 0

    def percent_bearish(self):
        total = self.total_polls()
        if total > 0:
            return (self.profiles_voted_bearish.count() / total) * 100
        else:
            return 0
       

    def update_poll(self, profile, poll_type):
        # Check if the profile has already votedxwxw
        if poll_type == 'bullish':
            self.profiles_voted_bullish.add(profile)
        elif poll_type == 'bearish':
            self.profiles_voted_bearish.add(profile)

        self.save()
            

    def remove_poll(self, profile, poll_type):
        if poll_type == 'bullish':
            self.profiles_voted_bullish.remove(profile)
        elif poll_type == 'bearish':
            self.profiles_voted_bearish.remove(profile)
        
        self.save()
    

    def get_sentiment(self):
        random_tens = random.randint(1, 10)
        sentiment_score = random_tens * 10
        mapped_sentiment = int(round((sentiment_score / 100) * 180, -1))
        if sentiment_score >= 0 and sentiment_score <= 25:
            sentiment_text = "Extremely Bearish"
            sentiment_code = "ebear"
        elif sentiment_score > 25 and sentiment_score <= 45:
            sentiment_text = "Slightly Bearish"
            sentiment_code = "sbear"
        elif sentiment_score > 45 and sentiment_score <= 55:
            sentiment_text = "Neutral"
            sentiment_code = "neu"
        elif sentiment_score > 55 and sentiment_score <= 75:
            sentiment_text = "Slightly Bullish"
            sentiment_code = "sbull"
        elif sentiment_score > 75 and sentiment_score <= 100:
            sentiment_text = "Extremely Bullish"
            sentiment_code = "ebull"
        else:
            sentiment_text = "N/A"

        result = {
        'sentiment_score': sentiment_score,
        'sentiment_deg': mapped_sentiment,
        'sentiment_text': sentiment_text,
        'sentiment_code': sentiment_code
        }

        return result

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True)
    display_name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_dp_image', blank=True)
    cover_picture = models.ImageField(upload_to='profile_cover_image', blank=True)
    bio = models.TextField(blank=True)
    joined = models.DateTimeField( default=datetime.now)
    followers = models.ManyToManyField('Profile', related_name='profile_followers', blank=True)
    following = models.ManyToManyField('Profile', related_name='profile_following', blank=True)
    # Define choices for interests
    interests = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.user.username}"


class Posts(models.Model):
    Bearish = 'Bearish'
    Bullish = 'Bullish'
    Neutral = 'Neutral'

    POST_SENTIMENT_CHOICES = (
            (Bullish, 'Bullish'),
            (Bearish, 'Bearish'),
            (Neutral, 'Neutral')
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    asset = models.ManyToManyField(Assets, related_name='posts_asset', blank=True)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images', blank=True)
    post_video = models.FileField(upload_to='post_videos', blank=True)
    likes = models.ManyToManyField('Profile', related_name='profile_likes', blank=True)
    comments = models.ManyToManyField('Comments', related_name='profile_comments', blank=True)
    reposts = models.ManyToManyField('Profile', related_name='profile_reposts', blank=True)
    post_date = models.DateTimeField(default=datetime.now)
    post_sentiment = models.CharField(max_length=100, choices=POST_SENTIMENT_CHOICES, default=Neutral)
    post_polarity = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    keywords = models.ManyToManyField('Interests', related_name='posts_interests', blank=True)

    def __str__(self):
        return f"{self.post_text}"
    
class Articles(models.Model):
    assets = models.ManyToManyField(Assets, related_name='articles_assets', blank=True)
    article_title = models.TextField(blank=True)
    article_link = models.TextField(blank=True)
    article_author =  models.CharField(max_length=100)
    article_date = models.DateTimeField(default=datetime.now)
    article_image = models.TextField(blank=True)
    article_description = models.TextField(blank=True)
    article_keywords = models.ManyToManyField('Interests', related_name='articles_interests', blank=True)
    article_publisher = models.TextField(blank=True)
    article_publisher_url = models.TextField(blank=True)
    article_publisher_logo = models.TextField(blank=True)

    def __str__(self):
        return f"{self.article_title}"
    
    def delete_old_articles(self):
        # Calculate the date 1 month ago from now
        one_month_ago = timezone.now() - timedelta(days=30)

        # Delete articles older than 1 month
        deleted_count, _ = Articles.objects.filter(
            asset=self.asset,
            article_date__lt=one_month_ago
        ).delete()

        return deleted_count


class Comments(models.Model):
    comment_text = models.TextField()
    comment_author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_author')
    comment_post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment_post')
    comment_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.comment_text}"
    
    
class Notifications(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notification')
    text = models.TextField()
    read = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.text}"
    
class Explore(models.Model):
    image = models.FileField(upload_to='explore_images')
    news = models.TextField(blank=True)



class Interests(models.Model):
    keyword = models.CharField(max_length=100, blank=True)
    posts = models.ManyToManyField(Posts, related_name='posts_interests', blank=True)
    articles = models.ManyToManyField(Articles, related_name='articles_interests', blank=True)

    def __str__(self):
        return f"{self.keyword}"

    @classmethod
    def get_top_interests(cls):
        # Get the top 20 interests based on the sum of articles and posts
        top_interests = cls.objects.annotate(
            total_count=Count('posts') + Count('articles')
        ).order_by('-total_count')[:15]

        return top_interests

    def get_interest_volume(self):
        # Get the number of posts and articles associated with this interest
        post_count = self.posts.count()
        article_count = self.articles.count()

        return post_count + article_count

    def get_associated_assets(self):
        # Get the names of assets associated with this interest through posts and articles
        post_assets = self.posts.values_list('asset__name', flat=True)
        article_assets = self.articles.values_list('assets__name', flat=True)

        # Combine and count the occurrences of each asset
        all_assets = [asset for asset in post_assets if asset is not None] + [asset for asset in article_assets if asset is not None]
        asset_counter = Counter(all_assets)

        # Get the most occurring asset
        most_occuring_asset = asset_counter.most_common(1)
        

        return most_occuring_asset[0][0] if most_occuring_asset else None
    

    
class Conversation(models.Model):

    INBOX = "Inbox"
    REQUEST = "Request"

    MESSAGE_CATEGORY_CHOICES = (
        (INBOX, "Inbox"),
        (REQUEST, "Request")
    )

    participants = models.ManyToManyField(Profile, related_name="conversations")
    messages = models.ManyToManyField('Message', related_name="messages")
    category = models.CharField(max_length=100, choices=MESSAGE_CATEGORY_CHOICES, default=REQUEST)

    def __str__(self):
        return f"{self.participants}"
    
    def get_last_message(self):
        return self.messages.order_by('-timestamp').first()
    

class Message(models.Model):
    TEXT = "Text"
    IMAGE = "Image"
    VIDEO = 'Video'

    CONTENT_TYPE_CHOICES = (
            (TEXT, 'Text'),
            (IMAGE, 'Image'),
            (VIDEO, 'Video'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default=TEXT)  # 'text', 'image', 'video'
    text = models.TextField()  # For captions
    media_file = models.FileField(upload_to='message_media', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Indicates if the message has been read

    def __str__(self):
        return f"{self.text}"
    

class Community(models.Model):
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField()
    display_image = models.FileField(upload_to='community_dp', null=True, blank=True)
    cover_image = models.FileField(upload_to='community_cover', null=True, blank=True)
    participants = models.ManyToManyField(Profile, related_name="group_conversations")
    messages = models.ManyToManyField('CommunityMessage', related_name="group_messages", blank=True)
    date_started = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name}"
    
    def get_last_message(self):
        return self.messages.order_by('-timestamp').first()
    

class CommunityMessage(models.Model):
    TEXT = "Text"
    IMAGE = "Image"
    VIDEO = 'Video'

    CONTENT_TYPE_CHOICES = (
            (TEXT, 'Text'),
            (IMAGE, 'Image'),
            (VIDEO, 'Video'),
    )
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default=TEXT)  # 'text', 'image', 'video'
    text = models.TextField()  # For captions
    media_file = models.FileField(upload_to='message_media', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Indicates if the message has been read

    def __str__(self):
        return f"{self.text}"


class Signal(models.Model):
    BUY = 'Buy'
    SELL = 'Sell'
    BUY_STOP = 'Buy Stop'
    SELL_STOP = 'Sell Stop'
    BUY_LIMIT = 'Buy Limit'
    SELL_LIMIT = 'Sell Limit'
    
    ORDER_TYPE_CHOICES = (
        (BUY, 'Buy'),
        (SELL, 'Sell'),
        (BUY_STOP, 'Buy Stop'),
        (SELL_STOP, 'Sell Stop'),
        (BUY_LIMIT, 'Buy Limit'),
        (SELL_LIMIT, 'Sell Limit')
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_signal')
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE)
    chart = models.FileField(upload_to='signal_charts', null=True, blank=True)
    order_type = models.CharField(max_length=100, choices=ORDER_TYPE_CHOICES)
    analysis = models.TextField(blank=True)
    entry_price = models.CharField(max_length=100)
    takeprofit = models.CharField(max_length=100)
    stoploss = models.CharField(max_length=100)
    upvotes =  models.ManyToManyField('Profile', related_name='profile_upvotes', blank=True)
    downvotes =  models.ManyToManyField('Profile', related_name='profile_downvotes', blank=True)
    expiry = models.DateTimeField()

    def __str__(self):
        return f"{self.asset}"


 