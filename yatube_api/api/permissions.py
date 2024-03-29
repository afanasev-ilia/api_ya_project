from typing import Any

from django.http import HttpRequest
from rest_framework import permissions, viewsets


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(
        self,
        request: HttpRequest,
        unused: viewsets,
    ) -> bool:
        del unused
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(
        self,
        request: HttpRequest,
        unused: viewsets,
        obj: Any,
    ) -> bool:
        del unused
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
