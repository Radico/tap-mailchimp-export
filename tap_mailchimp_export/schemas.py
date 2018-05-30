#!/usr/bin/env python3
import os
import singer
from singer import utils


class IDS(object):
    CAMPAIGNS = "campaigns"
    CAMPAIGN_SUBSCRIBER_ACTIVITY = "campaign_subscriber_activity"
    CAMPAIGN_UNSUBSCRIBES = "campaign_unsubscribes"
    LISTS = "lists"
    LIST_MEMBERS = "list_members"

stream_ids = [getattr(IDS, x) for x in dir(IDS)
              if not x.startswith("__")]

PK_FIELDS = {
    IDS.CAMPAIGNS: ["id"],
    IDS.CAMPAIGN_SUBSCRIBER_ACTIVITY: ["uuid"],
    IDS.LISTS: ["id"],
    IDS.LIST_MEMBERS: ["email"],
    IDS.CAMPAIGN_UNSUBSCRIBES: ["email"],
}

EXPORT_API_PATH_NAMES = {
    IDS.CAMPAIGN_SUBSCRIBER_ACTIVITY: "campaignSubscriberActivity",
    IDS.LIST_MEMBERS: "list"
}

V3_API_PATH_NAMES = {
    IDS.LIST_MEMBERS: "members",
    IDS.CAMPAIGN_UNSUBSCRIBES: "unsubscribed"
}

V3_API_INDEX_NAMES = {
    IDS.LIST_MEMBERS: "members",
    IDS.CAMPAIGN_UNSUBSCRIBES: "unsubscribes"
}

V3_API_ENDPOINT_NAMES = {
    IDS.CAMPAIGNS: "campaigns",
    IDS.LISTS: "lists",
    IDS.LIST_MEMBERS: "lists",
    IDS.CAMPAIGN_UNSUBSCRIBES: "reports"
}

V3_SINCE_KEY = {
    IDS.CAMPAIGNS: "since_send_time",
    IDS.LIST_MEMBERS: "since_last_changed",
    IDS.CAMPAIGN_SUBSCRIBER_ACTIVITY: "since",
    IDS.LISTS: "since_date_created"
}



def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schema(tap_stream_id):
    path = "schemas/{}.json".format(tap_stream_id)
    return utils.load_json(get_abs_path(path))


def load_and_write_schema(tap_stream_id):
    schema = load_schema(tap_stream_id)
    singer.write_schema(tap_stream_id, schema, PK_FIELDS[tap_stream_id])
