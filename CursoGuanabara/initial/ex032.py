#ADAPTADO
'''years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100]

print(f'Os anos bissextos do século XXI são: {years [3::4]}')'''
#xtra : import datetime and then datetime.date.today().year
#dá pra dar import calendar porque lá tem um módulo chamado isleap, que diz se o ano is leap = é bissexto

num = int(input('Digite um ano e eu te direi se esse ano é bissexto: '))
if num % 4 == 0 and num % 100 != 0 or  num % 400 == 0:
    print(f'O ano {num} é bissexto.')
else:
    print(f'O ano {num} não é bissexto.')