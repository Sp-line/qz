from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from abstracts.permissions import IsObjPublic
from common.permissions import MatchAnyPermissions, IsObjAdmin, IsObjOwner, MatchAllPermissions
from generic_status.permissions import HasObjRoles
from modules.models import Module


class ModuleUserHasReadPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Module) -> bool:
        return HasObjRoles(roles=["editor", "viewer"]).has_object_permission(request, view, obj)


class ModuleUserHasEditPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Module) -> bool:
        return HasObjRoles(roles=["editor"]).has_object_permission(request, view, obj)


class ModuleObjDestroyPolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjOwner, IsObjAdmin]


class ModuleObjUpdatePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjOwner, IsObjAdmin, ModuleUserHasEditPermission]


class ModuleObjRetrievePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjOwner, IsObjAdmin, IsObjPublic, ModuleUserHasReadPermission]


class ModuleObjPinsPolicyPermission(ModuleObjRetrievePolicyPermission):
    pass


class ModuleObjRatesPolicySubPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjOwner, IsObjAdmin, ModuleUserHasReadPermission]


class ModuleObjRatesPolicyPermission(MatchAllPermissions):
    permissions_to_check = [~IsObjOwner, ModuleObjRatesPolicySubPermission]


class ModuleObjExportPolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjPublic, IsObjAdmin, IsObjOwner, ModuleUserHasReadPermission]
