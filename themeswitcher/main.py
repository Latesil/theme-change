#!/usr/bin/python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import locale
import os
import sys
from locale import gettext as _

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, GLib, Gtk

from .new_main_window import AppWindow

# locales
locale.textdomain('com.github.Latesil.theme-switcher')


def main():
    app = Application()
    return app.run(sys.argv)


class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.github.Latesil.theme-switcher",
                         flags=Gio.ApplicationFlags.FLAGS_NONE, **kwargs)

        GLib.set_application_name(_('Theme Switcher'))
        # GLib.set_prgname('Theme Switcher')

    def do_activate(self):
        window = self.props.active_window
        if not window:
            window = AppWindow(application=self)
        window.present()
