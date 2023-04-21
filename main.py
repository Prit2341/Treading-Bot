import time
from Engulfing import detect_bearish_engulfing,detect_bullish_engulfing
from Doji import is_doji
from Trend import Trend
from datetime import datetime
from BinanceAPI import buy_eth,sell_eth
from API import get_crypto_data
# #This is Mail Data That Give To the Seling And Buying_alert Function
# Sub = "BOT"
# Body_Selling = "Bot Call\nSell The ETH\nTake Profit selling Price + 20 ETHUSD"
# Body_Buying = "Bot Call\nBuy The ETH\nTake Profit Buying Price + 20ETHUSD"
# Email =  "pritmayani359@gmail.com"

#Checking the Conditon
Checking_Condition = []
#Making array for the storing 15 min data in array
Live_Data1 = []
#Second 15 minute data
Live_Data2 = []
Buy = []
sell = []
count = 0


while True:
    Time = datetime.now()
    Checking_Condition.clear()
    
    print("Start appending in the Checking List")
    for i in Live_Data1:
        Checking_Condition.append(i)
    print("Completed Appending in the Checking List")
    print("-------------------------------------------")
    Live_Data1.clear()
    
    print("Appending Data Stated")
    #Appedning the Data of the Live_Data1 from Live_Data2
    for i in Live_Data2:
        Live_Data1.append(i)    
    
    print("Appending Data Completed")
    print("-------------------------------------------")
    Live_Data2.clear()
    
    
    #Start Scarping
    print("Scarping started.")
    Data_Time = 0
    while (Data_Time <= 900):
        symbol = 'ETH'
        #Geting Crypto price from coinbase api
        get_crypto_data(symbol,'live')
        Data_Time += 1
        time.sleep(1)
    print("Scarping Completed")
    print("-------------------------------------------")
    
    
    if count >= 3:
        print(Live_Data1)
        print(Live_Data2)
        #Cheacking Candle doji or not
        price_bullish_engulfing = [
            {'close':Live_Data1[-1],'open':Live_Data1[0]},#for red Candle
            {'close':Live_Data1[0],'open':Live_Data1[-1]}#for green Candle
        ]
        price_bearish_engulfing = [
            {'close':Live_Data1[0],'open':Live_Data1[-1]},#for Green Candle
            {'close':Live_Data1[-1],'open':Live_Data1[0]}#for red Candle
        ]
        if detect_bullish_engulfing(price_bullish_engulfing) == len(detect_bullish_engulfing(price_bullish_engulfing)) == 2:
            buy_eth()
        elif (detect_bearish_engulfing(price_bearish_engulfing)) == 2:
            sell_eth()
    else:
        print("Pass Only")
        
   
    #For the Checking the Price
    count += 1
  
    
   