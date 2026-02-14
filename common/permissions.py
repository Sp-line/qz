from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Any, Type

from django.db.models import Q
from rest_framework.permissions import BasePermission

from common.access_chain import AccessibleChain
from common.decorators import login_required_link

if TYPE_CHECKING:
    from django.db.models import Model
    from rest_framework.request import Request
    from rest_framework.views import APIView


def partial_cls(base: Any, *args: Any, **kwargs: Any) -> Any:
    class Adapter(base):
        def __init__(self):
            super().__init__(*args, **kwargs)
    return Adapter


class IsObjOwner(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        user = request.user
        if not user.is_authenticated:
            return False
        return obj.user == request.user


class IsObjAdmin(BasePermission):
    def has_object_permission(self,request: Request,view: APIView,obj: Any) -> bool:
        user = request.user
        if not user.is_authenticated:
            return False
        return bool(request.user and request.user.is_staff)


class OwnerIncludedLink(AccessibleChain):
    @login_required_link
    def handle(self, q: Optional[Q] = None) -> Q:
        if q is None:
            q = Q()

        q |= Q(user=self.request.user)
        return super().handle(q)


def get_accessible_q(request: Request, links: list[Type[AccessibleChain]]) -> Q:
    root = AccessibleChain(request)
    for l in links:
        root.add(l())
    return root.handle()


class MatchAllPermissions(BasePermission):
    permissions_to_check: list[type[BasePermission]] | None = None

    def has_permission(self, request: Request, view: APIView) -> bool:
        for perm_class in self.permissions_to_check:
            perm = perm_class()
            if not perm.has_permission(request, view):
                return False
        return True

    def has_object_permission(self, request: Request, view: APIView, obj: Model) -> bool:
        for perm_class in self.permissions_to_check:
            perm = perm_class()
            if not perm.has_object_permission(request, view, obj):
                return False
        return True


class MatchAnyPermissions(BasePermission):
    permissions_to_check: list[type[BasePermission]] | None = None

    def has_permission(self, request, view):
        for perm_class in self.permissions_to_check:
            perm = perm_class()
            if perm.has_permission(request, view):
                return True
        return False

    def has_object_permission(self, request, view, obj):
        for perm_class in self.permissions_to_check:
            perm = perm_class()
            if perm.has_object_permission(request, view, obj):
                return True
        return False


def get_obj_from_view_kwargs[T](view: APIView, lookup_url_kwarg: str, model_class: type[T]) -> T | None:
    obj_id = view.kwargs.get(lookup_url_kwarg)
    try:
        return model_class.objects.get(pk=obj_id)
    except model_class.DoesNotExist:
        return None
