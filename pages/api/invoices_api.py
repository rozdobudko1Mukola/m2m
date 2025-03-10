from playwright.sync_api import APIRequestContext, expect


class InvoiceAPI:
    """Клас для роботи з API InvoiceAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def get_account_invoice_by_id(self, invoice_id: int):
        """Метод для отримання інформації про Invoice по ID."""
        response = self.api_context.get(f"/api/invoice/{invoice_id}",headers=self.headers)
        return response


    def update_invoice_properties(self, invoice_id: int, **kwargs):
        """Метод для оновлення властивостей Invoice по ID."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/invoice/{invoice_id}", data=data, headers=self.headers)
        return response

    
    def get_list_of_invoices_paginated(self, **kwargs):
        """Метод для отримання списку Invoice."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/invoices", params=params, headers=self.headers)
        return response


    def export_a_list_of_invoices_paginated_to_file(self, file_ext, **kwargs):
        """Метод для експорту списку Invoice в файл."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/invoices/{file_ext}", params=params, headers=self.headers)
        return response


    def get_invoice_pdf(self, invoice_id: int):
        """Метод для отримання PDF Invoice по ID."""
        response = self.api_context.get(f"/api/invoice/{invoice_id}/invoice/pdf", headers=self.headers)
        return response