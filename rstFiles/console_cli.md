## console\_cli.py

This file is responsible for displaying and receiving inputs from the cli. It has no subscribers or
publishers, but it does instantiate [console_event_logger.py](https://aerpaw-uav.atlassian.net/wiki/spaces/VD/pages/149422199) to receive MQTT messages.

| Subscribers | Publishers |
|-------------|------------|
| NONE        | NONE       |

## Cli commands

- add <data\_type>
  - add a data type to display in the cli table
- del <data\_type>
  - delete a data type to display in the cli table
