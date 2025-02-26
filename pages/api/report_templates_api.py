from playwright.sync_api import APIRequestContext, expect

class ReportTemplatesAPI:
    def __init__(self, api_context: APIRequestContext, token: str):
        self.api_context = api_context
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}


    def create_new_report_template(self, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post("api/report/templates", data=data, headers=self.headers)
        return response


    def remove_report_template(self, template_id: str):
        response = self.api_context.delete(f"api/report/template/{template_id}", headers=self.headers)
        return response


    def create_new_report_template_chart(self, template_id: str, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"api/report/template/{template_id}/charts", data=data, headers=self.headers)
        return response

    
    def remove_report_template_chart(self, template_id: str, chart_id: str):
        response = self.api_context.delete(f"api/report/template/{template_id}/chart/{chart_id}", headers=self.headers)
        return response


    def create_new_report_template_table(self, template_id: str, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"api/report/template/{template_id}/tables", data=data, headers=self.headers)
        return response


    def remove_report_template_table(self, template_id: str, table_id: str):
        response = self.api_context.delete(f"api/report/template/{template_id}/table/{table_id}", headers=self.headers)
        return response


    def get_report_template_table_by_id(self, template_id: str, table_id: str):
        response = self.api_context.get(f"api/report/template/{template_id}/table/{table_id}", headers=self.headers)
        return response


    def update_report_template_table_properties(self, template_id: str, table_id: str, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"api/report/template/{template_id}/table/{table_id}", data=data, headers=self.headers)
        return response


    def get_report_template_chart_by_id(self, template_id: str, chart_id: str):
        response = self.api_context.get(f"api/report/template/{template_id}/chart/{chart_id}", headers=self.headers)
        return response


    def update_report_template_chart_properties(self, template_id: str, chart_id: str, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"api/report/template/{template_id}/chart/{chart_id}", data=data, headers=self.headers)
        return response


    def get_report_template_by_id(self, template_id: str):
        response = self.api_context.get(f"api/report/template/{template_id}", headers=self.headers)
        return response


    def update_report_template_properties(self, template_id: str, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.put(f"api/report/template/{template_id}", data=data, headers=self.headers)
        return response


    def rename_report_template(self, template_id: str, name: str):
        data={
            "name": name
            }
        response = self.api_context.put(f"api/report/template/{template_id}/rename", data=data, headers=self.headers)
        return response


    def retrieve_list_of_reports_templates(self):
        response = self.api_context.get("api/report/templates", headers=self.headers)
        return response


    def retrieve_list_of_report_tables(self, template_id: str):
        response = self.api_context.get(f"api/report/template/{template_id}/tables", headers=self.headers)
        return response


    def retrieve_list_of_report_charts(self, template_id: str):
        response = self.api_context.get(f"api/report/template/{template_id}/charts", headers=self.headers)
        return response


    def execute_the_report_by_template(self, template_id: str, elementId: str, dateFrom: str, dateTo: str):
        response = self.api_context.get(f"api/report/template/{template_id}/execute?elementId={elementId}&dateFrom={dateFrom}&dateTo={dateTo}", headers=self.headers)
        return response


    def get_report_template_permission_for_child(self, template_id: str, user_id: str):
        response = self.api_context.get(f"api/permission/user/{user_id}/template/{template_id}", headers=self.headers)
        return response


    def update_report_template_permission_for_child(self, template_id: str, user_id: str, **kwargs):
        data = {
            key: value for key, value in kwargs.items() if value is not None
        }
        response = self.api_context.post(f"api/permission/user/{user_id}/template/{template_id}", data=data, headers=self.headers)
        return response