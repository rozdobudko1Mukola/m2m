import pytest
from pytest import mark
from pages.api.billing_plan_api import BillingPlanAPI
from playwright.sync_api import expect


# Fixtures ---------------------------------------------------------------------

@pytest.fixture(scope="function")
def billing_plan_data():
    return {
        "name": "test api billing plan",
        "vehicleCost": 0,
        "vehiclePauseCost": 0,
        "personalTrackerCost": 0,
        "personalTrackerPauseCost": 0,
        "beaconCost": 0,
        "beaconPauseCost": 0,
        "vehicleFuelCost": 0,
        "vehicleFuelPauseCost": 0,
        "dataStoringDays": "30",
        "dataStoringPerDayCost": 0,
        "template": 0,
        "simKyivstarCost": 0,
        "simKyivstarRoamingCost": 0,
        "simVodafoneCost": 0,
        "simVodafoneRoamingCost": 0,
        "simLifecellCost": 0,
        "simLifecellRoamingCost": 0,
        "simUkrtelecomCost": 0,
        "simUkrtelecomRoamingCost": 0,
        "simTravelSimCost": 0,
        "simTravelSimRoamingCost": 0,
        "blockSum": 0,
        "deviceLimit": 0,
        "description": "",
        "publicPlan": False,
        "allowBeacon": False,
        "allowVehicle": False,
        "allowVehicleFuel": False,
        "allowPersonalTracker": False,
        "allowReportTemplates": False
    }

@pytest.fixture(scope="function")
def create_new_billing_plan_template(api_context, admin_token, test_data, billing_plan_data):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.create_new_billing_plan_template(**billing_plan_data)

    json_data = response.json()
    test_data['billing_plan_id'] = json_data['id']

    yield


@pytest.fixture(scope="function")
def delete_billing_plan_template(api_context, admin_token, test_data):

    yield

    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.remove_the_billing_plan_template(test_data['billing_plan_id'])
    expect(response).to_be_ok()


@pytest.fixture(scope="function")
def create_and_remove_bill_plan(api_context, admin_token, test_data, billing_plan_data):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.create_new_billing_plan_template(**billing_plan_data)

    json_data = response.json()
    test_data['billing_plan_id'] = json_data['id']

    yield

    response = billing_plan.remove_the_billing_plan_template(test_data['billing_plan_id'])
    expect(response).to_be_ok()


# Tests ------------------------------------------------------------------------

@mark.api
@mark.smoke
@mark.testomatio('@Tttttt993')
def test_get_billing_plan_template_by_id(api_context, admin_token, test_data, create_and_remove_bill_plan):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.get_billing_plan_template_by_id(test_data['billing_plan_id'])
    expect(response).to_be_ok()
    assert response.json()['name'] == "test api billing plan"


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt994')
def test_updata_billing_plan_template_properties(api_context, admin_token, test_data, create_and_remove_bill_plan):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.update_billing_plan_template_properties(test_data['billing_plan_id'], name='new name')
    expect(response).to_be_ok()
    assert response.json()['name'] == 'new name'


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt995')
def test_remove_the_billing_plan_template(api_context, admin_token, test_data, create_new_billing_plan_template):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.remove_the_billing_plan_template(test_data['billing_plan_id'])
    expect(response).to_be_ok()
    test_data.pop('billing_plan_id', None)


@mark.api
@mark.smoke
@mark.testomatio('@Ttttt1738')
def test_retrieve_a_list_of_billing_plan_templates_with_pagination(api_context, admin_token, test_data, create_and_remove_bill_plan):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.retrieve_a_list_of_billing_plan_templates_with_pagination(page=1, per_page=10)
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt996')
def test_create_new_billing_plan_template(api_context, admin_token, test_data, billing_plan_data, delete_billing_plan_template):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.create_new_billing_plan_template(**billing_plan_data)

    json_data = response.json()
    test_data['billing_plan_id'] = json_data['id']


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt997')
@mark.skip("Зміна тарифу можлива не частіше ніж один раз на 24 години. Поки не знаю як автоматизувати тест")
def test_change_to_another_billing_plan(api_context, token, test_data):
    billing_plan = BillingPlanAPI(api_context, token)
    response = billing_plan.change_to_another_billing_plan(7)
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt998')
def test_retrieve_a_public_billing_plan_templates(api_context, token):
    billing_plan = BillingPlanAPI(api_context, token)
    response = billing_plan.retrieve_a_public_billing_plan_templates()
    expect(response).to_be_ok()


@mark.api
@mark.smoke
@mark.testomatio('@Tttttt999')
def test_retrieve_a_list_of_billing_plan_templates_without_pagination(api_context, admin_token):
    billing_plan = BillingPlanAPI(api_context, admin_token)
    response = billing_plan.retrieve_a_list_of_billing_plan_templates_without_pagination(search='')
    expect(response).to_be_ok()
