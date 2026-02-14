from rest_framework.permissions import IsAuthenticated, AllowAny

from modules.permissions import (
    ModuleObjDestroyPolicyPermission,
    ModuleObjUpdatePolicyPermission,
    ModuleObjRetrievePolicyPermission,
    ModuleObjPinsPolicyPermission,
    ModuleObjRatesPolicyPermission,
)

CREATE_POLICY = [IsAuthenticated]

DESTROY_POLICY = [IsAuthenticated, ModuleObjDestroyPolicyPermission]

UPDATE_POLICY = [IsAuthenticated, ModuleObjUpdatePolicyPermission]

PARTIAL_UPDATE_POLICY = UPDATE_POLICY

LIST_POLICY = [AllowAny]

RETRIEVE_POLICY = [ModuleObjRetrievePolicyPermission]

RATES_POLICY = [IsAuthenticated, ModuleObjRatesPolicyPermission]

PINS_POLICY = [IsAuthenticated, ModuleObjPinsPolicyPermission]

SAVES_POLICY = PINS_POLICY

COPIES_POLICY = PINS_POLICY

MODULE_MERGE_POLICY = PINS_POLICY


POLICIES = {
    "retrieve": RETRIEVE_POLICY,
    "list": LIST_POLICY,
    "create": CREATE_POLICY,
    "update": UPDATE_POLICY,
    "partial_update": PARTIAL_UPDATE_POLICY,
    "destroy": DESTROY_POLICY,
    "saves": SAVES_POLICY,
    "pins": PINS_POLICY,
    "rates": RATES_POLICY,
    "copies": COPIES_POLICY,
}
