import requests

topic = "dailyreminder"
title = "Daily Reminder"
message = "Life's simple, you make choices and don't look back"

requests.post(
    f"https://ntfy.sh/{topic}",
    headers={
        "Title": title,
        "Priority": "high",
        "Tags": "white_check_mark"
    },
    data=message.encode("utf-8")
)


