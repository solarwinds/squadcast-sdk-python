## Python SDK Changes:
* `squadcast_sdk.webhooks.create()`: `response` **Changed** (Breaking ⚠️)
    - `body` **Removed** (Breaking ⚠️)
    - `data` **Added**
* `squadcast_sdk.incidents.export.export_async()`: `response.union(ResponseBody)` **Changed** (Breaking ⚠️)
    - `body` **Removed** (Breaking ⚠️)
    - `data` **Added**
* `squadcast_sdk.incidents.notes.create()`: `response` **Changed** (Breaking ⚠️)
    - `body` **Removed** (Breaking ⚠️)
    - `data` **Added**
* `squadcast_sdk.postmortems.create()`: `response` **Changed** (Breaking ⚠️)
    - `body` **Removed** (Breaking ⚠️)
    - `data` **Added**
* `squadcast_sdk.users.get_all()`:  `response.data[].notification_rules` **Changed** (Breaking ⚠️)
* `squadcast_sdk.users.add()`:  `response.data.notification_rules` **Changed** (Breaking ⚠️)
* `squadcast_sdk.users.get_by_id()`:  `response.data.notification_rules` **Changed** (Breaking ⚠️)
* `squadcast_sdk.users.update_by_id()`:  `response.data.notification_rules` **Changed** (Breaking ⚠️)
* `squadcast_sdk.services.create()`: `response` **Changed** (Breaking ⚠️)
    - `body` **Removed** (Breaking ⚠️)
    - `data` **Added**
* `squadcast_sdk.services.overlay.custom_content_templates.get_all()`:  `response.data[].overlay_template_type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.services.overlay.custom_content_templates.create_or_update()`:  `response.data.overlay_template_type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.services.overlays.custom_content_templates.get()`:  `response.data.overlay_template_type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.schedules.list()`: `response.page_info` **Changed** (Breaking ⚠️)
    - `has_prev` **Added**
    - `has_previous` **Removed** (Breaking ⚠️)
    - `prev_cursor` **Added**
    - `previous_cursor` **Removed** (Breaking ⚠️)
* `squadcast_sdk.schedules.overrides.list()`: `response.page_info` **Changed** (Breaking ⚠️)
    - `has_prev` **Added**
    - `has_previous` **Removed** (Breaking ⚠️)
    - `prev_cursor` **Added**
    - `previous_cursor` **Removed** (Breaking ⚠️)
* `squadcast_sdk.rotations.list_by_schedule()`:  `response.data` **Changed** (Breaking ⚠️)
* `squadcast_sdk.squads.list()`: `response.page_info` **Changed** (Breaking ⚠️)
    - `has_prev` **Added**
    - `has_previous` **Removed** (Breaking ⚠️)
    - `prev_cursor` **Added**
    - `previous_cursor` **Removed** (Breaking ⚠️)
