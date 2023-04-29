import requests
from scrapy.http import HtmlResponse
from utils import cookies, headers, params, convert_list_of_dicts_to_csv



# hotel_urls = [
#     "https://www.marriott.com/en-us/hotels/ewrcp-courtyard-paramus/",
#     "https://www.marriott.com/en-us/hotels/ewrsb-marriott-saddle-brook/"
#     "https://www.marriott.com/en-us/hotels/ewrgp-teaneck-marriott-at-glenpointe/",
#     "https://www.marriott.com/en-us/hotels/ewrsr-residence-inn-saddle-river",
#     "https://www.marriott.com/en-us/hotels/ewrew-element-new-york-wood-ridge",
# ]


data = []
rate_url = "https://www.marriott.com/reservation/rateListMenu.mi"


response = requests.get(rate_url, headers=headers, cookies=cookies, params=params)

print(response.status_code)

html = HtmlResponse(url=rate_url, body=response.text, encoding="utf-8")

room_list = html.xpath('//*[@class="l-room-type-category-section"]/div').extract()

# finding out json data
# json_finder = html.xpath('//*[@id="tab0"]/div[2]/@data-ers4-room-list').extract()

# print(json_finder)

for i, room in enumerate(room_list):
    checkin = html.xpath('//*[@id="staydates"]/a/div[2]/span[1]/text()').extract_first()
    checkout = html.xpath(
        '//*[@id="staydates"]/a/div[2]/span[3]/text()'
    ).extract_first()
 
    room_name = html.xpath(
        f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[1]/div[1]/h3/text()'
    ).extract_first()
    rates = html.xpath(
        f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div'
    ).extract()
    for j, rate in enumerate(rates):
        rate_name = html.xpath(
            f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[1]/div[1]/h3/text()'
        ).extract_first()
        price = html.xpath(
            f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/span[1]/text()'
        ).extract_first()
        currency = html.xpath(
            f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/span[2]/text()'
        ).extract_first()
        data.append(
            {
                "checkin": checkin,
                "checkout": checkout,
                "roomname": room_name.strip(),
                "ratename": rate_name.strip(),
                "StayTotalwTaxes": price.strip(),
                "currency": currency,
            }
        )
        # print(f"{rate_name} for room {room_name} has price {price}/{currency}")

print(len(room_list))

print(data)

convert_list_of_dicts_to_csv(data)




