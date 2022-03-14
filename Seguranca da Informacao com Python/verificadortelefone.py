import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefonoe no formato: +5511912345678: ')

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))