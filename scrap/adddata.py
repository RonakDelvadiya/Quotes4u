import json
from QuotesModel.models import *
import csv
from django.utils.encoding import smart_str, smart_unicode
import  ast

sourceFile = open("quotes.json","rU")
json_data = json.load(sourceFile)
outputFile = open("quotes.csv" , "w")
outputWriter = csv.writer(outputFile)
featurelist = []
list1 = []
print type(json_data)
for data in json_data:
    quote = data['quote']
    author = data['author']
    category = data['category']
    
    for offer in products['products'][0]['offers']:
        seller_id = offer['seller_id'] if 'seller_id' in offer.keys() else ""
        seller = offer['seller'] if 'seller' in offer.keys() else ""
        seller = u""+seller+""
        availability = offer['availability'] if 'availability' in offer.keys() else ""
        price = offer['price'] if 'price' in offer.keys() else ""
        condition = offer['condition'] if 'condition' in offer.keys() else ""
        shipping = offer['shipping'] if 'shipping' in offer.keys() else ""
        currency = offer['currency'] if 'currency' in offer.keys() else ""
        sellerratings_number = offer['sellerratings_number'] if 'sellerratings_number' in offer.keys() else ""
        sellername = offer['sellername'] if 'sellername' in offer.keys() else ""
        
        sellername = sellername.encode('utf-8')
        sellerrating_scale = offer['sellerrating_scale'] if 'sellerrating_scale' in offer.keys() else ""
        x = products['products'][0]['images'] 
        image = ", ".join(map(str, x))
        sku = products['products'][0]['sku'] 
        variation_id = products['products'][0]['variation_id']  
        name = products['products'][0]['name']
        name = u""+name+"" 
        try:
            des = products['products'][0]['description']
            description = u""+des+"" 
        except:
            description = ""
        try:
            brand = products['products'][0]['brand']
            brand =  u""+brand+"" 
        except:
            brand = ""
        try:
            color = products['products'][0]['color']
            color =  u""+color+""
        except:
            color = ""
        created_at = products['products'][0]['created_at'] 
        updated_at = products['products'][0]['updated_at'] 
        try:
            size = products['products'][0]['size']
            size = u""+size+""
        except:
            size = ""

        try:
            model = products['products'][0]['model']
            model = model.encode('utf-8')
        except:
            model = ""

        try:
            upc = products['products'][0]['upc']
            upc = u""+upc+""
        except:
            upc = ""
        
        listprice_currency = products['products'][0]['listprice_currency']
        site = products['products'][0]['site']
        url = products['products'][0]['url']
        isactive = products['products'][0]['isactive']
        crumb = products['products'][0]['crumb']
        feature = products['products'][0]['features']
        feature = str(ast.literal_eval(json.dumps(feature)))

        csv_data = smart_str(seller),str(seller_id),availability,price,condition,shipping,currency,sellerrating_scale,sellerratings_number,sellername,model,smart_str(upc),sku,variation_id,smart_str(name),smart_str(description),smart_str(brand),smart_str(color),created_at,updated_at,smart_str(size),listprice_currency,site,url,isactive,crumb,image,feature
        outputWriter.writerow(csv_data)
sourceFile.close()
outputFile.close()




