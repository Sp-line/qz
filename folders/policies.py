from rest_framework.permissions import IsAuthenticated, AllowAny

from folders.permissions import (
    FolderObjUpdatePolicyPermission,
    FolderObjRetrievePolicyPermission,
    FolderObjPinsPolicyPermission,
    FolderObjManageModulePermission,
)

CREATE_POLICY = [IsAuthenticated]

UPDATE_POLICY = [IsAuthenticated, FolderObjUpdatePolicyPermission]

PARTIAL_UPDATE_POLICY = UPDATE_POLICY

DESTROY_POLICY = UPDATE_POLICY

LIST_POLICY = [AllowAny]

RETRIEVE_POLICY = [FolderObjRetrievePolicyPermission]

PINS_POLICY = [IsAuthenticated, FolderObjPinsPolicyPermission]

SAVES_POLICY = PINS_POLICY

MANAGE_MODULE_POLICY = [IsAuthenticated, FolderObjManageModulePermission]


POLICIES = {
    "retrieve": RETRIEVE_POLICY,
    "list": LIST_POLICY,
    "create": CREATE_POLICY,
    "update": UPDATE_POLICY,
    "partial_update": PARTIAL_UPDATE_POLICY,
    "destroy": DESTROY_POLICY,
    "saves": SAVES_POLICY,
    "pins": PINS_POLICY,
    "manage_module": MANAGE_MODULE_POLICY,
}
