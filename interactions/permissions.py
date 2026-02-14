from rest_framework.permissions import BasePermission, IsAuthenticated

from common.permissions import IsObjAdmin, IsObjOwner, MatchAnyPermissions


class InteractionsUserCanReadPolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjAdmin, IsObjOwner]


class InteractionsPermsMixin:
    def get_permissions(self) -> list[BasePermission]:
        if self.action in {"pins", "saves"}:
            return [IsAuthenticated()]
        if self.action in {"user_saves_list", "user_pins_list"}:
            return [IsAuthenticated(), InteractionsUserCanReadPolicyPermission()]
        return super().get_permissions()
