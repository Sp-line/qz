from common.permissions import MatchAnyPermissions, IsObjOwner, IsObjAdmin


class UserObjDestroyPolicyPermission(MatchAnyPermissions):
    permissions_to_check = [IsObjOwner, IsObjAdmin]
