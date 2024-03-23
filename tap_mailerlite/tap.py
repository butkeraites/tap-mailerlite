"""MailerLite tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_mailerlite import streams


class TapMailerLite(Tap):
    """MailerLite tap class."""

    name = "tap-mailerlite"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.MailerLiteStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.SubscribersStream(self),
            streams.GroupsStream(self),
            streams.CampaignsStream(self),
        ]


if __name__ == "__main__":
    TapMailerLite.cli()
