import pytz


def get_timezones():
    """Get list countries and cities"""
    timezones = []
    for key in pytz.country_timezones:
        country = pytz.country_names.get(key)
        if country == 'Russia':
            cities = pytz.country_timezones.get(key)
            for city in cities:
                city_ = ' '.join(city.split('/')[1:])
                result = (f'{country}, {city_.replace("_", " ")} - {city}', f'{country}, {city_}')
                timezones.append(result)
    return tuple(sorted(timezones))
