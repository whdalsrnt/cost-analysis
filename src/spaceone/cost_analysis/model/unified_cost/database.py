from mongoengine import *

from spaceone.core.model.mongo_model import MongoModel


class UnifiedCost(MongoModel):
    unified_cost_id = StringField(
        max_length=40, generate_id="unified-cost", unique=True
    )
    cost = DictField(default={})
    cost_report_name = StringField(max_length=255)
    billed_month = StringField(max_length=40)
    billed_year = StringField(max_length=20)
    exchange_date = StringField(max_length=40)
    exchange_source = StringField(max_length=40)
    aggregation_date = StringField(max_length=40)
    currency = StringField(max_length=40)
    is_confirmed = BooleanField(default=False)
    provider = StringField(max_length=40)
    region_code = StringField(max_length=60)
    region_key = StringField(max_length=60)
    product = StringField(max_length=255)
    usage_type = StringField(max_length=255)
    usage_unit = StringField(max_length=255)
    service_account_name = StringField(max_length=255)
    data_source_name = StringField(max_length=255)
    project_name = StringField(max_length=255)
    workspace_name = StringField(max_length=255)
    service_account_id = StringField(max_length=40)
    data_source_id = StringField(max_length=40)
    project_id = StringField(max_length=40, default=None, null=True)
    workspace_id = StringField(max_length=40)
    domain_id = StringField(max_length=40)
    created_at = DateTimeField(auto_now_add=True)

    meta = {
        "updatable_fields": [],
        "minimal_fields": [
            "unified_cost_id",
            "data_source_id",
            "workspace_id",
            "aggregation_date",
        ],
        "ordering": ["is_confirmed", "-aggregation_date"],
        "change_query_keys": {"user_projects": "project_id"},
        "indexes": [
            {
                "fields": [
                    "is_confirmed",
                    "workspace_id",
                    "domain_id",
                    "project_id",
                ],
                "name": "COMPOUND_INDEX_FOR_DEFAULT_UNIFIED_COST",
            },
            {
                "fields": [
                    "aggregation_date",
                    "domain_id",
                    "workspace_id",
                    "project_id",
                ],
                "name": "COMPOUND_INDEX_FOR_WORKSPACE_LANDING",
            },
            {
                "fields": [
                    "workspace_id",
                    "billed_year",
                    "billed_month",
                    "is_confirmed",
                ],
                "name": "COMPOUND_INDEX_FOR_DELETE_UNIFIED_COST",
            },
        ],
    }