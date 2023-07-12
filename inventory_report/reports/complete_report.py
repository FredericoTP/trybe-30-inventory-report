from inventory_report.reports.simple_report import SimpleReport
from inventory_report.product import Product


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        data = self.inventory.data
        oldest = self.oldest_manufacturing_date(data)
        closest = self.closest_expiration_date(data)
        largest = self.largest_inventory(data)
        companies = self.get_all_companies(data)

        return (
            f"Oldest manufacturing date: {oldest}\n"
            f"Closest expiration date: {closest}\n"
            f"Company with the largest inventory: {largest}\n"
            f"Stocked products by company:\n"
            f"{companies}"
        )

    def get_all_companies(self, data: list[Product]) -> str:
        companies: dict[str, int] = {}

        for item in data:
            if not companies.get(item.company_name):
                companies[item.company_name] = 1
            else:
                companies[item.company_name] += 1

        string_to_return = ""

        for key, value in companies.items():
            company = f"- {key}: {value}\n"
            string_to_return += company

        return string_to_return
