from rest_framework import viewsets

from fusion_auth.permissions import HasModuleGrant, HasPermission
from modules.department.api.serializers import (
    AnnouncementSerializer,
    DepartmentDetailChangeSerializer,
    DepartmentDetailSerializer,
    DepartmentProfileSerializer,
    DepartmentSerializer,
    FeedbackSerializer,
    InventoryItemSerializer,
    LabResourceSerializer,
    StockRequestSerializer,
    TimetableSerializer,
    TimetableSlotSerializer,
)
from modules.department.models import (
    Announcement,
    Department,
    DepartmentDetail,
    DepartmentDetailChange,
    DepartmentProfile,
    Feedback,
    InventoryItem,
    LabResource,
    StockRequest,
    Timetable,
    TimetableSlot,
)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [HasModuleGrant("department"), HasPermission("department.detail.update")]


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [
        HasModuleGrant("department"),
        HasPermission("department.announcement.publish"),
    ]


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [
        HasModuleGrant("department"),
        HasPermission("department.inventory.manage"),
    ]


class StockRequestViewSet(viewsets.ModelViewSet):
    queryset = StockRequest.objects.all()
    serializer_class = StockRequestSerializer
    permission_classes = [
        HasModuleGrant("department"),
        HasPermission("department.stock_request.create"),
    ]


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [HasModuleGrant("department"), HasPermission("department.feedback.submit")]


class DepartmentProfileViewSet(viewsets.ModelViewSet):
    queryset = DepartmentProfile.objects.all()
    serializer_class = DepartmentProfileSerializer
    permission_classes = [HasModuleGrant("department"), HasPermission("department.profile.view")]


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [
        HasModuleGrant("department"),
        HasPermission("department.timetable.manage"),
    ]


class TimetableSlotViewSet(viewsets.ModelViewSet):
    queryset = TimetableSlot.objects.all()
    serializer_class = TimetableSlotSerializer
    permission_classes = [
        HasModuleGrant("department"),
        HasPermission("department.timetable.manage"),
    ]


class LabResourceViewSet(viewsets.ModelViewSet):
    queryset = LabResource.objects.all()
    serializer_class = LabResourceSerializer
    permission_classes = [HasModuleGrant("department"), HasPermission("department.resource.view")]


class DepartmentDetailViewSet(viewsets.ModelViewSet):
    queryset = DepartmentDetail.objects.all()
    serializer_class = DepartmentDetailSerializer
    permission_classes = [HasModuleGrant("department"), HasPermission("department.detail.update")]


class DepartmentDetailChangeViewSet(viewsets.ModelViewSet):
    queryset = DepartmentDetailChange.objects.all()
    serializer_class = DepartmentDetailChangeSerializer
    permission_classes = [HasModuleGrant("department"), HasPermission("department.detail.propose")]
