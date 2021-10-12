# ~~WIP~~

![Development abandoned](https://img.shields.io/badge/development-abandoned-%23F7CA88.svg?labelColor=585858&style=for-the-badge&logoColor=FFFFFF "Development abandoned")

Use [Nix](https://nixos.org) instead.

---

A "all for one" package manager, a package manager wrapper that works on any distro that finds and matches an exact package between the package manager using [Repology](https://repology.org).

Example:

```sh
bpack install godot
```

|Package manager                                                 |What it's actually run     |
|----------------------------------------------------------------|---------------------------|
|[APT](https://wiki.debian.org/Apt)                              |`apt install godot3`       |
|[AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository)|`yay -Sy godot-bin`        |
|[XBPS](https://docs.voidlinux.org/xbps/index.html)              |`xbps-install --sync godot`|
