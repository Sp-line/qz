from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from abstracts.permissions import IsObjPublic
from cards.models import Card
from common.permissions import MatchAnyPermissions, IsObjAdmin, IsObjOwner
from generic_status.permissions import HasObjRoles


class IsObjCardModulePublic(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Card) -> bool:
        return IsObjPublic().has_object_permission(request, view, obj.module)


class IsObjCardModuleOwner(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Card) -> bool:
        return IsObjOwner().has_object_permission(request, view, obj.module)


class IsObjCardModuleUserHasReadPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Card) -> bool:
        return HasObjRoles(roles=["viewer", "editor"]).has_object_permission(request, view, obj.module)


class IsObjCardModuleUserHasEditPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Card) -> bool:
        return HasObjRoles(roles=["editor"]).has_object_permission(request, view, obj.module)


class CardObjRetrievePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjAdmin, IsObjCardModulePublic, IsObjCardModuleOwner, IsObjCardModuleUserHasReadPermission]
    

class CardObjCreatePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjCardModuleOwner, IsObjAdmin, IsObjCardModuleUserHasEditPermission]
