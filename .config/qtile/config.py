# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook

from typing import List  # noqa: F401

mod = "mod4"


##### COLORS #####
colors = [
    ["#282a36", "#282a36"],  # panel background
    ["#434758", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
    ["#668bd7", "#668bd7"],  # color for the even widgets
    ["#e1acff", "#e1acff"],  # window name
]

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="Ubuntu Mono", fontsize=12, padding=2, background=colors[2])
extension_defaults = widget_defaults.copy()


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),
    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("alacritty")),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

##### GROUPS #####
group_names = [
    ("TERM", {"layout": "max"}),
    ("WWW", {"layout": "max"}),
    ("CODE", {"layout": "monadtall"}),
    ("DOC", {"layout": "monadtall"}),
    ("VBOX", {"layout": "monadtall"}),
    ("CHAT", {"layout": "monadtall"}),
    ("MUS", {"layout": "monadtall"}),
    ("VID", {"layout": "monadtall"}),
    ("TIME", {"layout": "floating"}),
]

# groups = [Group(i) for i in "123456789"]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )  # Send current window to another group


# for i in groups:
#    keys.extend(
#        [
#            # mod1 + letter of group = switch to group
#            Key([mod], i.name, lazy.group[i.name].toscreen()),
#            # mod1 + shift + letter of group = switch to & move focused window to group
#            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
#            # Or, use below if you prefer not to switch to that group.
#            # # mod1 + shift + letter of group = move focused window to group
#            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
#        ]
#    )

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 1,
    "margin": 3,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}

layouts = [
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2, **layout_theme),
    layout.Floating(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(font="Consolas", fontsize=14, padding=2, background=colors[0])
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="Consolas Bold",
                    disable_drag=True,
                    fontsize=10,
                    margin_y=3,
                    margin_x=5,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[2],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[3],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[0],
                ),
                widget.Prompt(),
                widget.Sep(foreground="000000", padding=10),
                widget.WindowName(),
                # widget.Systray(),
                # Right side:
                widget.KeyboardLayout(
                    configured_keyboards=["us", "ar"], font="Consolas Bold"
                ),
                widget.CurrentLayout(),
                widget.DF(
                    visible_on_warn=False,
                    partition="/var",
                    format="[ {p} ({uf}{m}|{r:.0f}%) ]",
                ),
                widget.Battery(
                    font="Ubuntu",
                    charge_char="🗲",
                    discharge_char="▼",
                    format="{char} {percent:2.0%}",
                ),
                widget.TextBox(
                    text="",
                    background=colors[4],
                    foreground=colors[5],
                    padding=0,
                    fontsize=37,
                ),
                widget.TextBox(
                    text=" Vol:", foreground=colors[2], background=colors[5], padding=0
                ),
                widget.Volume(foreground=colors[2], background=colors[5], padding=5),
                widget.TextBox(
                    text="",
                    background=colors[5],
                    foreground=colors[4],
                    padding=0,
                    fontsize=37,
                ),
                widget.Net(
                    interface="wlp110s0",
                    format="{down} ↓↑ {up}",
                    foreground=colors[2],
                    background=colors[4],
                    padding=5,
                ),
                # widget.MemoryGraph(
                # foreground = colors[2],
                # background = colors[5],
                # padding = 5
                # ),
                # widget.QuickExit(),
                widget.TextBox(
                    text="",
                    background=colors[4],
                    foreground=colors[5],
                    padding=0,
                    fontsize=37,
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    foreground=colors[2],
                    background=colors[5],
                ),
                widget.Systray(background=colors[0], padding=10),
                widget.Notify(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
