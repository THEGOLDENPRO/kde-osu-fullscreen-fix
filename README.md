<div align="center">

  # 🟣 koff

  <sub>Temporary KDE osu! full screen fix.</sub>

  ![showcase video](./assets/koff_showcase.mp4)

</div>

There's currently an issue with osu! lazer on KDE where the game will launch minimized in the corner despite it being set to full screen. (The issue can be discussed here: https://github.com/ppy/osu/discussions/26241)

A quick fix for this is to re-toggle full screen by taping ``f11`` or ``ctrl + alt`` but well you see... I'm just too lazy... so I made a python script to do it for me.

🟣 Koff (aka "KDE osu full-screen fix") is a small python daemon that automatically full screens osu! for you on launch as a temporary fix for this issue.