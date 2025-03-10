from playwright.sync_api import APIRequestContext, expect


class PaymentAPI:
    """Клас для роботи з API PaymentAPI."""
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def prepare_liqpay_payment_request(self, paymentAmount):
        """Метод для підготовки запиту на отримання платежу в LiqPay."""
        data = {
            "paymentAmount": paymentAmount
        }
        response = self.api_context.post("/api/liqpay/payment/request", data=data, headers=self.headers)
        return response


    def list_current_account_transactions(self, **kwargs):
        """Метод для отримання списку транзакцій поточного рахунку."""
        params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.get("/api/transactions", params=params, headers=self.headers)    
        return response