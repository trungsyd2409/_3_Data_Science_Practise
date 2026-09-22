from api import get_url

status_code, response_text = get_url("https://api.frankfurter.app/currencies")
print(status_code, response_text)
