"""Server-driven module metadata for Department."""
MODULE = {
    "code": "department", "label": "Department", "icon": "Buildings",
    "base_path": "/department", "nav_section": "Department", "sort_order": 20,
    "status": "planned",
}

NAV_ITEMS = []

PERMISSIONS = [
    ("department.announcement.publish", "Publish announcements"),
    ("department.inventory.manage", "Insert and track inventory"),
    ("department.stock_request.create", "Submit stock requests"),
    ("department.feedback.submit", "Submit confidential feedback"),
    ("department.profile.view", "View department profiles"),
    ("department.timetable.manage", "Upload and modify timetables"),
    ("department.resource.view", "View lab resource profiles"),
    ("department.detail.update", "Update general department information"),
    ("department.detail.propose", "Propose official department-detail changes"),
]

SYSTEM_PERMISSIONS = []

_STUDENT = ["department.feedback.submit", "department.profile.view", "department.resource.view"]
_FACULTY = ["department.announcement.publish", "department.stock_request.create",
            "department.feedback.submit", "department.profile.view", "department.resource.view"]
_DEPT_ADMIN = [
    "department.announcement.publish", "department.inventory.manage",
    "department.feedback.submit", "department.profile.view",
    "department.timetable.manage", "department.resource.view",
    "department.detail.update", "department.detail.propose",
]
_HOD = ["department.detail.propose"]

ROLE_GRANTS = {
    "student": _STUDENT,
    "faculty": _FACULTY,
    "department_admin": _DEPT_ADMIN,
    "department_head": _HOD,
}
