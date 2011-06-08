#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pynotify

pynotify.init('scru_notify')
#TODO: notify-send --hint=int:transient:1 -t 3000 -u normal

def show_notification(title, message, image=None):
    """Show a notification message"""
    pynotify.init('Scru')
    n = pynotify.Notification(title, message, image)
    n.set_hint_string('append', '')
    n.set_hint('transient', True)
    n.set_urgency(pynotify.URGENCY_NORMAL)
    n.set_timeout(5000)
    try:
        if not n.show():
            print "Failed to send notification"
    # Not notify daemon installed
    # NOtify OSD, Notification-daemon-xfce, notification-daemon, etc
    except glib.GError:
        pass
