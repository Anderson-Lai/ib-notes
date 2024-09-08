import json

def get_value(name: str) -> dict:
    result = {}
    cleaned = name.lower()
    try:
        with open("periodic-table.json", "r") as file:
            result = json.load(file)
            for element in result["elements"]:
                if (element["name"].lower() == cleaned or element["symbol"].lower() == cleaned):
                    return element
    except FileNotFoundError:
        return {}
    return {}

def main():
    while True:
        name = input("\nelement: ")
        result = get_value(name)
        formatted = json.dumps(result, indent=4)
        print()
        print(formatted)
    
    return 0

if __name__ == "__main__":
    main()
