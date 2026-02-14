from allauth.headless.base.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from abstracts.permissions import IsObjPublic
from common.permissions import MatchAnyPermissions, IsObjAdmin, IsObjOwner, MatchAllPermissions, \
    get_obj_from_view_kwargs
from folders.models import Folder
from generic_status.permissions import HasObjRoles
from modules.models import Module


class FolderObjUpdatePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjAdmin, IsObjOwner]


class FolderObjRetrievePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjAdmin, IsObjOwner, IsObjPublic]


class FolderObjPinsPolicyPermission(FolderObjRetrievePolicyPermission):
    pass


class FolderObjModuleIsPublicPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Folder) -> bool:
        if not (module := get_obj_from_view_kwargs(view, "module_id", Module)):
            return False
        return IsObjPublic().has_object_permission(request, view, module)


class FolderObjModuleIsOwnerPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Folder) -> bool:
        if not (module := get_obj_from_view_kwargs(view, "module_id", Module)):
            return False
        return IsObjOwner().has_object_permission(request, view, module)


class FolderObjUserHasEditPermission(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Folder) -> bool:
        if not (module := get_obj_from_view_kwargs(view, "module_id", Module)):
            return False
        return HasObjRoles(roles=["viewer", "editor"]).has_object_permission(request, view, module)


class FolderObjModuleRetrievePolicyPermission(MatchAnyPermissions):
    permissions_to_check = [
        FolderObjModuleIsPublicPermission,
        FolderObjModuleIsOwnerPermission,
        FolderObjUserHasEditPermission,
    ]


class FolderObjectUserCanManageModulePermission(MatchAllPermissions):
    permissions_to_check = [IsObjOwner, FolderObjModuleRetrievePolicyPermission]


class FolderObjManageModulePermission(MatchAnyPermissions):
    permissions_to_check = [IsObjAdmin, FolderObjectUserCanManageModulePermission]
