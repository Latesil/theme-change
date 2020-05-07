# theme-switcher

A global automated switcher for dark/light GTK theme during day/night and more.

Theme-switcher automatically can switch your:

- GTK theme
- GNOME Terminal profiles
- Wallpapers
- More will come...
<p align="center">
  <img src="https://raw.githubusercontent.com/Latesil/theme-switcher/master/theme-switcher-screenshot-1.png" style="max-width:666px;">
</p>

### Prerequisites for building from source

```sh
sudo dnf install python3-gobject gtk3
sudo cp com.github.Latesil.theme-switcher.gschema.xml /usr/share/glib-2.0/schemas/
sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
```

### Install

Fedora [COPR](https://copr.fedorainfracloud.org/coprs/atim/theme-switcher/):

```
sudo dnf copr enable atim/theme-switcher -y
sudo dnf install theme-switcher -y
```

### Run GUI version:

```sh
theme-switcher-gui
```

### Run CLI version

#### Automatically

- Enable: `systemctl --user enable --now theme-switcher-auto.timer`

- Disable: `systemctl --user disable --now theme-switcher-auto.timer`

#### Manually:

```sh
theme-switcher-manual.py
```
