def generate_alert(count, density, thresholds, scene_info):

    warning_threshold = thresholds["warning"]
    critical_threshold = thresholds["critical"]

    if count >= critical_threshold:
        status = "CRITICAL"
        suggestion = "Immediate crowd control required!"
    elif count >= warning_threshold:
        status = "WARNING"
        suggestion = "Crowd building up. Monitor closely."
    else:
        status = "NORMAL"
        suggestion = "Crowd level is safe."

    return status, suggestion
