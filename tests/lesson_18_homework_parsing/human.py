import argparse
import json
import xml.dom.minidom
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__, indent=4)

    def convert_to_xml(self):
        human_element = ET.Element("Human")
        for key, value in self.__dict__.items():
            element = ET.Element(key)
            element.text = str(value)
            human_element.append(element)

        xml_string = ET.tostring(human_element)
        xml_formatted = xml.dom.minidom.parseString(xml_string)
        return xml_formatted.toprettyxml()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Convert Human object to JSON or XML")
    parser.add_argument("format", choices=["json", "xml"], help="Output format (json or xml)")

    args = parser.parse_args()

    human = Human("Andrii", 30, "Male", 1989)

    if args.format == "json":
        json_str = human.convert_to_json()
        print("JSON:")
        print(json_str)
    elif args.format == "xml":
        xml_str = human.convert_to_xml()
        print("XML:")
        print(xml_str)
