from playwright.sync_api import APIRequestContext, expect


class AccDocContactAPI:
    """Клас для роботи з API облікових записів."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


# Account Documents API -------------------------------------------------------

    def retrieve_child_account_documents(self, account_id: int):
        """Метод для отримання документів облікових записів."""
        response = self.api_context.get(f"api/account/{account_id}/documents",headers=self.headers)
        return response


    def update_child_account_documents(self, account_id: int, **kwargs):
        """Метод для оновлення документів облікових записів."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put(f"api/account/{account_id}/documents/", data=data, headers=self.headers)
        return response


    def retrieve_account_documents(self):
        """Метод для отримання документів облікових записів."""
        response = self.api_context.get("api/account/documents", headers=self.headers)
        return response


    def update_account_documents(self, **kwargs):
        """Метод для оновлення документів облікових записів."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put("api/account/documents/", data=data, headers=self.headers)
        return response


# Account contacts API --------------------------------------------------------

    def retrieve_account_contacts_for_child_account(self, account_id):
        """Метод для отримання контактів облікових записів."""
        response = self.api_context.get(f"api/account/{account_id}/contacts", headers=self.headers)
        return response

    
    def edit_contacts_for_child_account(self, account_id, **kwargs):
        """Метод для редагування контактів облікових записів."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put(f"api/account/{account_id}/contacts", data=data, headers=self.headers)
        return response 


    def retrieve_account_contacts(self):
        """Метод для отримання контактів облікових записів."""
        response = self.api_context.get("api/account/contacts", headers=self.headers)
        return response

    
    def update_account_contacts(self, **kwargs):
        """Метод для оновлення контактів облікових записів."""
        data = {
            key: value for key, value in kwargs.items() if value is not None 
        }
        response = self.api_context.put("api/account/contacts", data=data, headers=self.headers)
        return response