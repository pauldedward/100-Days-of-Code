import requests
import os
from twilio.rest import Client 
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID") 
auth_token = os.getenv("TWILIO_AUTH_TOKEN") 
client = Client(account_sid, auth_token) 

alpha_vantage_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + STOCK + "&apikey=" + stock_api_key

news_api_url = "https://newsapi.org/v2/everything?q=" + COMPANY_NAME +"&pageSize=3"+ "&apiKey=" + news_api_key

response = requests.get(alpha_vantage_url)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
today_data = list(data.items())[0]
yesterday_data = list(data.items())[1]

today_closing_price = float(today_data[1]['4. close'])
yesterday_closing_price = float(yesterday_data[1]['4. close'])
difference = today_closing_price - yesterday_closing_price
difference_percentage = abs(difference) / yesterday_closing_price * 100

if difference_percentage > 5:
    news_response = requests.get(news_api_url)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    
    messages = []
    for article in news_data:
        messages.append({'title':article['title'], 'description':article['description']})
        
    if difference > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    
    for m in messages:
        messageBody = f"\n{STOCK}: {symbol}{abs(difference_percentage)}%\nHeadline: {m['title']}\nBrief: {m['description']}"
        message = client.messages.create(  
                                messaging_service_sid='MG4d6f28736aa22d8bdf50c27d550e5b9c', 
                                body=messageBody,      
                                to='+918883336601' 
                            )
        print(f'{message.sid} sent')


