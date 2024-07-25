import pygeolang

# Get alpha-3 code
code = pygeolang.get_country_code("Germany", "alpha_3")  
print(code)  # Output: DEU

# Get country object by numeric code
country = pygeolang.get_country_by_code("276")
print(country.name)  # Output: Germany

# Get country object by alpha_2 code and access its official name
country = pygeolang.get_country_by_code("DE")
print(country.official_name)  # Output: Federal Republic of Germany

languages = pygeolang.core.get_languages_by_country("India")
if languages:
    print("Languages spoken in India:", languages)
else:
    print("Country not found or no language data available.")
