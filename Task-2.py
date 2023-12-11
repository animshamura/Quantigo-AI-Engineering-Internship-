import json

def combine_and_rename(json_files):
    combined_json = {"images": []}

    for file_path in json_files:
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Change class names as specified
        for annotation in data.get("annotations", []):
            if "class" in annotation:
                if annotation["class"] == "Vehicle":
                    annotation["class"] = "car"
                elif annotation["class"] == "license plate":
                    annotation["class"] = "number"

        combined_json["images"].append(data)

    return combined_json

def main():
    input_files = ["Pos_0.png.json", "Pos_10010.png.json", "Pos_10492.png.json"]
    output_file = "combined_and_renamed.json"

    combined_data = combine_and_rename(input_files)

    with open(output_file, "w") as output_file:
        json.dump(combined_data, output_file, indent=2)

if __name__ == "__main__":
    main()
