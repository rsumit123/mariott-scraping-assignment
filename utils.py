import requests
import pandas as pd


def convert_list_of_dicts_to_csv(data):
    """Takes a list of dictionaries and returns a csv file"""

    df = pd.DataFrame(data, columns=data[0].keys())
    df.to_csv("output/result.csv")



cookies = {
    '_rti': '927141D8-1F64-5D42-82B3-03F867EE0F90',
    'MI_Visitor': '9A4430E2-F3F9-5498-8A72-6FB5BBAAF78F',
    'dtCookie': 'v_4_srv_3_sn_C25554306F150B54E343DDE8DCE8892B_perc_100000_ol_0_mul_1_app-3A220110cf75551a30_1_rcs-3Acss_0',
    'x-mi-tag': 'rel-R23.4.4',
    'PIM-SESSION-ID': 'oaE6f65NhX9qoVrw',
    'rxVisitor': '1682681159421LU4JFH1A9AQGFSIDPUSVSLUN9VLNFQCT',
    'at_check': 'true',
    'usprivacy': '1---',
    'AMCVS_664516D751E565010A490D4C%40AdobeOrg': '1',
    's_cc': 'true',
    '_gcl_au': '1.1.1232819711.1682681161',
    '_fbp': 'fb.1.1682681161121.270256986',
    '_scid': '1ef817be-03d4-4091-86bb-9ed4c7864e2c',
    '_cls_v': '8d8341ae-c396-44a3-836e-10081554bb86',
    '_cls_s': '80948c1a-0682-4db3-9a82-53ee11c03401:0',
    'mdLogger': 'false',
    'kampyle_userid': 'bce4-787a-65e4-3e60-8f72-cfaf-bf52-22b5',
    'aam_uuid': '26683682597873442090454440834010657667',
    'demdex': '26683682597873442090454440834010657667',
    '_sctr': '1%7C1682620200000',
    '_pin_unauth': 'dWlkPVptTTRORGM0WVRFdE5qaGhPQzAwTlRWaExXRmxOVFF0TURjeE16YzVNVGczWTJJMA',
    '_sfid_baed': '{%22anonymousId%22:%22b7c0c6a25100bd4a%22%2C%22consents%22:[]}',
    'OneTrustWPCCPAGoogleOptOut': 'false',
    'MarriottOrigin': 'B',
    'BVBRANDID': '0a7db6bd-e92f-4785-b258-7ca120ff49ac',
    'BVImplmain_site': '14883',
    'tntId': '9A4430E2-F3F9-5498-8A72-6FB5BBAAF78F.34_0',
    'F8eh4Hwq': 'A9RixciHAQAAcik3cJSOkstRUmkEug5vDtGSaH9dsS8goMlIdqCIIJ_fkr1yAXX_82yuchZ2wH8AAOfvAAAAAA',
    'akacd_phoenix': '3860153391~rv=13~id=9cb6788ea902367f51adb0e50f2dcc09',
    'exitIntentShown': 'true',
    '__lt__cid': '947469ea-48b1-4cf7-a0c3-460a99910c04',
    'MI_SITE': 'prod16',
    '54101a7964dcdb9dcb7d4ee99752c5ea': 'e9212572c93b9f470447d751a2a3fb59',
    'a57b2616814e0f1487309dd765f09aac': '06ef86ae5a5ff130910bba2d3ca1ddbf',
    'lastUserEvent': '{"id":"","class":"mfp-close","text":"Close","dataAttr":{},"event_type":"click","event_data":{"timeStamp":34802,"metaKey":false,"namespace":"","pageX":1303,"pageY":489}}',
    'ln_or': 'eyIzNjA1NzIiOiJkIn0%3D',
    'sessionID': '927141D8-1F64-5D42-82B3-03F867EE0F90',
    'AKA_A2': 'A',
    'bm_mi': '8A42B0DBC16AF3F82DB7985A7603E4AF~YAAQLrYRYC3y9aKHAQAAs89VzRNH1z0JH5VlTJtFNmqqSf+bK6xS6WNNxj4B2cPYb/iTJRh2kSwkhSf5nbxJPU10t0dMlzm1ZieMY0Tf91NEZ6YtSSSUxr3sWlpfLqooqmunwNONU4BPyfgSbF2fRRfGwTIURQ1UtkX/iKCE9qL28Pz+RzA68HiF2HAm7MF4llzU/Bh1/Y3TyiqQIO4kQAmeIj6n6qalttM7PWtn2LYUooX7l0nPKiqFsxd7HzCnW30cNm/mEMO47QzTm8kB/7vJfj6p/MPktmIdTZhqxPzhceCp7+2oHutyTGMl4OqwaXBwKPiwWHo5dwcbscEqjdSehiWgJcePsIk=~1',
    'AMCV_664516D751E565010A490D4C%40AdobeOrg': '-1124106680%7CMCMID%7C26935551056128264240443854515239681514%7CMCAAMLH-1683381968%7C12%7CMCAAMB-1683381968%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1682784368s%7CNONE%7CvVersion%7C5.2.0',
    'ak_bmsc': 'ABC4CA2C3A6F53D58F7FBB9CB5BFAD96~000000000000000000000000000000~YAAQLrYRYIby9aKHAQAABuJVzRMIeMqMETRJPQZrGIvypYP2dsFPcmMp2NBnrq3N72mEdiLkRpM1SD7mI3f0fl74fhRvtARIyaORFYp+wlpLM++UF1rTTwfOc973sRds6aKvEbrelkMFSNxcRjZJmplnLYTMRPImzfhQD5MCyBLKcUk1raA0ajQ12O/BiCENESa9h8DQLXUxF2k/znEaE2N7h9757LpLdWfbyT6fDsctfrfjQm6JTDhH9bJ1cOo7+3YE6QZZxZhATP3T0FmJDRwT2y/auUkvLudVwz2DXHd8Yrs7cmcNGjAwN2BFgosxST5glvFlnyWyN/AaoKsZlNnW9pWbGu6a3Txj9WA6GvBSQ302X23HRkgyfnDLvNxQRFILUU6NO2Yhk4iXjjEker7uULDMT7dSQjicSZ/fu4/PWKK3KiZ7ZlYint0hqHAGMhZmz6FLv09G',
    's_tbm': 'true',
    '_dpm_ses.be2e': '*',
    '_ga': 'GA1.2.170800548.1682777176',
    '_gid': 'GA1.2.1381339476.1682777176',
    'merchViewed': 'reservationAvailabilityFooterBanner-unlockYourStay1120|rlmFooterBanner-unlockYourStay1120|',
    '__lt__sid': '51253788-52fe5310',
    '96692dd177842ab0abc545b2793fa2cc': '1f0aa117a3dad0b54a776ebc979b192c',
    'bm_sz': '7CEDC99297BBDC66E5BBB23F3ABD4EE3~YAAQLrYRYH0F9qKHAQAAqc5XzRMbRbhgr34B/ooSnEAYriSqXcGyIXLgyZudNl0IgRcWa04gqvCH7oT4/lv+DJRD6Qmor15yN+UPD1eHtaZZgU9epytEhD7EIcOuP0e9E7ag1CQ+yCZYdLtNoLydcS5TocwEEVXKAE1w5bkmS2bikh/hFgZrzZp9VYajkOr2INsLBPwQ3NkSQ2MJ0TnfTFCX6LiSVXWawMNxbRD6AMYe1Hce6Nsf9k6BmE/WMtSi3Wa0bSopESW6hBIWUNaefRimnMkrfdrv9PqMzJoDkVt2lKjdHHCkA9iUdmY4iI5vB93LEQUJiLAp8WrSuQ==~3687222~3748659',
    'BVBRANDSID': '07d8c954-8f5e-4480-8914-bb85da0574c8',
    'AWSELB': 'B52949030425731B930EB8066EE6D92E09A9264F1C2900DE0B14996FDEDD1FCD68A13205C6C12D29C878311FA0FAE4568E15853E49F379A27D338141935C538A12D16D9C7B',
    'AWSELBCORS': 'B52949030425731B930EB8066EE6D92E09A9264F1C2900DE0B14996FDEDD1FCD68A13205C6C12D29C878311FA0FAE4568E15853E49F379A27D338141935C538A12D16D9C7B',
    'kampyleUserSession': '1682777301357',
    'kampyleUserSessionsCount': '8',
    's_sq': '%5B%5BB%5D%5D',
    'JVMID': 'aries-play-reservation-app-green-35-kmnkn',
    'e37a5a7b342e64476a0b7920f4e28414': '0cb6d4bbbe67d75211c303f69bbcd68f',
    'ZMz286iJ': 'f%3DA2vhWc2HAQAAqG6b-fXOphPcINt1MtjSfebShNSDUNSewefA-Y8z0DJFR4rtAWrPGCmuchZ2wH8AAOfvAAAAAA%253D%253D%26b%3D2vteth%26c%3DAAA7UM2HAQAA-C81M_j-FioJxUyER-jWqrqXbv-FOhtXykrALabzVwHZpIKk%26d%3DABYAgACAAIAAgACAAQCm81cB2aSCpAAAAABrKlY4ABrI4CRjFRzkGOlQqmVEH8k%26z%3Dq%26a%3Dn2TTH86fdHEZGdKjKYVJFaf24T78',
    'dtSa': '-',
    'mbox': 'PC#ecdb34bae8b941079ef5d0627b69f648.31_0#1746022234|session#30052c1977af4c46bb681c198083a4ec#1682779029',
    '_evga_0a63': '{%22uuid%22:%22b7c0c6a25100bd4a%22%2C%22puid%22:%22pXxHZN-geyDQgNRng5tcSDgx8ZEntShQAFDxntI5oGo-26oi964GNN-oWMy8aS1FDvN0sCc_mXB1LOJqVgw0sQ%22%2C%22affinityId%22:%220PW%22}',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Apr+29+2023+19%3A40%3A34+GMT%2B0530+(India+Standard+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=81cf46d2-0671-4cc2-9eee-3c2d0552ae7d&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1%2C6%3A1&AwaitingReconsent=false',
    'kampyleSessionPageCounter': '4',
    '_uetsid': '744c0be0e5b711eda6d355552a27160b',
    '_uetvid': '744c3620e5b711edb9c85d7fbcf2fc78',
    '7f43ca11c4dc21bb60196804ca3a8e4a': '171128ab8ad0e7af9a770d35ba43bfb7',
    '_dpm_id.be2e': '3eef4fbb-4630-4da1-b97e-3b53bddf1adc.1682681162.6.1682777435.1682768097.5efce9a1-c580-4496-be2d-636e89a90c58',
    '_scid_r': '1ef817be-03d4-4091-86bb-9ed4c7864e2c',
    '_derived_epik': 'dj0yJnU9emJuRGNCSThpUjhhY2JISFJrWVVlTDZ4Y1FiLS1vRk0mbj13UUJfLXR1eUhRTFE2dnJhZ0UtUW1RJm09MSZ0PUFBQUFBR1JOSlYwJnJtPTEmcnQ9QUFBQUFHUk5KVjAmc3A9NQ',
    '855f89e12f62018a955cfa5e05012eda': '0e2ebf9583723e596f6c933c6a333a14',
    'rxvt': '1682779297871|1682777296427',
    'dtPC': '3$377432416_338h-vNRUUHVOCPKRJAMFTGMPAHLNWQRPGQVSO-0e0',
    '_abck': '9EAF2BCAB1C52058E3815F6A1FD0F1B1~0~YAAQLrYRYN8T9qKHAQAAru1azQmnsHgmZzbyzI3dk5EbihRbminRZEGFgVAFdlWSjwOmVyJMIKffsSian/GsFn2gWW/uPXzkJliPqqGAoaXDMBOfkHrhnzBkH2Zv1/itj06kPtwzldxsUCaz7S8FoqJP/PW6RFaGvFWx5lMo0M0yBy/JFo3hexzWo5sA3YCdQsCcvLEBiqzKd+dx+QNf2txrlj9hrqkVfyqtba+LVjDIEPTZ8bCKRR3GoV4B5sE+bImXrR43ye0i9EBZV9bl8bTsqYFdRTeP4aKHFCWKOk5reom1TeF5Scuwzl6GV7r1FZj67D2ZwuusuLF/ZKAX3gyMrMtaEQNMzCUrusctVwPAhLDzL1W5jMZKbdHHFcNn~-1~-1~-1',
    'bm_sv': '202999A3059393FD246900F10311F13C~YAAQLrYRYOAT9qKHAQAAru1azRPITt+wShpTMB68dAsP6QIeuqAUBKRIELm3eyVWxqCB5mNCajkvgV+Ail/bOxpXRSHs1vb9G+WkGY3/chTX0/SAkRn3rfT0jc/3ySNWPO/ycIfQaNvUkRZ0QcWso9OxdgdKqo/dKdYdWxIPsJOnLET7IxpQKMrndho4Go/ZhntN8tzUSFb7257fdx27yruBU9NDPwhu5qeIF3wUoI9J5FgpvG+Aiheg8kkF93iuJovI~1',
    'dtLatC': '5',
}

headers = {
    'authority': 'www.marriott.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6,en-GB;q=0.5,en-US;q=0.4,fr;q=0.3',
    'cache-control': 'max-age=0',
    # 'cookie': '_rti=927141D8-1F64-5D42-82B3-03F867EE0F90; MI_Visitor=9A4430E2-F3F9-5498-8A72-6FB5BBAAF78F; dtCookie=v_4_srv_3_sn_C25554306F150B54E343DDE8DCE8892B_perc_100000_ol_0_mul_1_app-3A220110cf75551a30_1_rcs-3Acss_0; x-mi-tag=rel-R23.4.4; PIM-SESSION-ID=oaE6f65NhX9qoVrw; rxVisitor=1682681159421LU4JFH1A9AQGFSIDPUSVSLUN9VLNFQCT; at_check=true; usprivacy=1---; AMCVS_664516D751E565010A490D4C%40AdobeOrg=1; s_cc=true; _gcl_au=1.1.1232819711.1682681161; _fbp=fb.1.1682681161121.270256986; _scid=1ef817be-03d4-4091-86bb-9ed4c7864e2c; _cls_v=8d8341ae-c396-44a3-836e-10081554bb86; _cls_s=80948c1a-0682-4db3-9a82-53ee11c03401:0; mdLogger=false; kampyle_userid=bce4-787a-65e4-3e60-8f72-cfaf-bf52-22b5; aam_uuid=26683682597873442090454440834010657667; demdex=26683682597873442090454440834010657667; _sctr=1%7C1682620200000; _pin_unauth=dWlkPVptTTRORGM0WVRFdE5qaGhPQzAwTlRWaExXRmxOVFF0TURjeE16YzVNVGczWTJJMA; _sfid_baed={%22anonymousId%22:%22b7c0c6a25100bd4a%22%2C%22consents%22:[]}; OneTrustWPCCPAGoogleOptOut=false; MarriottOrigin=B; BVBRANDID=0a7db6bd-e92f-4785-b258-7ca120ff49ac; BVImplmain_site=14883; tntId=9A4430E2-F3F9-5498-8A72-6FB5BBAAF78F.34_0; F8eh4Hwq=A9RixciHAQAAcik3cJSOkstRUmkEug5vDtGSaH9dsS8goMlIdqCIIJ_fkr1yAXX_82yuchZ2wH8AAOfvAAAAAA; akacd_phoenix=3860153391~rv=13~id=9cb6788ea902367f51adb0e50f2dcc09; exitIntentShown=true; __lt__cid=947469ea-48b1-4cf7-a0c3-460a99910c04; MI_SITE=prod16; 54101a7964dcdb9dcb7d4ee99752c5ea=e9212572c93b9f470447d751a2a3fb59; a57b2616814e0f1487309dd765f09aac=06ef86ae5a5ff130910bba2d3ca1ddbf; lastUserEvent={"id":"","class":"mfp-close","text":"Close","dataAttr":{},"event_type":"click","event_data":{"timeStamp":34802,"metaKey":false,"namespace":"","pageX":1303,"pageY":489}}; ln_or=eyIzNjA1NzIiOiJkIn0%3D; sessionID=927141D8-1F64-5D42-82B3-03F867EE0F90; AKA_A2=A; bm_mi=8A42B0DBC16AF3F82DB7985A7603E4AF~YAAQLrYRYC3y9aKHAQAAs89VzRNH1z0JH5VlTJtFNmqqSf+bK6xS6WNNxj4B2cPYb/iTJRh2kSwkhSf5nbxJPU10t0dMlzm1ZieMY0Tf91NEZ6YtSSSUxr3sWlpfLqooqmunwNONU4BPyfgSbF2fRRfGwTIURQ1UtkX/iKCE9qL28Pz+RzA68HiF2HAm7MF4llzU/Bh1/Y3TyiqQIO4kQAmeIj6n6qalttM7PWtn2LYUooX7l0nPKiqFsxd7HzCnW30cNm/mEMO47QzTm8kB/7vJfj6p/MPktmIdTZhqxPzhceCp7+2oHutyTGMl4OqwaXBwKPiwWHo5dwcbscEqjdSehiWgJcePsIk=~1; AMCV_664516D751E565010A490D4C%40AdobeOrg=-1124106680%7CMCMID%7C26935551056128264240443854515239681514%7CMCAAMLH-1683381968%7C12%7CMCAAMB-1683381968%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1682784368s%7CNONE%7CvVersion%7C5.2.0; ak_bmsc=ABC4CA2C3A6F53D58F7FBB9CB5BFAD96~000000000000000000000000000000~YAAQLrYRYIby9aKHAQAABuJVzRMIeMqMETRJPQZrGIvypYP2dsFPcmMp2NBnrq3N72mEdiLkRpM1SD7mI3f0fl74fhRvtARIyaORFYp+wlpLM++UF1rTTwfOc973sRds6aKvEbrelkMFSNxcRjZJmplnLYTMRPImzfhQD5MCyBLKcUk1raA0ajQ12O/BiCENESa9h8DQLXUxF2k/znEaE2N7h9757LpLdWfbyT6fDsctfrfjQm6JTDhH9bJ1cOo7+3YE6QZZxZhATP3T0FmJDRwT2y/auUkvLudVwz2DXHd8Yrs7cmcNGjAwN2BFgosxST5glvFlnyWyN/AaoKsZlNnW9pWbGu6a3Txj9WA6GvBSQ302X23HRkgyfnDLvNxQRFILUU6NO2Yhk4iXjjEker7uULDMT7dSQjicSZ/fu4/PWKK3KiZ7ZlYint0hqHAGMhZmz6FLv09G; s_tbm=true; _dpm_ses.be2e=*; _ga=GA1.2.170800548.1682777176; _gid=GA1.2.1381339476.1682777176; merchViewed=reservationAvailabilityFooterBanner-unlockYourStay1120|rlmFooterBanner-unlockYourStay1120|; __lt__sid=51253788-52fe5310; 96692dd177842ab0abc545b2793fa2cc=1f0aa117a3dad0b54a776ebc979b192c; bm_sz=7CEDC99297BBDC66E5BBB23F3ABD4EE3~YAAQLrYRYH0F9qKHAQAAqc5XzRMbRbhgr34B/ooSnEAYriSqXcGyIXLgyZudNl0IgRcWa04gqvCH7oT4/lv+DJRD6Qmor15yN+UPD1eHtaZZgU9epytEhD7EIcOuP0e9E7ag1CQ+yCZYdLtNoLydcS5TocwEEVXKAE1w5bkmS2bikh/hFgZrzZp9VYajkOr2INsLBPwQ3NkSQ2MJ0TnfTFCX6LiSVXWawMNxbRD6AMYe1Hce6Nsf9k6BmE/WMtSi3Wa0bSopESW6hBIWUNaefRimnMkrfdrv9PqMzJoDkVt2lKjdHHCkA9iUdmY4iI5vB93LEQUJiLAp8WrSuQ==~3687222~3748659; BVBRANDSID=07d8c954-8f5e-4480-8914-bb85da0574c8; AWSELB=B52949030425731B930EB8066EE6D92E09A9264F1C2900DE0B14996FDEDD1FCD68A13205C6C12D29C878311FA0FAE4568E15853E49F379A27D338141935C538A12D16D9C7B; AWSELBCORS=B52949030425731B930EB8066EE6D92E09A9264F1C2900DE0B14996FDEDD1FCD68A13205C6C12D29C878311FA0FAE4568E15853E49F379A27D338141935C538A12D16D9C7B; kampyleUserSession=1682777301357; kampyleUserSessionsCount=8; s_sq=%5B%5BB%5D%5D; JVMID=aries-play-reservation-app-green-35-kmnkn; e37a5a7b342e64476a0b7920f4e28414=0cb6d4bbbe67d75211c303f69bbcd68f; ZMz286iJ=f%3DA2vhWc2HAQAAqG6b-fXOphPcINt1MtjSfebShNSDUNSewefA-Y8z0DJFR4rtAWrPGCmuchZ2wH8AAOfvAAAAAA%253D%253D%26b%3D2vteth%26c%3DAAA7UM2HAQAA-C81M_j-FioJxUyER-jWqrqXbv-FOhtXykrALabzVwHZpIKk%26d%3DABYAgACAAIAAgACAAQCm81cB2aSCpAAAAABrKlY4ABrI4CRjFRzkGOlQqmVEH8k%26z%3Dq%26a%3Dn2TTH86fdHEZGdKjKYVJFaf24T78; dtSa=-; mbox=PC#ecdb34bae8b941079ef5d0627b69f648.31_0#1746022234|session#30052c1977af4c46bb681c198083a4ec#1682779029; _evga_0a63={%22uuid%22:%22b7c0c6a25100bd4a%22%2C%22puid%22:%22pXxHZN-geyDQgNRng5tcSDgx8ZEntShQAFDxntI5oGo-26oi964GNN-oWMy8aS1FDvN0sCc_mXB1LOJqVgw0sQ%22%2C%22affinityId%22:%220PW%22}; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+29+2023+19%3A40%3A34+GMT%2B0530+(India+Standard+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=81cf46d2-0671-4cc2-9eee-3c2d0552ae7d&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1%2C6%3A1&AwaitingReconsent=false; kampyleSessionPageCounter=4; _uetsid=744c0be0e5b711eda6d355552a27160b; _uetvid=744c3620e5b711edb9c85d7fbcf2fc78; 7f43ca11c4dc21bb60196804ca3a8e4a=171128ab8ad0e7af9a770d35ba43bfb7; _dpm_id.be2e=3eef4fbb-4630-4da1-b97e-3b53bddf1adc.1682681162.6.1682777435.1682768097.5efce9a1-c580-4496-be2d-636e89a90c58; _scid_r=1ef817be-03d4-4091-86bb-9ed4c7864e2c; _derived_epik=dj0yJnU9emJuRGNCSThpUjhhY2JISFJrWVVlTDZ4Y1FiLS1vRk0mbj13UUJfLXR1eUhRTFE2dnJhZ0UtUW1RJm09MSZ0PUFBQUFBR1JOSlYwJnJtPTEmcnQ9QUFBQUFHUk5KVjAmc3A9NQ; 855f89e12f62018a955cfa5e05012eda=0e2ebf9583723e596f6c933c6a333a14; rxvt=1682779297871|1682777296427; dtPC=3$377432416_338h-vNRUUHVOCPKRJAMFTGMPAHLNWQRPGQVSO-0e0; _abck=9EAF2BCAB1C52058E3815F6A1FD0F1B1~0~YAAQLrYRYN8T9qKHAQAAru1azQmnsHgmZzbyzI3dk5EbihRbminRZEGFgVAFdlWSjwOmVyJMIKffsSian/GsFn2gWW/uPXzkJliPqqGAoaXDMBOfkHrhnzBkH2Zv1/itj06kPtwzldxsUCaz7S8FoqJP/PW6RFaGvFWx5lMo0M0yBy/JFo3hexzWo5sA3YCdQsCcvLEBiqzKd+dx+QNf2txrlj9hrqkVfyqtba+LVjDIEPTZ8bCKRR3GoV4B5sE+bImXrR43ye0i9EBZV9bl8bTsqYFdRTeP4aKHFCWKOk5reom1TeF5Scuwzl6GV7r1FZj67D2ZwuusuLF/ZKAX3gyMrMtaEQNMzCUrusctVwPAhLDzL1W5jMZKbdHHFcNn~-1~-1~-1; bm_sv=202999A3059393FD246900F10311F13C~YAAQLrYRYOAT9qKHAQAAru1azRPITt+wShpTMB68dAsP6QIeuqAUBKRIELm3eyVWxqCB5mNCajkvgV+Ail/bOxpXRSHs1vb9G+WkGY3/chTX0/SAkRn3rfT0jc/3ySNWPO/ycIfQaNvUkRZ0QcWso9OxdgdKqo/dKdYdWxIPsJOnLET7IxpQKMrndho4Go/ZhntN8tzUSFb7257fdx27yruBU9NDPwhu5qeIF3wUoI9J5FgpvG+Aiheg8kkF93iuJovI~1; dtLatC=5',
    'referer': 'https://www.marriott.com/reservation/rateListMenu.mi?defaultTab=prepay',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

params = {
    'defaultTab': 'prepay',
    'showFullPrice': 'true',
}

response = requests.get('https://www.marriott.com/reservation/rateListMenu.mi', params=params, cookies=cookies, headers=headers)
