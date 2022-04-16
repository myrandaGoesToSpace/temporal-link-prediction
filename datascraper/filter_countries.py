"""
The purpose of this script is to filter top N countries from both reporters and partners
based on the node_countries file that is provided. This uses fuzzy text matching to extract the text
https://www.worldometers.info/gdp/gdp-by-country/
"""
import json
from fuzzywuzzy import fuzz

def best_match(country, obj):
    return max([
        (fuzz.ratio(country, l['text']), (l['text'], l['id'])) for l in obj['results']
    ])

def filter_json(obj, lines):
    r = []
    for country in lines:
        best = best_match(country, obj)
        if best[0] != 100:
            print (f"The best match for {country} is {best}")
        r.append(best[1])
    return r
    # for country in obj['results']:
    #     best = best_match(country['text'], lines)
    #     print (f"The best match for {country} is {best}")

lines = list(map(lambda l: l.strip(), open("node_countries.txt", "r")))
partners_obj = json.load(open("partners.json", "r"))
reporters_obj = json.load(open("reporters.json", "r"))
filtered_partners = filter_json(partners_obj, lines)
filtered_reporters = filter_json(reporters_obj, lines)

# open("filtered_partners", 'w').write(json.dumps(dict(filtered_partners)))
open("country_codes.json", 'w').write(json.dumps(dict(filtered_reporters)))

# The country code is uniform
assert set(filtered_reporters) == set(filtered_partners)