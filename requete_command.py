import requests
import json 

url = "https://www.ubereats.com/_p/api/addMemberToDraftOrderV1"
headers = {
    "Host": "www.ubereats.com",
    "Cookie": "uev2.id.xp=55118ed6-7138-4ef8-9606-fc5cf9b0b666; dId=748393f1-e865-443b-9bb0-9151e1b37906; marketing_vistor_id=d3a93d19-cc32-455f-8d89-d9e60cd5a46a; uev2.loc=%7B%22latitude%22%3A45.89335007730314%2C%22longitude%22%3A6.122568547725675%2C%22address%22%3A%7B%22address1%22%3A%2228%20Faubourg%20des%20Balmettes%22%2C%22address2%22%3A%22%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%22%22%2C%22title%22%3A%2228%20Faubourg%20des%20Balmettes%22%2C%22subtitle%22%3A%22Annecy%2C%20Auvergne-Rh%C3%B4ne-Alpes%2C%2074000%22%2C%22uuid%22%3A%22%22%7D%2C%22reference%22%3A%22faf167e4-083f-b1f4-bdc6-09d7d81201b8%22%2C%22referenceType%22%3A%22uber_places%22%2C%22type%22%3A%22uber_places%22%2C%22addressComponents%22%3A%7B%22countryCode%22%3A%22%22%2C%22firstLevelSubdivisionCode%22%3A%22%22%2C%22city%22%3A%22%22%2C%22postalCode%22%3A%22%22%7D%7D; gclid=EAIaIQobChMI5JmIgJzYggMV5wIGAB3MWQJ1EAAYASAAEgKi4_D_BwE; gclsrc=aw.ds; uev2.gg=true; utm_medium=undefined; fm_conversion_id=undefined; utm_source=AdWords_Brand; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1700677133212%7Cconsent:true; _scid=6291efeb-2993-4eb2-9481-7e90c8d72089; _gac_UA-60706425-3=1.1700677134.EAIaIQobChMI5JmIgJzYggMV5wIGAB3MWQJ1EAAYASAAEgKi4_D_BwE; _fbp=fb.1.1700677134744.846760239; _gcl_aw=GCL.1700677135.EAIaIQobChMI5JmIgJzYggMV5wIGAB3MWQJ1EAAYASAAEgKi4_D_BwE; _gcl_dc=GCL.1700677135.EAIaIQobChMI5JmIgJzYggMV5wIGAB3MWQJ1EAAYASAAEgKi4_D_BwE; _gcl_au=1.1.782765575.1700677135; _yjsu_yjad=1700677134.3224ae68-3e72-4fd9-91d6-7bb76c6a70d8; _tt_enable_cookie=1; _ttp=4Vu13NBLLYO8IYcNujK0wZM-YhI; uev2.unregisteredUserUuid=5cd4d0d1-9851-5dfb-bbf9-122652817bc8; uev2.gosid=GOSID-9e8bc27f-0343-4553-8f8f-423159e71701; uev2.do=58d1dab9-9e7d-4ee9-b5f8-6a2e1561daf1; udi-id=COtvcvMvNDXR5Cb2caVSPUWQp+YHWdWDnB3cxfFQEwxiVMR0T630o81fihiL7KeZ58fTVMHdaUfIQJRDaC/K6+l8etLR6c0O+LszO6xwMfGxO75x497eaegq64s7DsU7h8PtbmyO6FNihqBiaoCOE3WD+RcH+7aiR3EGu9LHw34IwzU1417IiThfBjJQLqBkHH4URZcUe5uWi7OR13G87g==IS6bBHshT0//krpHs7vO9Q==QThuhc1V1raV+uE8k75vMp/tQ/PG2szsE/QzDqo0u/o=; uev2.diningMode=DELIVERY; mcd_restaurant=Brut Butcher; _uetvid=998de600896311eeac21ffb78d81c1c3; uev2.id.session=7fdec1e3-e7cc-447e-b78e-d975cb162e81; uev2.ts.session=1700764409177; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9fand0X3JwY19wcm90ZWN0aW9uX2V4cGlyZXNfYXRfbXMiOjE3MDA4NTA5MjAyMDAsIl9fand0X3JwY19wcm90ZWN0aW9uX3V1aWQiOiI5YmNkZTRhOS00ZmExLTQzODktYmUxMy1kNjNiYTM2Y2VhZDMiLCJfX2p3dF9ycGNfcHJvdGVjdGlvbl9jcmVhdGVkX2F0X21zIjoxNzAwNzY0NDA5MjAwfSwiaWF0IjoxNzAwNzY0NDEwLCJleHAiOjE3MDA4NTA4MTB9.2SR0JFgkTHYeaQqFyNyzZHEz1XSZLB5lMeCKv99bfdw; utag_main__sn=2; utag_main__se=1%3Bexp-session; utag_main__ss=1%3Bexp-session; utag_main__st=1700766326079%3Bexp-session; utag_main_ses_id=1700764526079%3Bexp-session; utag_main__pn=1%3Bexp-session; _userUuid=undefined; _scid_r=6291efeb-2993-4eb2-9481-7e90c8d72089; u.bdc=b87bbf29259f0de899ea94f3b6a673c9:NkzV4I6WEbiD+kGy:bqD8L+jBhhLnop+9+n2T+/LP7qLWnKEI6p0E7vReF2lbqkTS:rASG7/k+IxWJH7G4eYyG3g==; _gid=GA1.2.447229742.1700764561; _ga_P1RM71MPFP=GS1.1.1700764564.2.0.1700764564.60.0.0; _ga=GA1.1.1412892647.1700677134",  # Your complete cookie string here
    "Content-Length": "75",
    "Sec-Ch-Ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Content-Type": "application/json",
    "X-Uber-Client-Gitref": "d2eba94957a97374d00d68d2944d0c995bd0c99e",
    "X-Csrf-Token": "x",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Accept": "*/*",
    "Origin": "https://www.ubereats.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.ubereats.com/group-orders/6b92393a-4c3e-4fbc-af62-3acd31deb1db/join",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=1, i"
}

payload = {
    "draftOrderUuid": "671ea677-7f30-49ff-a05c-21e91b5e1dca",
    "nickname": "Remy"
}

response = requests.post(url, json=payload, headers=headers)

#print("Status code:", response.status_code)
#print("Response content:", response.text)
rep = response.text 

data = json.loads(rep)
status = data["status"]
uuid = data["data"]["uuid"]
cart_items = data["data"]["shoppingCart"]["items"]
price = 300
# Imprimer les informations extraites
print("Status:", status)
print("UUID:", uuid)
print("Cart Items:")
for item in cart_items:
    print("  - Title:", item["title"])
    if price == 300:
        price = int(item["price"])
    else:
        price += int(item["price"])
    print("    price:", item["price"])
    print("    Quantity:", item["quantity"])
    customizations = item.get("customizations", {})
    if customizations:
        print("    Customizations:")
        for customization_key, customization_values in customizations.items():
            for customization_value in customization_values:
                print("        Title:", customization_value["title"])
                print("        Quantity:", customization_value["quantity"])
                print (" Price:", customization_value["price"])
                price += customization_value["price"]
    print("finaly price", price)
                
    print("\n")
    
adress = data["data"]["deliveryAddress"]["address"]["title"]
postal = data["data"]["deliveryAddress"]["address"]["subtitle"]



print("✅ C'est tout bon ! Un cuisto viendra vers vous très prochainement Si vous souhaiter annuler votre commande, faites /close.")
print("\n")
print(f'📍 Adresse :{adress},{postal}')
print(f'💰 Montant à payer : {price} - 50% = {price // 2}')


#print("ID:", uuid)
