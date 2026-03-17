import json
import os
from pathlib import Path


def main():
    current_path = Path(os.path.dirname(os.path.abspath(__file__)))
    report_path = current_path / "Sales.Report"

    visual_files = list(report_path.rglob("visual.json"))

    for file in visual_files:
        print(f"Processing visual in file: {file}")

        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        visual = data.get("visual", {})

        # Ensure the nested structure exists
        if "visualContainerObjects" not in visual:
            visual["visualContainerObjects"] = {}

        container_objects = visual["visualContainerObjects"]

        if "title" not in container_objects:
            container_objects["title"] = [{"properties": {}}]

        title = container_objects["title"]

        # title can be a list (array) - access the first element
        if isinstance(title, list):
            title_obj = title[0]
        else:
            title_obj = title

        if "properties" not in title_obj:
            title_obj["properties"] = {}

        properties = title_obj["properties"]

        if "show" not in properties:
            properties["show"] = {
                "expr": {
                    "Literal": {
                        "Value": "false"
                    }
                }
            }
        else:
            properties["show"]["expr"]["Literal"]["Value"] = "false"

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")


if __name__ == "__main__":
    main()