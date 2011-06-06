#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pynotify

pynotify.init('scru_notify')


def show_notification(title, message, image=None):
    """Show a notification message"""
    pynotify.init('Scru')
    n = pynotify.Notification(title, message, image)
    n.set_hint_string('append', '')
    try:
        n.show()
    # Not notify daemon installed
    # NOtify OSD, Notification-daemon-xfce, notification-daemon, etc
    except glib.GError:
        pass
