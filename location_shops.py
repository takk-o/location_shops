import settings
import googlemaps
import pandas as pd
from pathlib import Path

# Google Maps Web Services APIs Client取得
API_KEY = settings.key
gmaps_cl = googlemaps.Client(key=API_KEY)
# 指定場所のジオコード取得
place = input('Location: ')
geo_cd = gmaps_cl.geocode(place)
location = geo_cd[0]['geometry']['location']
# 検索キーワードを指定
keyword = input('keyword: ')
# 指定場所から半径1kmでkeywordに該当する店舗を検索
shops = gmaps_cl.places_nearby(location=location, radius=1000, keyword=keyword + ' 店舗')
# 店舗詳細情報(id,、名前、住所、電話番号、URL)を取得
shop_details = list()
for shop in shops['results']:
    place_id = shop['place_id']
    fields = ['place_id', 'name', 'formatted_address', 'formatted_phone_number', 'website']
    language = 'ja'
    shop_details.append(gmaps_cl.place(place_id, fields=fields, language=language)['result'])
df = pd.DataFrame(shop_details)
df = df.set_index('place_id')
df = df[['name', 'formatted_address', 'formatted_phone_number', 'website']]

# 出力フォルダの準備
out_fd = Path('output')
out_fd.mkdir(exist_ok=True)
# 取得情報をexcelに出力
out_fl = out_fd.joinpath('shopdata.xlsx')
df.to_excel(out_fl, sheet_name=place + '_' + keyword, header=['名前', '住所', '電話番号', 'URL'], index_label='ID')