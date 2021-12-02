# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401


mod = "mod4"
terminal = "terminator"

keys = [

    # Custom launch commands
    #Key([mod], "r", lazy.spawn("dmenu_run"), desc="Launch Dmenu"),
    #Key([mod], "w", lazy.spawn("firefox-esr"), desc="Launch Firefox"),
    Key([mod], "r", lazy.spawncmd(), desc="Launch Prompt"),
    Key([mod], "w", lazy.spawn("brave"), desc="Launch Brave"),
    Key([mod], "e", lazy.spawn("code"), desc="Launch Code OSS"),
    #Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch Pcmanfm"),
    #Key([mod], "v", lazy.spawn("virtualbox"), desc="Launch Virtualbox"),


    # Custom volume commands
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc="Mute"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5"), desc="Volume dowm"),

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod, "control"], "p", lazy.spawn("poweroff"), desc="Shutdown"),
    Key(["mod4"], "l", lazy.spawn("betterlockscreen -l"), desc="Lock screen"),
]

group_names = [("WWW", {'layout': 'Columns'}),
               ("DEV", {'layout': 'Columns'}),
               ("SYS", {'layout': 'Columns'}),
               ("CHAT", {'layout': 'Columns'}),
               ("VBOX", {'layout': 'Columns'}),
               ("DOC", {'layout': 'Columns'}),
               ("MUS", {'layout': 'Columns'}),
               ("VID", {'layout': 'Columns'}),
               ("OTHER", {'layout': 'Columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

colors = [["#282c34", "#282c34"], # 0
          ["#3d3f4b", "#434758"], # 1
          ["#ffffff", "#ffffff"], # 2
          ["#AEC3B0", "#AEC3B0"], # 3
          ["#124559", "#124559"], # 4
          ["#598392", "#598392"], # 5
          ]

layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": colors[5],
                "border_normal": colors[1]
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict( font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                active = colors[2],
                inactive = colors[1],
                rounded = False,
                highlight_color = colors[1],
                highlight_method = "line",
                this_current_screen_border = colors[4],
                this_screen_border = colors [4],
                other_current_screen_border = colors[4],
                other_screen_border = colors[4],
                foreground = colors[2],
                background = colors[0]
                ),
                widget.Spacer(
                background=colors[0],
                length=10
                ),
                widget.WindowName(
                background=colors[0],
                foreground=colors[3]
                ),
                widget.Prompt(
                background=colors[0],
                prompt="Run: ",
                cursor=False
                ),
                widget.Spacer(
                background=colors[0],
                length=20
                ),
                widget.Systray(
                background=colors[0]
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
                widget.TextBox(
                background=colors[0],
                text='Volume:'
                ),
                widget.Volume(
                background=colors[0],
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
                widget.TextBox(
                background=colors[0],
                text='Battery:'
                ),
                widget.Battery(
                format='{percent:2.0%}  {char}',
                background=colors[0]
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
                widget.Clock(
                format='%m-%d %H:%M',
                background=colors[0]
                ),
                widget.Spacer(
                background=colors[0],
                length=5
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, "shift"], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
