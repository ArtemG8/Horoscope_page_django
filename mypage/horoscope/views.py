from django.http import HttpResponse
from django.urls import reverse


def get_type(request,):
    zodiacs = ["Fire", "Earth", "Air", "Water"]
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li><a href='{redirect_path}'</a><font size=10>{sign}</li>"  # Вывод списка стихий
    return HttpResponse(li_elements)


def get_info_word(request, sign_zodiac: str):
    fire_zodiacs = {'Aries': 'Aries is the first sign of the zodiac, the planet Mars (from March 21 to April 20).',
                    'Leo': 'Leo is the fifth sign of the zodiac, the sun (from July 23 to August 21).',
                    'Sagittarius': 'Sagittarius is the ninth sign of the zodiac, Capricorn is the tenth sign of the '
                                   'zodiac, '
                                   'the planet Saturn ( '
                                   'from December 23 to January 20).', }
    earth_zodiacs = {'Taurus': ' Taurus is the second sign of the zodiac, the planet Venus (from April 21 to May 21).',
                     'Virgo': 'Virgo is the sixth sign of the zodiac, the planet Mercury (from August 22 to September '
                              '23).',
                     'Capricorn': 'Capricorn is the tenth sign of the zodiac, the planet Saturn (from December 23 to '
                                  'January 20).'}
    air_zodiacs = {'Gemini': ' Gemini is the third sign of the zodiac, the planet Mercury (from May 22 to June 21).',
                   'Libra': 'Libra is the seventh sign of the zodiac, the planet Venus (from September 24 to October '
                            '23)',
                   'Aquarius': 'Aquarius is the eleventh sign of the zodiac, the planets Uranus and Saturn (from '
                               'January 21 to '
                               'February 19).'}
    water_zodiacs = {'Cancer': 'Cancer is the fourth sign of the zodiac, the Moon (from June 22 to July 22).',
                     'Scorpio': 'Scorpio is the eighth sign of the zodiac, the planet Mars (from October 24 to '
                                'November 22).',
                     'Pisces': 'Pisces is the twelfth sign of the zodiac, the planet Jupiter (from February 20 to '
                               'March 20). '
                     }
    zod_fire = list(fire_zodiacs)
    zod_earth = list(earth_zodiacs)
    zod_air = list(air_zodiacs)
    zod_water = list(water_zodiacs)

    elements = ''

    if sign_zodiac == 'Fire':  # При нажатии на стихию приходит запрос в sign_zodiac, а дальше переадресация по функции:
        for sign_f in zod_fire:
            redirect_path = reverse('horoscope_name', args=[sign_f])
            elements += f'<li><a href={redirect_path}><font size=10>{sign_f} </a></li>'  # Вывод списка задиаков
        return HttpResponse(elements)
    elif sign_zodiac == 'Aries':
        return HttpResponse(fire_zodiacs.get('Aries'))
    elif sign_zodiac == 'Leo':
        return HttpResponse(fire_zodiacs.get('Leo'))
    elif sign_zodiac == 'Sagittarius':
        return HttpResponse(fire_zodiacs.get('Sagittarius'))
    # end of fire zodiacs

    if sign_zodiac == 'Earth':
        for sign_w in zod_earth:
            redirect_path = reverse('horoscope_name', args=[sign_w])
            elements += f'<li><a href={redirect_path}><font size=10>{sign_w}</a></li>'
        return HttpResponse(elements)  # по аналогии с fire zadiacs
    elif sign_zodiac == 'Taurus':
        return HttpResponse(earth_zodiacs.get('Taurus'))
    elif sign_zodiac == 'Virgo':
        return HttpResponse(earth_zodiacs.get('Virgo'))
    elif sign_zodiac == 'Capricorn':
        return HttpResponse(earth_zodiacs.get('Capricorn'))
    # end of earth zodiacs

    if sign_zodiac == 'Air':
        for sign_w in zod_air:
            redirect_path = reverse('horoscope_name', args=[sign_w])
            elements += f'<li><a href={redirect_path}><font size=10>{sign_w}</a></li>'
        return HttpResponse(elements)  # по аналогии с fire zadiacs
    elif sign_zodiac == 'Gemini':
        return HttpResponse(air_zodiacs.get('Gemini'))
    elif sign_zodiac == 'Libra':
        return HttpResponse(air_zodiacs.get('Libra'))
    elif sign_zodiac == 'Aquarius':
        return HttpResponse(air_zodiacs.get('Aquarius'))
    # end of Air zodiacs

    if sign_zodiac == 'Water':
        for sign_w in zod_water:
            redirect_path = reverse('horoscope_name', args=[sign_w])
            elements += f'<li><a href={redirect_path}><font size=10>{sign_w}</a></li>'
        return HttpResponse(elements)  # по аналогии с fire zadiacs
    elif sign_zodiac == 'Cancer':
        return HttpResponse(water_zodiacs.get('Cancer'))
    elif sign_zodiac == 'Scorpio':
        return HttpResponse(water_zodiacs.get('Scorpio'))
    elif sign_zodiac == 'Pisces':
        return HttpResponse(water_zodiacs.get('Pisces'))
