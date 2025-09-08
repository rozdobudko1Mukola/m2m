import pytest
from datetime import datetime
from playwright.sync_api import expect

from pages.api.account_api import AccountAPI
from pages.api.devices_api import DeviceAPI


# --------------------
# 1. Список API-параметрів (orderBy)
# --------------------
account_order_by = [
    "ACCOUNT_NAME", "CREATOR_NAME", "BILLING_PLAN",
    "UNITS_COUNT", "BALANCE", "ACCOUNT_STATUS", "CREATED_DATE"
]

device_order_by = [
    "DEVICE_NAME", "OBJECT_TYPE", "TRACKER_TYPE",
    "UNIQUE_ID", "PHONE", "PHONE_2", "CREATED_DATE", "LAST_MESSAGE_DATE"
]

# --------------------
# 2. Мапінг: API-параметр -> поле JSON для перевірки
# --------------------
account_field_mapping = {
    "ACCOUNT_NAME": "email",
    "CREATOR_NAME": "creatorName",
    "BILLING_PLAN": "billingPlanName",
    "UNITS_COUNT": "unitsCount",
    "BALANCE": "balance",
    "ACCOUNT_STATUS": "enabled",
    "CREATED_DATE": "creatingDate"
}

device_field_mapping = {
    "DEVICE_NAME": "name",
    "OBJECT_TYPE": "type",
    "TRACKER_TYPE": "model",
    "UNIQUE_ID": "uniqueId",
    "PHONE": "phone",
    "PHONE_2": "phone2",
    "CREATED_DATE": "createDate",
    "LAST_MESSAGE_DATE": "lastUpdate"
}


# --------------------
# Універсальна функція перевірки сортування
# --------------------
def check_sorting(response_json, field_name, order="ASC"):
    """
    Перевіряє чи відсортовані елементи у JSON по заданому полю.

    :param response_json: відповідь API (dict)
    :param field_name: ключ у JSON для перевірки
    :param order: "ASC" або "DESC"
    :return: список порушень [(елементА, елементB), ...]
    """
    elements = []
    for item in response_json.get("items", []):
        if "device" in item:  # деякі елементи загорнуті в "device"
            elements.append(item["device"])
        else:
            elements.append(item)

    def get_value(el):
        value = el.get(field_name)
        if field_name in ["creatingDate", "createDate", "lastUpdate"] and value:
            value = datetime.fromisoformat(value)
        return value

    violations = []
    for i in range(len(elements) - 1):
        a, b = get_value(elements[i]), get_value(elements[i + 1])
        if a is None or b is None:
            continue
        if order.upper() == "ASC" and a > b:
            violations.append((elements[i], elements[i + 1]))
        elif order.upper() == "DESC" and a < b:
            violations.append((elements[i], elements[i + 1]))
    return violations


# --------------------
# Тести для Accounts
# --------------------
@pytest.mark.parametrize("api_field,order", [
    (field, order) for field in account_order_by for order in ["ASC", "DESC"]
])
def test_api_sort_acc(api_context, admin_token, api_field, order):
    account_api = AccountAPI(api_context, admin_token)

    # API отримує параметр orderBy = api_field
    api_order_field = api_field
    # А ми перевіряємо значення у JSON по ключу з мапінгу
    field_for_check = account_field_mapping[api_field]

    response = account_api.retrieve_a_list_of_accounts_with_pagination(
        page=1,
        per_page=100,
        orderBy=api_order_field,
        order=order
    )
    expect(response).to_be_ok

    data = response.json()

    # Логування
    values_list = [el.get(field_for_check) if "device" not in el else el["device"].get(field_for_check)
                   for el in data.get("items", [])]
    print(f"\n[ACCOUNTS] API Field: {api_field} -> JSON Field: {field_for_check}, Order: {order}")
    print("Values:", values_list)

    # Перевірка сортування
    violations = check_sorting(data, field_for_check, order)
    if violations:
        message = f"Порядок порушено (Accounts) по {api_field} ({field_for_check}):\n"
        for a, b in violations:
            message += f"  id={a.get('id')} ({field_for_check}={a.get(field_for_check)}) -> " \
                       f"id={b.get('id')} ({field_for_check}={b.get(field_for_check)})\n"
        pytest.fail(message)


# --------------------
# Тести для Devices
# --------------------
@pytest.mark.parametrize("api_field,order", [
    (field, order) for field in device_order_by for order in ["ASC", "DESC"]
])
def test_api_sort_units(api_context, admin_token, api_field, order):
    device_api = DeviceAPI(api_context, admin_token)

    # API отримує параметр orderBy = api_field
    api_order_field = api_field
    # А ми перевіряємо значення у JSON по ключу з мапінгу
    field_for_check = device_field_mapping[api_field]

    response = device_api.retrieve_list_of_devices_with_pagination(
        page=1,
        per_page=100,
        orderBy=api_order_field,
        order=order
    )
    expect(response).to_be_ok

    data = response.json()

    # Логування
    values_list = [el.get(field_for_check) if "device" not in el else el["device"].get(field_for_check)
                   for el in data.get("items", [])]
    print(f"\n[DEVICES] API Field: {api_field} -> JSON Field: {field_for_check}, Order: {order}")
    print("Values:", values_list)

    # Перевірка сортування
    violations = check_sorting(data, field_for_check, order)
    if violations:
        message = f"Порядок порушено (Devices) по {api_field} ({field_for_check}):\n"
        for a, b in violations:
            message += f"  id={a.get('id')} ({field_for_check}={a.get(field_for_check)}) -> " \
                       f"id={b.get('id')} ({field_for_check}={b.get(field_for_check)})\n"
        pytest.fail(message)
