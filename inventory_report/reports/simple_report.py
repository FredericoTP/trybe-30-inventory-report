from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from inventory_report.product import Product
from datetime import datetime, date


# Comparação de datas --> https://datagy.io/python-string-to-date/


class SimpleReport(Report):
    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory = inventory

    def generate(self) -> str:
        data = self.inventory.data
        oldest = self.oldest_manufacturing_date(data)
        closest = self.closest_expiration_date(data)
        largest = self.largest_inventory(data)

        return (
            f"Oldest manufacturing date: {oldest} "
            f"Closest expiration date: {closest} "
            f"Company with the largest inventory: {largest}"
        )

    def oldest_manufacturing_date(self, data: list[Product]) -> str:
        oldest = min(item.manufacturing_date for item in data)

        return oldest

    def closest_expiration_date(self, data: list[Product]) -> str:
        today = date.today()
        closest = min(
            item.expiration_date
            for item in data
            if datetime.strptime(item.expiration_date, "%Y-%m-%d").date()
            > today
        )

        return closest

    def largest_inventory(self, data: list[Product]) -> str:
        companies: dict[str, int] = {}

        for item in data:
            if not companies.get(item.company_name):
                companies[item.company_name] = 1
            else:
                companies[item.company_name] += 1

        return max(companies, key=lambda item: companies[item])
