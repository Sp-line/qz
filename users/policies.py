from rest_framework.permissions import AllowAny, IsAuthenticated

from users.permissions import UserObjDestroyPolicyPermission

DESTROY_POLICY = [IsAuthenticated, UserObjDestroyPolicyPermission]

LIST_POLICY = [AllowAny]

RETRIEVE_POLICY = LIST_POLICY


POLICIES = {
    "list": LIST_POLICY,
    "retrieve": RETRIEVE_POLICY,
    "destroy": DESTROY_POLICY,
}
