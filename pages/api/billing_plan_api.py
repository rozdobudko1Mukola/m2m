from playwright.sync_api import APIRequestContext, expect


class BillingPlanAPI:
    """Клас для роботи з API BillingPlanAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def get_billing_plan_template_by_id(self, billing_plan_id: int):
        """Метод для отримання шаблону планування за ID."""
        response = self.api_context.get(f"/api/billing/plan/{billing_plan_id}", headers=self.headers)
        return response


    def update_billing_plan_template_properties(self, billing_plan_id: int, **kwargs):
        """Метод для оновлення властивостей шаблону планування."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"/api/billing/plan/{billing_plan_id}", data=data, headers=self.headers)
        return response

    
    def remove_the_billing_plan_template(self, billing_plan_id: int):
        """Метод для видалення шаблону планування."""
        response = self.api_context.delete(f"/api/billing/plan/{billing_plan_id}", headers=self.headers)
        return response


    def retrieve_a_list_of_billing_plan_templates_with_pagination(self, **kwargs):
        """Метод для отримання списку шаблонів планування з пагінацією."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get(f"/api/billing/plans", params=params, headers=self.headers)
        return response


    def create_new_billing_plan_template(self, **kwargs):
        """Метод для створення нового шаблону планування."""
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("/api/billing/plans", data=data, headers=self.headers)
        return response


    def change_to_another_billing_plan(self, billingPlanId: int):
        """Метод для зміни на інший план планування."""
        data = {
            "billingPlanId": billingPlanId
        }
        response = self.api_context.post("/api/billing/plan/change", data=data, headers=self.headers)
        return response


    def retrieve_a_public_billing_plan_templates(self):
        """Метод для отримання публічних шаблонів планування."""
        response = self.api_context.get("/api/billing/plans/public", headers=self.headers)
        return response


    def retrieve_a_list_of_billing_plan_templates_without_pagination(self, search: str):
        """Метод для отримання списку шаблонів планування без пагінації."""
        params = {
            "search": search
        }
        response = self.api_context.get("/api/billing/plans/all", params=params, headers=self.headers)
        return response