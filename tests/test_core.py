"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_mailerlite.tap import TapMailerLite

import json

with open("config.json") as json_file:
    data = json.load(json_file)
    SAMPLE_CONFIG = {
        "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
        "auth_token": data["auth_token"],
    }


# Run standard built-in tap tests from the SDK:
TestTapMailerLite = get_tap_test_class(
    tap_class=TapMailerLite,
    config=SAMPLE_CONFIG,
)
