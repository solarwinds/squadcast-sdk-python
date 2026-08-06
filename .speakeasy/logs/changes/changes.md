## Python SDK Changes:
* `squadcast_sdk.overlays.dedup_key.get_for_alert_source()`:  `response.data.overlay_template_type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.dedup_keys.list_by_service()`:  `response.data[].overlay_template_type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.rotations.get_participants()`: `response.data` **Changed** (Breaking ⚠️)
    - `participant_groups` **Added**
    - `participants` **Removed** (Breaking ⚠️)
* `squadcast_sdk.incidents.reassign()`: 
  *  `request.reassign_to.type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.incidents.actions.webhook.trigger()`:  `response.data.triggers[]` **Changed** (Breaking ⚠️)
* `squadcast_sdk.services.create()`: `request` **Changed** (Breaking ⚠️)
    - `owner_id_param` **Added** (Breaking ⚠️)
    - `owner_id` **Changed**
* `squadcast_sdk.services.overlays.dedup_key.update()`:  `response.union(class (0)).data.overlay_template_type` **Changed** (Breaking ⚠️)
* `squadcast_sdk.teams.create()`:  `response.data.roles` **Changed**
* `squadcast_sdk.incidents.incidents_unmerge_incident()`: **Added**
* `squadcast_sdk.incidents.incidents_merge_incidents()`: **Added**
* `squadcast_sdk.teams.get_all()`:  `response.data[].roles` **Changed**
* `squadcast_sdk.teams.get()`:  `response.data.roles` **Changed**
* `squadcast_sdk.teams.update()`:  `response.data.roles` **Changed**
* `squadcast_sdk.teams.roles.create()`:  `response.data.roles` **Changed**
* `squadcast_sdk.teams.roles.update()`:  `response.data.roles` **Changed**
* `squadcast_sdk.status_pages/subscribers.status_pages_delete_subscriber_by_id()`: **Added**
* `squadcast_sdk.status_pages.list()`:  `response.data[].custom_domain_name` **Changed**
* `squadcast_sdk.status_pages.get_by_id()`:  `response.data.custom_domain_name` **Changed**
* `squadcast_sdk.status_pages.update()`:  `response.data.custom_domain_name` **Changed**
