
import pandas as pd
from binance.client import Client
import datetime as dt
import pandas as pd
# client configuration
api_key = '95Ogs30EZ740spnpcGG6fZQB89LErkAPaPIT5EazoweBERJ0DxBswnQKp1WVxLpD'
api_secret = 'iTRlZSdRBkdOaE3yzapcEzxfqaevljVzUdHfqQm2lcvlP75U62seswVIefXY2wn3'

client = Client('api_key', 'api_secret')
pair_list = client.get_exchange_info()
pairs = []
quoteAsset = []
baseAsset = []
for s in pair_list['symbols']:
    quoteAsset.append(s['quoteAsset'])
    baseAsset.append(s['baseAsset'])
    pairs.append(s['symbol'])
df = pd.DataFrame()
df['Trading-Pairs'] = pairs
df['Base-Asset'] = baseAsset
df['Quote-Asset'] = quoteAsset
df.to_csv("/Users/pasitapio/Downloads/trading_pairs.csv")
print(df)
