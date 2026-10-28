
"""Warehouse asset maintenance registry with inspection tracking."""

import json
import tempfile
from datetime import datetime, timedelta

# Global state
assets = {}
registration_logs = []
CONFIG = {"service_interval_days": 90}


def register_asset(asset_id, machine_type, logs=None):
    """Register a warehouse asset and record its registration."""
    if not asset_id:
        raise ValueError("Asset ID cannot be empty")

    if logs is None:
        logs = registration_logs

    assets[asset_id] = {
        "type": machine_type,
        "last_service": datetime.now().strftime("%Y-%m-%d"),
    }
    logs.append(asset_id)

    print(
        "Registered",
        asset_id,
        "- total registrations this run:",
        len(logs),
    )


def update_service_date(asset_id, date):
    """Update the last service date for a registered asset."""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        assets[asset_id]["last_service"] = date
    except KeyError:
        print("Could not update", asset_id)
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")


def due_for_inspection():
    """Return asset IDs whose inspections are overdue."""
    due = []

    for asset_id, asset in assets.items():
        last_service = datetime.strptime(
            asset["last_service"], "%Y-%m-%d"
        )

        if datetime.now() - last_service > timedelta(
            days=CONFIG["service_interval_days"]
        ):
            due.append(asset_id)

    return due


def change_interval(days):
    """Update the inspection interval after validating it."""
    if days <= 0:
        raise ValueError("Service interval must be positive")

    CONFIG["service_interval_days"] = days


def export_service_report(file="maintenance.json"):
    """Export the asset registry to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=2)

    print("Report written to " + file)


def write_scratch_copy():
    """Write the asset registry to a secure temporary JSON file."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False,
        encoding="utf-8",
    ) as f:
        json.dump(assets, f)
        path = f.name

    print("Scratch copy at", path)


def print_alerts():
    """Print alerts for assets with overdue inspections."""
    for asset_id in due_for_inspection():
        print(
            "ALERT: inspection overdue for",
            asset_id,
            assets[asset_id]["type"],
        )


def main():
    """Run the warehouse asset maintenance registry."""
    register_asset("FL-01", "Forklift")
    register_asset("CV-07", "Conveyor")
    register_asset("PJ-03", "Pallet Jack")

    update_service_date("FL-01", "2025-01-15")
    update_service_date("XX-99", "2025-02-01")

    change_interval(90)

    service_date = input(
        "Last service date for CV-07 (YYYY-MM-DD, Enter to skip): "
    )

    if service_date:
        update_service_date("CV-07", service_date)

    if not assets:
        raise ValueError("No assets registered")

    print_alerts()
    export_service_report()
    write_scratch_copy()


if __name__ == "__main__":
    main()
