import json

def convert_format(raw_json):
    formatted_json = {
        "image_path": raw_json.get("image_path", ""),
        "annotations": []
    }

    # Check if "vehicle" class is present
    if "vehicle" in raw_json:
        for vehicle_data in raw_json["vehicle"]:
            formatted_json["annotations"].append({
                "class": "vehicle",
                "attributes": {
                    "presence": vehicle_data.get("presence", "")
                }
            })

    # Check if "license plate" class is present
    if "license plate" in raw_json:
        for plate_data in raw_json["license plate"]:
            formatted_json["annotations"].append({
                "class": "license plate",
                "attributes": {
                    "presence": plate_data.get("presence", "")
                }
            })

    return formatted_json

def main():
    input_file_path = "pos_0.png.json"
    output_file_path = "formatted_pos_0.png.json"

    with open(input_file_path, "r") as file:
        raw_json = json.load(file)

    formatted_json = convert_format(raw_json)

    with open(output_file_path, "w") as output_file:
        json.dump(formatted_json, output_file, indent=2)

if __name__ == "__main__":
    main()
