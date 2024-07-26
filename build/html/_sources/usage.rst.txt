Usage
=====

Here are some examples of how to use PyGeoLang:

.. code-block:: python

   import pygeolang

   # Get country code
   code = pygeolang.get_country_code("Germany", "alpha_3")
   print(code)  # Output: DEU

   # Get country by code
   country = pygeolang.get_country_by_code("276")
   print(country.name)  # Output: Germany
   print(country.official_name)  # Output: Federal Republic of Germany
   print(country.languages)    # Output: ['German']
   print(country.continent)    # Output: Europe

   # Get countries by continent
   countries = pygeolang.get_countries_by_continent("Asia")
   print(countries) # ['Afghanistan', 'Armenia', ... ]

   # Get languages by country
   languages = pygeolang.get_languages_by_country("India")
   print(languages) # ['Hindi', 'English', ...]
