import requests
from scrapy.http import HtmlResponse
from utils import (
    params,
    get_payment_policy,
    convert_list_of_dicts_to_csv,
    find_price_before_tax,
    get_cancel_policy,
)
from headers_cookies_data import headers_cookie_dict


import json
from tqdm import tqdm


hotel_urls = [
    "https://www.marriott.com/en-us/hotels/ewrcp-courtyard-paramus/",
    "https://www.marriott.com/en-us/hotels/ewrsb-marriott-saddle-brook/",
    "https://www.marriott.com/en-us/hotels/ewrgp-teaneck-marriott-at-glenpointe/",
    "https://www.marriott.com/en-us/hotels/ewrsr-residence-inn-saddle-river/",
    "https://www.marriott.com/en-us/hotels/ewrew-element-new-york-wood-ridge/",
]


# iterating through all hotels
for hotel_url in hotel_urls:
    data = []
    rate_url = "https://www.marriott.com/reservation/rateListMenu.mi"

    print(f"Now scraping for {hotel_url} ....")

    hotel_code = hotel_url.split("en-us/hotels/")[1].split("-")[0]

    response = requests.get(
        rate_url,
        headers=headers_cookie_dict[hotel_url]["headers"],
        cookies=headers_cookie_dict[hotel_url]["cookies"],
        params=params,
    )

    # generating xpath tree

    html = HtmlResponse(url=rate_url, body=response.text, encoding="utf-8")

    # get all member elements

    room_list = html.xpath('//*[@class="l-room-type-category-section"]/div').extract()

    # finding out json data if available, many info can be accessed from this data

    try:
        json_finder = html.xpath(
            '//*[@id="tab0"]/div[2]/@data-ers4-room-list'
        ).extract_first()

        json_data = json.loads(json_finder)

        for rows in json_data:
            pass

    except Exception as e:
        print(e)
        pass

    for i, room in tqdm(enumerate(room_list), total=len(room_list)):
        checkin = html.xpath(
            '//*[@id="staydates"]/a/div[2]/span[1]/text()'
        ).extract_first()
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

            try:
                price = html.xpath(
                    f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/span[1]/text()'
                ).extract_first()

                price = price.replace(",", "")

                price = float(price)
            except:
                price = html.xpath(
                    f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/div/span[1]/text()'
                ).extract_first()

                price = price.replace(",", "")

                price = float(price)

            price_before_tax = find_price_before_tax(
                rate_url,
                hotel_url,
                [
                    f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/span[1]/text()',
                    f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/div/span[1]/text()',
                ],
            )

            currency = html.xpath(
                f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/span[2]/text()'
            ).extract_first()

            if currency is None or "night" not in currency:
                currency = currency = html.xpath(
                    f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/div/div/span[2]/text()'
                ).extract_first()

            availability = html.xpath(
                f'//*[@id="tab0"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[2]/div[1]/div/div/p/text()'
            ).extract_first()

            if availability is None:
                availability = "NA"

            des_text = html.xpath(
                f'//*[@id="tab1"]/div[1]/div/div[{i+1}]/div/div[3]/div[{j+1}]/div[1]/ul/li/text()'
            ).extract()

            if des_text is not None:
                cancel_policy = get_cancel_policy(des_text)
                if cancel_policy is None:
                    cancel_policy = "NA"
                payment_policy = get_payment_policy(des_text)

                if payment_policy is None:
                    payment_policy = "NA"

            data.append(
                {
                    "checkin": checkin,
                    "PerNight": price_before_tax,
                    "checkout": checkout,
                    "roomname": room_name.strip(),
                    "ratename": rate_name.strip(),
                    "StayTotalwTaxes": price,
                    "currency": currency.replace("/ night", "").strip(),
                    "availability": availability.strip(),
                    "cancelpolicy": cancel_policy,
                    "paymentpolicy": payment_policy,
                }
            )

    # print(data)

    print(f"saving csv for {hotel_code}..")

    convert_list_of_dicts_to_csv(data, f"output/{hotel_code}_data.csv")
