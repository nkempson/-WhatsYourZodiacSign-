#name: Nasia Kempson
#date: 07/28/2021
#title: What's Your Zodiac Sign?
#description: This is an app to determine what your astrological/zodiac sign is.
#to operate the, click run, you will be prompted to enter your Birth month and your Birth Day.
#Birthday must be typed with lowercase letters.

month = input("What Month Were You Born?  ")
day = int(input("What Day Were You Born?  "))


if month == 'december':
	zodiac_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	zodiac_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	zodiac_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	zodiac_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	zodiac_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	zodiac_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	zodiac_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	zodiac_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	zodiac_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	zodiac_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	zodiac_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	zodiac_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",zodiac_sign)