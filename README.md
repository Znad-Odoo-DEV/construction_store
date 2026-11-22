# Construction Store

Odoo 19 module that ties a site store to a project, on top of the native inventory.

## Features

- A project and a storekeeper on the stock location.
- A project on the transfer (the site it was consumed on, or the store it was received into).
- Quantities only: no accounting entries are posted, so material cost is not counted twice.

## Dependencies

Odoo 19: `stock`, `project`, `hr`.

## Installation

1. Copy this folder into your Odoo 19 addons path.
2. Update the apps list and install **Construction Store**.

## License

LGPL-3
