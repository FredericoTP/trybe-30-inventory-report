from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        data = []

        with open(self.path) as file:
            products = json.load(file)

        for item in products:
            data.append(
                Product(
                    item["id"],
                    item["product_name"],
                    item["company_name"],
                    item["manufacturing_date"],
                    item["expiration_date"],
                    item["serial_number"],
                    item["storage_instructions"],
                )
            )

        return data


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
