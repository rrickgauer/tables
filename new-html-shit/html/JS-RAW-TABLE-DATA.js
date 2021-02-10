const G_TABLE_DATA = [
    {
        "table": "Event_Cancelations",
        "data": [
            {
                "field": "id",
                "type": "char(36)",
                "null": "NO",
                "key": "PRI",
                "default": null,
                "extra": ""
            },
            {
                "field": "event_id",
                "type": "char(36)",
                "null": "NO",
                "key": "MUL",
                "default": null,
                "extra": ""
            },
            {
                "field": "date",
                "type": "date",
                "null": "NO",
                "key": "",
                "default": null,
                "extra": ""
            }
        ]
    },
    {
        "table": "Event_Completions",
        "data": [
            {
                "field": "id",
                "type": "char(36)",
                "null": "NO",
                "key": "PRI",
                "default": null,
                "extra": ""
            },
            {
                "field": "event_id",
                "type": "char(36)",
                "null": "NO",
                "key": "MUL",
                "default": null,
                "extra": ""
            },
            {
                "field": "date",
                "type": "date",
                "null": "NO",
                "key": "",
                "default": null,
                "extra": ""
            }
        ]
    },
    {
        "table": "Event_Notes",
        "data": [
            {
                "field": "id",
                "type": "char(36)",
                "null": "NO",
                "key": "PRI",
                "default": null,
                "extra": ""
            },
            {
                "field": "event_id",
                "type": "char(36)",
                "null": "NO",
                "key": "MUL",
                "default": null,
                "extra": ""
            },
            {
                "field": "created_on",
                "type": "datetime",
                "null": "NO",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "content",
                "type": "text",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            }
        ]
    },
    {
        "table": "Event_Recurrences",
        "data": [
            {
                "field": "id",
                "type": "char(36)",
                "null": "NO",
                "key": "PRI",
                "default": null,
                "extra": ""
            },
            {
                "field": "event_id",
                "type": "char(36)",
                "null": "NO",
                "key": "MUL",
                "default": null,
                "extra": ""
            },
            {
                "field": "week",
                "type": "int(11)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "day",
                "type": "int(11)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "month",
                "type": "int(11)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            }
        ]
    },
    {
        "table": "Events",
        "data": [
            {
                "field": "id",
                "type": "char(36)",
                "null": "NO",
                "key": "PRI",
                "default": null,
                "extra": ""
            },
            {
                "field": "user_id",
                "type": "char(36)",
                "null": "NO",
                "key": "MUL",
                "default": null,
                "extra": ""
            },
            {
                "field": "name",
                "type": "varchar(100)",
                "null": "NO",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "description",
                "type": "text",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "phone_number",
                "type": "varchar(10)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "location_address_1",
                "type": "varchar(70)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "location_address_2",
                "type": "varchar(70)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "location_city",
                "type": "varchar(40)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "location_state",
                "type": "char(2)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "location_zip",
                "type": "varchar(5)",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "starts_on",
                "type": "date",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "ends_on",
                "type": "date",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "starts_at",
                "type": "datetime",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "ends_at",
                "type": "datetime",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "frequency",
                "type": "enum('ONCE','DAILY','WEEKLY','MONTHLY','YEARLY')",
                "null": "YES",
                "key": "",
                "default": "ONCE",
                "extra": ""
            },
            {
                "field": "seperation",
                "type": "int(10) unsigned",
                "null": "YES",
                "key": "",
                "default": "1",
                "extra": ""
            },
            {
                "field": "count",
                "type": "int(10) unsigned",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "until",
                "type": "date",
                "null": "YES",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "created_on",
                "type": "timestamp",
                "null": "NO",
                "key": "",
                "default": "CURRENT_TIMESTAMP",
                "extra": ""
            }
        ]
    },
    {
        "table": "Users",
        "data": [
            {
                "field": "id",
                "type": "char(36)",
                "null": "NO",
                "key": "PRI",
                "default": null,
                "extra": ""
            },
            {
                "field": "email",
                "type": "varchar(100)",
                "null": "NO",
                "key": "UNI",
                "default": null,
                "extra": ""
            },
            {
                "field": "password",
                "type": "varchar(250)",
                "null": "NO",
                "key": "",
                "default": null,
                "extra": ""
            },
            {
                "field": "created_on",
                "type": "datetime",
                "null": "NO",
                "key": "",
                "default": null,
                "extra": ""
            }
        ]
    }
];