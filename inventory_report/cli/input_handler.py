from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    types = ["simple", "complete"]
    if report_type not in types:
        raise ValueError("Report type is invalid.")

    if report_type == "simple":
        response = ""
        inventory = Inventory()

        for file in file_paths:
            simple = process_returns_simple(file, inventory)
            response += simple

        return response
    else:
        response = ""
        inventory = Inventory()

        for file in file_paths:
            complete = process_returns_complete(file, inventory)
            response += complete

        return response


def process_returns_simple(file_path: str, inventory: Inventory) -> str:
    if file_path.endswith(".json"):
        json_data = JsonImporter(file_path)
        inventory.add_data(json_data.import_data())
        report = SimpleReport()
        report.add_inventory(inventory)
        return report.generate()
    elif file_path.endswith(".csv"):
        csv_data = CsvImporter(file_path)
        inventory.add_data(csv_data.import_data())
        report = SimpleReport()
        report.add_inventory(inventory)
        return report.generate()
    else:
        return ""


def process_returns_complete(file_path: str, inventory: Inventory) -> str:
    if file_path.endswith(".json"):
        json_data = JsonImporter(file_path)
        inventory.add_data(json_data.import_data())
        report = CompleteReport()
        report.add_inventory(inventory)
        return report.generate()
    elif file_path.endswith(".csv"):
        csv_data = CsvImporter(file_path)
        inventory.add_data(csv_data.import_data())
        report = CompleteReport()
        report.add_inventory(inventory)
        return report.generate()
    else:
        return ""
