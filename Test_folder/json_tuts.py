import json

simple_dict = {"key": "value"}
print(simple_dict["key"])

data = {"president": {"name": "Donald Trump",
                      "nation": "USA"
                      }
                      }

print(data["president"])

json_string = json.dumps(data)
print(json_string)

json_string2 = """
    {
        "Countries":{
            "Scotland": [{"Capital": "Edinburgh"}],
            "England": [{"Capital": "London"}],
            "Northern Ireland":[{"Capital": "Belfast"}],
            "Wales":[{"Capital": "Cardiff"}]
        }
    }
"""

countries_dict = json.loads(json_string2)

print(type(json_string2))
print(type(countries_dict))

with open("country_data.json", "w") as write_file:
    json.dump(countries_dict, write_file)

