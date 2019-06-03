import json

leaders = [
    {
        "name": "Madison",
        "description": "Slightly less awesome than kosa"
    },
    {
        "name": "Madison",
        "description": "Slightly less awesome than kosa"
    }
]


with open("techleader.json", "w") as file:
    json.dump(leaders,file,indent=4)