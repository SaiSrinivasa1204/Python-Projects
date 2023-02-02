from plyer import notification
title = "Go to get juice"

message = "At 11.30 go and get sugarcane juice"

notification.notify(title=title, message=message, app_icon="", timeout=30, toast=False)
