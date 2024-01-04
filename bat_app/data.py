from django.shortcuts import render
from .models import Assets, Profile, Posts, Articles,  Notifications, Comments, Explore, Interests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
import requests
import io
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from datetime import datetime
import svglib
import time

def get_news(limit):
    try:
        base_url = "https://api.polygon.io/v2/reference/news"
        api_key = "mPPslHGjobijJVWn8R03vFPREPTiTZSW"  # Replace with your actual API key

        endpoint_url = f"{base_url}?limit={limit}&apiKey={api_key}"
        response = requests.get(endpoint_url)
        print(response)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", {})
            for result in results:
                print(result)
                assets_data = result.get("tickers", [])
                assets = []
                for asset_data in assets_data:
                    try:
                        asset = Assets.objects.get(symbol=asset_data)
                        assets.append(asset)
                    except Assets.DoesNotExist:
                        pass
                print(assets)

                article_title = result.get("title", "")
                article_link = result.get("article_url", "")
                article_author = result.get("author", "")
                article_date = result.get("published_utc", "")
                #article_date = datetime.fromisoformat(article_date_str)
                article_image = result.get("image_url", "")
                article_description = result.get("description", "")
                article_keywords = result.get("keywords", [])
                
                article_publisher = result.get("publisher", {}).get("name", "")
                article_publisher_url = result.get("publisher", {}).get("homepage_url", "")
                article_publisher_logo = result.get("publisher", {}).get("favicon_url", "")

                article, created = Articles.objects.get_or_create(
                    article_title=article_title,
                    article_link=article_link,
                    article_author=article_author,
                    article_date=article_date,
                    article_image=article_image,
                    article_description=article_description,
                    
                    article_publisher=article_publisher,
                    article_publisher_url=article_publisher_url,
                    article_publisher_logo=article_publisher_logo
                )

                for keyword in article_keywords:
                    print(keyword)
                    interest, created = Interests.objects.get_or_create(
                        keyword = keyword,
                
                    )
                    interest.articles.add(article)
                    interest.save()

                # Add associated assets to the article
                article.assets.set(assets)

                # Print some information
                if created:
                    print(f"Created Article: {article}")
                else:
                    print(f"Updated Article: {article}")

    except Exception as e:
        print(f"Error processing news for: {e}")


def download_and_save_logo(logo_url, symbol, type):
    try:
        logo_response = requests.get(logo_url)
        if logo_response.status_code == 200:
            content_type = logo_response.headers.get('content-type', '').lower()

            if content_type.startswith('image/jpeg'):
                img = Image.open(BytesIO(logo_response.content))
                image_buffer = BytesIO()
                img.save(image_buffer, format='JPEG')
                file_extension = 'jpg'

            elif content_type.startswith('image/png'):
                img = Image.open(BytesIO(logo_response.content))
                image_buffer = BytesIO()
                img.save(image_buffer, format='PNG')
                file_extension = 'png'

            elif content_type.startswith('image/svg'):
                svg_content = logo_response.content
                svg_image = svglib.svg2rlg(io.StringIO(svg_content.decode('utf-8')))
                png_image = BytesIO()
                svglib.renderPM.drawToFile(svg_image, png_image, fmt="PNG")
                image_buffer = BytesIO(png_image.getvalue())
                file_extension = 'png'

    
            else:
                print(f"Unsupported image content type from logo URL: {content_type}")
                return None

            logo_file = InMemoryUploadedFile(
                file=image_buffer,
                field_name=None,
                name=f"{symbol}_{type}.{file_extension}",
                content_type=f'image/{file_extension}',
                size=image_buffer.tell(),
                charset=None
            )
            print("icon added succesfully")
            return logo_file
        else:
            print(f"Failed to download logo. Status Code: {logo_response.status_code}")

    except Exception as e:
        print(f"Error processing logo for: {e}")



def fetch_and_store_stock_assets():
    base_url = "https://api.polygon.io/v3/reference/tickers"
    api_key = "mPPslHGjobijJVWn8R03vFPREPTiTZSW"  # Replace with your actual API key

    # Other variables
    stocks_symbols = [
        "AAPL", "NVDA", "AMZN", "F", "BAC", "RIVN", "SOFI", "NU", "LCID", "VALE",
        "T", "GOOGL", "BABA", "COIN", "XPEV", "PFE", "SNAP", "ITUB", "SBSW", "UBER",
        "ABEV", "XOM", "MSFT", "CCL", "M", "GOOG", "YMM", "BEKE", "JWN", "RIG", "CSCO",
        "SE", "GRAB", "AGNC", "CSX", "GOLD", "PCG", "GM", "PYPL", "AFRM", "WBD", "LYFT",
        "VZ", "KGC",  "GSAT", "AI", "CIG", "WFC", "ET", "CNHI", "SQ", "BCS", "BMY", "SHOP",
        "TSLA", "MARA", "PLTR", "LU", "NIO", "RIOT", "BBD", "PLUG", "TAL", "PBR", 
        "DNA", "ARM", "KMI", "C", "JD", "CMCSA", "SWN", "NEM", "DIS", "META",
        "PDD",
    ]

    # Iterate through symbols
    for symbol in reversed(stocks_symbols):
        time.sleep(120)  # Wait for 2 seconds before making the next API call
        endpoint_url = f"{base_url}/{symbol}?apiKey={api_key}"
        response = requests.get(endpoint_url)
        print(response)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", {})
            print(data)
            name = results.get("name", "")
            market_cap = results.get("market_cap", 0)
            description = results.get("description", "")
            homepage_url = results.get("homepage_url", "")
            #logo_url = results.get("branding", {}).get("logo_url", "")
            icon_url = results.get("branding", {}).get("icon_url", "")
            #logo_url_key = f"{logo_url}?apiKey={api_key}"
            icon_url_key = f"{icon_url}?apiKey={api_key}"
            #logo = download_and_save_logo(logo_url_key, symbol, "logo")
            icon = download_and_save_logo(icon_url_key, symbol, "icon")
            address1 = results.get("address", {}).get("address1", "")
            city = results.get("address", {}).get("city", "")
            state = results.get("address", {}).get("state", "")
            country = results.get("address", {}).get("country", "")
            postal_code = results.get("address", {}).get("postal_code", "")
            list_date_str = results.get("list_date", "")
            list_date = datetime.strptime(list_date_str, '%Y-%m-%d').date()
            locale = results.get("locale", "")
            employees = results.get("total_employees", "")
            phone_number = results.get("phone_number", "")
            exchange = results.get("primary_exchange", "")
            ticker_type = results.get("type", "")

            # Create or update Asset object in the database
            asset, created = Assets.objects.update_or_create(
                symbol=symbol,
                defaults={
                    "name": name,
                    "market_cap": market_cap,
                    "description": description,
                    "website": homepage_url,
                    #"logo": logo,
                    "icon": icon,
                    "address": address1,
                    "city": city,
                    "state": state,
                    "country": country,
                    "postal_code": postal_code,
                    "list_date": list_date,
                    "locale": locale,
                    "employees": employees,
                    "phone_number": phone_number,
                    "exchange": exchange,
                    "ticker_type": ticker_type
                }
            )
            

            # Print some information
            if created:
                print(f"Created Asset: {asset}")
            else:
                print(f"Updated Asset: {asset}")
        else:
            print(f"Failed to fetch data for {symbol}. Status Code: {response.status_code}")

def clear_last():
    last_50_assets = Assets.objects.all()[0]
    last_50_assets_ids = last_50_assets.values_list('id', flat=True)
    Assets.objects.exclude(id__in=last_50_assets_ids).delete()



