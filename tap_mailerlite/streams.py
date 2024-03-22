"""Stream type classes for tap-mailerlite."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailerlite.client import MailerLiteStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class SubscribersStream(MailerLiteStream):
    """Define custom stream."""

    name = "subscribers"
    path = "/subscribers"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("email", th.StringType),
        th.Property("status", th.StringType),
        th.Property("source", th.StringType),
        th.Property("sent", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("clicks_count", th.IntegerType),
        th.Property("open_rate", th.IntegerType),
        th.Property("click_rate", th.IntegerType),
        th.Property("ip_address", th.StringType),
        th.Property("subscribed_at", th.StringType),
        th.Property("unsubscribed_at", th.StringType),
        th.Property("created_at", th.StringType),
        th.Property("updated_at", th.StringType),
        th.Property(
            "fields",
            th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("country", th.StringType),
                th.Property("city", th.StringType),
                th.Property("phone", th.StringType),
                th.Property("state", th.StringType),
                th.Property("z_i_p", th.StringType),
            ),
        ),
        th.Property("opted_in_at", th.StringType),
        th.Property("optin_ip", th.StringType),
    ).to_dict()


class GroupsStream(MailerLiteStream):
    """Define custom stream."""

    name = "groups"
    path = "/groups"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("name", th.StringType),
        th.Property("active_count", th.IntegerType),
        th.Property("sent_count", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("open_rate", th.IntegerType),
        th.Property(
            "open_rate",
            th.ObjectType(
                th.Property("float", th.NumberType),
                th.Property("string", th.StringType),
            ),
        ),
        th.Property("clicks_count", th.IntegerType),
        th.Property(
            "click_rate",
            th.ObjectType(
                th.Property("float", th.NumberType),
                th.Property("string", th.StringType),
            ),
        ),
        th.Property("unsubscribed_count", th.IntegerType),
        th.Property("unconfirmed_count", th.IntegerType),
        th.Property("bounced_count", th.IntegerType),
        th.Property("junk_count", th.IntegerType),
        th.Property("created_at", th.StringType),
    ).to_dict()


class CampaignsStream(MailerLiteStream):
    """Define custom stream."""

    name = "campaigns"
    path = "/campaigns"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("account_id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("missing_data", th.ArrayType(th.AnyType)),
        th.Property(
            "settings",
            th.ObjectType(
                th.Property("track_opens", th.BooleanType),
                th.Property("use_google_analytics", th.BooleanType),
            ),
        ),
        th.Property("filter", th.ArrayType(th.AnyType)),
        th.Property("filter_for_humans", th.ArrayType(th.AnyType)),
        th.Property("delivery_schedule", th.StringType),
        th.Property("language_id", th.StringType),
        th.Property(
            "language",
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("shortcode", th.StringType),
                th.Property("iso639", th.StringType),
                th.Property("name", th.StringType),
                th.Property("direction", th.StringType),
            ),
        ),
        th.Property("created_at", th.StringType),
        th.Property("updated_at", th.StringType),
        th.Property("scheduled_for", th.StringType),
        th.Property("queued_at", th.StringType),
        th.Property("started_at", th.StringType),
        th.Property("finished_at", th.StringType),
        th.Property("stopped_at", th.StringType),
        th.Property("default_email_id", th.StringType),
        th.Property(
            "emails",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("account_id", th.StringType),
                    th.Property("emailable_id", th.StringType),
                    th.Property("emailable_type", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("from", th.StringType),
                    th.Property("from_name", th.StringType),
                    th.Property("reply_to", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("subject", th.StringType),
                    th.Property("plain_text", th.StringType),
                    th.Property("screenshot_url", th.StringType),
                    th.Property("preview_url", th.StringType),
                    th.Property("created_at", th.StringType),
                    th.Property("updated_at", th.StringType),
                    th.Property("is_designed", th.BooleanType),
                    th.Property("language_id", th.IntegerType),
                    th.Property(
                        "language",
                        th.ObjectType(
                            th.Property("id", th.StringType),
                            th.Property("shortcode", th.StringType),
                            th.Property("iso639", th.StringType),
                            th.Property("name", th.StringType),
                            th.Property("direction", th.StringType),
                        ),
                    ),
                    th.Property("is_winner", th.BooleanType),
                    th.Property(
                        "stats",
                        th.ObjectType(
                            th.Property("sent", th.IntegerType),
                            th.Property("opens_count", th.IntegerType),
                            th.Property("unique_opens_count", th.IntegerType),
                            th.Property(
                                "open_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("clicks_count", th.IntegerType),
                            th.Property("unique_clicks_count", th.IntegerType),
                            th.Property(
                                "click_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("unsubscribes_count", th.IntegerType),
                            th.Property(
                                "unsubscribe_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("spam_count", th.IntegerType),
                            th.Property(
                                "spam_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("hard_bounces_count", th.IntegerType),
                            th.Property(
                                "hard_bounce_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("soft_bounces_count", th.IntegerType),
                            th.Property(
                                "soft_bounce_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("forwards_count", th.IntegerType),
                            th.Property(
                                "forward_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property("social_interactions_count", th.IntegerType),
                            th.Property(
                                "social_interaction_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                            th.Property(
                                "click_to_open_rate",
                                th.ObjectType(
                                    th.Property("float", th.NumberType),
                                    th.Property("string", th.StringType),
                                ),
                            ),
                        ),
                    ),
                    th.Property("send_after", th.StringType),
                    th.Property("track_opens", th.BooleanType),
                    th.Property("uses_survey", th.BooleanType),
                    th.Property("uses_quiz", th.BooleanType),
                    th.Property("preheader", th.StringType),
                )
            ),
        ),
        th.Property("used_in_automations", th.BooleanType),
        th.Property("type_for_humans", th.StringType),
        th.Property("is_stopped", th.BooleanType),
        th.Property("has_winner", th.StringType),
        th.Property("winner_version_for_human", th.StringType),
        th.Property("winner_sending_time_for_humans", th.StringType),
        th.Property("winner_selected_manually_at", th.StringType),
        th.Property(
            "can",
            th.ObjectType(
                th.Property("update", th.BooleanType),
                th.Property("delete", th.BooleanType),
                th.Property("send", th.BooleanType),
                th.Property("copy", th.BooleanType),
                th.Property("resend", th.BooleanType),
            ),
        ),
        th.Property("uses_ecommerce", th.BooleanType),
        th.Property(
            "ecommerce_stats",
            th.ObjectType(
                th.Property("total_orders", th.IntegerType),
                th.Property("total_price", th.StringType),
                th.Property("multi_currency", th.BooleanType),
            ),
        ),
        th.Property("uses_survey", th.BooleanType),
        th.Property("can_be_scheduled", th.BooleanType),
        th.Property("is_smart_sending_index_option_finished", th.BooleanType),
        th.Property("is_applied_for_smart_sending_index_option", th.BooleanType),
        th.Property("warnings", th.ArrayType(th.AnyType)),
        th.Property("initial_created_at", th.StringType),
        th.Property("is_currently_sending_out", th.BooleanType),
        th.Property("can_be_copied", th.BooleanType),
        th.Property("has_basic_filter", th.BooleanType),
        th.Property(
            "basic_filter_for_humans",
            th.ObjectType(
                th.Property("included_groups", th.ArrayType(th.AnyType)),
                th.Property("excluded_groups", th.ArrayType(th.AnyType)),
                th.Property("included_segments", th.ArrayType(th.AnyType)),
                th.Property("excluded_segments", th.ArrayType(th.AnyType)),
                th.Property("all_active_subscribers", th.BooleanType),
            ),
        ),
        th.Property("is_eligible_for_sending", th.BooleanType),
    ).to_dict()
