import requests

BASE_URL = "www.dataaccess.com"


def number_to_words(data_xml: str):
    response = requests.post(
        url=f"https://{BASE_URL}/webservicesserver/NumberConversion.wso",
        headers={
            "Host": BASE_URL,
            "Content-Type": "text/xml; charset=utf-8",
            "Content-Length": str(len(data_xml.encode('utf-8')))
        },
        data=data_xml)
    return response


