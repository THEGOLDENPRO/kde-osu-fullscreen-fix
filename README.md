<div align="center">

  # 🟣 koff

  <sub>Temporary KDE osu! full screen fix.</sub>

  [!showcase video](https://github.com/THEGOLDENPRO/kde-osu-fullscreen-fix/assets/66202304/5e65223a-c01f-4cf6-a2ec-451777e910f0)

</div>

> [!WARNING]
> This script is only compatible with Wayland *but may actually not be limited to the KDE desktop environment*.
> Also systemd is required.

> [!NOTE]
> **The issue is now [fixed](https://github.com/ppy/osu/discussions/26241#discussioncomment-9501639) so this script is no longer needed. It will now be archived. 👋**

# ❓ What is this?
There's currently an issue with osu! lazer on KDE where the game will launch minimized in the corner despite it being set to full screen. (The issue can be discussed here: https://github.com/ppy/osu/discussions/26241)

A quick fix for this is to re-toggle full screen by taping ``f11`` or ``ctrl + alt`` but well you see... I'm just too lazy... so I made a python script to do it for me.

🟣 Koff (aka "KDE osu full-screen fix") is a small python daemon that automatically full screens osu! for you on launch as a temporary fix for that [issue](https://github.com/ppy/osu/discussions/26241).

# 🛠️ Installation
Before installing the script you first must install [dotool](https://git.sr.ht/~geb/dotool) for you distribution. (NOT "**x**dotool", "dotool"!)

On arch it's available on the [AUR](https://aur.archlinux.org/packages/dotool):
```sh
yay -S dotool
```

Then you can clone the repo and install the daemon from source:
```sh
git clone https://github.com/THEGOLDENPRO/kde-osu-fullscreen-fix
cd kde-osu-fullscreen-fix
make
make install
```

Then start it with systemd:
```sh
systemctl --user enable koff
systemctl --user start koff
```

# 🔮 How to change defaults?
You may want to adjust the defaults like example, increase the default delay time of when f11 is pressed. You can do so by overriding the .service via systemd with environment variables like so:
```sh
systemctl --user edit koff
```
then edit that file with your environment variables like so:
```toml
[Service]
Environment="KOFF_DELAY=4"
Environment="KOFF_REPEAT_AMOUNT=3"
Environment="KOFF_POLLING_RATE=4"
```
then restart the daemon:
```sh
systemctl --user restart koff
```
