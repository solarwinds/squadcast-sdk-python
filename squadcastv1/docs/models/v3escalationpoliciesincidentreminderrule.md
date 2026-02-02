# V3EscalationPoliciesIncidentReminderRule

Represents a rule for sending incident reminders.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `via`                                                  | List[*str*]                                            | :heavy_check_mark:                                     | The notification methods to use for the reminder.      |
| `time_interval`                                        | *int*                                                  | :heavy_check_mark:                                     | The interval in minutes at which to send the reminder. |
| `till`                                                 | *int*                                                  | :heavy_check_mark:                                     | The duration in minutes for which to send reminders.   |