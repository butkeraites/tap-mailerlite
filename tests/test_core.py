"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_mailerlite.tap import TapMailerLite

import json

with open(".secrets/config.json") as json_file:
    data = json.load(json_file)
    SAMPLE_CONFIG = {
        "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
        "auth_token": data["TAP_MAILERLITE_AUTH_TOKEN"],
        "project_ids": [data["PROJECT_ID"]],
    }


# Run standard built-in tap tests from the SDK:
TestTapMailerLite = get_tap_test_class(
    tap_class=TapMailerLite,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
