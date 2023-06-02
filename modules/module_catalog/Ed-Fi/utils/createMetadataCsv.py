import requests
import csv

swaggerUrls = [
    "https://api.ed-fi.org/v5.2/api/metadata/composites/v1/ed-fi/enrollment/swagger.json",
    # "https://api.ed-fi.org/v5.2/api/metadata/identity/v2/swagger.json",
    "https://api.ed-fi.org/v5.2/api/metadata/data/v3/descriptors/swagger.json",
    "https://api.ed-fi.org/v5.2/api/metadata/data/v3/resources/swagger.json"
    ]

definitions = dict()
with open('./Metadata.csv', 'w',newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write header row
    writer.writerow(["Entity Name","Attribute Name","Attribute Data Type","Pseudonymization"])

    for url in swaggerUrls:
        print(url)
        swagger = requests.get(url).json()

        #build all definitions
        for definition in swagger['definitions'].keys():
            key = definition
            print(key)

            # write entity row
            # writer.writerow([key,"","",""])

            if key not in definitions:
                definitions[key] = {}
                for property in swagger["definitions"][definition]["properties"].keys():
                    print(property, swagger["definitions"][definition]["properties"][property])
                    if "$ref" in swagger["definitions"][definition]["properties"][property]:
                        #For now don't add refs to the definitions.  
                        #definitions[key][property] = swagger["definitions"][definition]["properties"][property]
                        pass
                    elif property == "id":
                        definitions[key][property] = ["",property, swagger["definitions"][definition]["properties"][property]["type"],"hash"]
                    elif swagger["definitions"][definition]["properties"][property]["type"] == "array":
                        definitions[key][property] = ["",property, "string","no-op"]
                    elif swagger["definitions"][definition]["properties"][property]["type"] == "number":
                        definitions[key][property] = ["",property, "float","no-op"]
                    else:
                        definitions[key][property] = ["",property, swagger["definitions"][definition]["properties"][property]["type"],"no-op"]
            print("--------------------------------------")

        #iterate over the entities by path and write metadata for each entity to file
        for entity in swagger["paths"].keys():
            print(entity)
            entity_split = entity.split("/")
            entity_key = entity_split[2]
            print(entity_key)
            print(swagger["paths"][entity]["get"]["responses"]["200"])
            rows = []
            for property in swagger["paths"][entity]["get"]["responses"]["200"]['schema'].keys():
                if property == "$ref":
                    definition = swagger["paths"][entity]["get"]["responses"]["200"]['schema'][property].split("/")[-1]
                    print(definitions[definition])
                    for field in definitions[definition]:
                        rows.append(definitions[definition][field])
                # else:
                #     print(swagger["paths"][entity]["get"]["responses"]["200"]['schema'][property])
            if len(rows) > 0:
                rows.insert(0,[entity_key,"","",""])
                writer.writerows(rows)
            print("------------------------------")
