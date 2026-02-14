from rest_framework.permissions import IsAuthenticated

from cards.permissions import CardObjRetrievePolicyPermission, IsObjCardModuleUserHasEditPermission, \
    CardObjCreatePolicyPermission

RETRIEVE_POLICY = [CardObjRetrievePolicyPermission]

LIST_POLICY = RETRIEVE_POLICY

LEARNS_POLICY = RETRIEVE_POLICY

SAVES_POLICY = [IsAuthenticated, CardObjRetrievePolicyPermission]

CREATE_POLICY = [IsAuthenticated, CardObjCreatePolicyPermission]

UPDATE_POLICY = CREATE_POLICY

PARTIAL_UPDATE_POLICY = CREATE_POLICY

DESTROY_POLICY = CREATE_POLICY

POLICIES = {
    "retrieve": RETRIEVE_POLICY,
    "list": LIST_POLICY,
    "learns": LEARNS_POLICY,
    "saves": SAVES_POLICY,
    "create": CREATE_POLICY,
    "update": UPDATE_POLICY,
    "partial_update": PARTIAL_UPDATE_POLICY,
    "destroy": DESTROY_POLICY,
}
