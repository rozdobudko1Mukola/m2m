from playwright.sync_api import APIRequestContext, expect


class CompaniesAPI:
    """Клас для роботи з API CompaniesAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    
    def get_company_by_id(self, companyId):
        """Метод для отримання компанії по ID."""
        response = self.api_context.get(f"/api/company/{companyId}", headers=self.headers)
        return response

    
    def update_company_properties(self, companyId, **kwargs):
        """Метод для оновлення властивостей компанії."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/company/{companyId}", data=data, headers=self.headers)
        return response


    def delete_company(self, companyId):
        """Метод для видалення компанії."""
        response = self.api_context.delete(f"/api/company/{companyId}", headers=self.headers)
        return response


    def get_invoice_properties(self, companyId):
        """Метод для отримання властивостей рахунків."""
        response = self.api_context.get(f"/api/company/{companyId}/invoice/properties", headers=self.headers)
        return response


    def update_invoice_properties(self, companyId, **kwargs):
        """Метод для оновлення властивостей рахунків."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put(f"/api/company/{companyId}/invoice/properties", data=data, headers=self.headers)
        return response


    def get_stamp_image(self, companyId):
        """Метод для отримання зображення печатки."""
        response = self.api_context.get(f"/api/company/{companyId}/invoice/stamp", headers=self.headers)
        return response


    def save_stamp_image(self, companyId, image):
        """Метод для збереження зображення печатки."""
        with open(image, 'rb') as img_file:
            files = {'image': img_file}
            response = self.api_context.post(f"/api/company/{companyId}/invoice/stamp", files=files, headers=self.headers)
        return response


    def get_signature_image(self, companyId):
        """Метод для отримання зображення підпису."""
        response = self.api_context.get(f"/api/company/{companyId}/invoice/signature", headers=self.headers)
        return response


    def save_signature_image(self, companyId, image):
        """Метод для збереження зображення підпису."""
        response = self.api_context.post(f"/api/company/{companyId}/invoice/signature", image=image, headers=self.headers)
        return response


    def retrieve_a_list_of_companies_with_pagination(self, **kwargs):
        """Метод для отримання списку компаній з пагінацією."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/companies", params=params, headers=self.headers)
        return response


    def create_a_new_company(self, **kwargs):
        """Метод для створення нової компанії."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/companies", data=data, headers=self.headers)
        return response


    def assign_company_to_account(self, companyId, accountId):
        """Метод для призначення компанії до акаунту."""
        data = {
            "companyId": companyId
        }
        response = self.api_context.post(f"/api/account/{accountId}/company/assign", data=data,  headers=self.headers)
        return response


    def get_preview_of_invoice(self, companyId):
        """Метод для отримання попереднього перегляду рахунку."""
        response = self.api_context.get(f"/api/company/{companyId}/invoice/preview", headers=self.headers)
        return response