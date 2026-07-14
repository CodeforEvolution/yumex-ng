%global app_id dk.yumex.Yumex
%global app_build release

Name:     yumex
Version:  5.5.0
Release:  %autorelease
Summary:  Yum Extender graphical package management tool

Group:    Applications/System
License:  GPL-3.0-or-later
URL:      https://github.com/timlau/yumex-ng
Source0:  %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: meson
BuildRequires: blueprint-compiler >= 0.18.0
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: systemd-rpm-macros

Requires: python3-gobject
Requires: libadwaita >= 1.8
Requires: gtk4
Requires: python3-dbus
Requires: flatpak-libs > 1.15.0
Requires: appstream >= 1.0.2

Recommends: %{name}-updater

# dnf5 requirements
Requires: dnf5daemon-server >= 5.2.12
Provides: yumex-dnf5 = %{version}-%{release}
Obsoletes: yumex-dnf5 < %{version}-%{release}

%description
Graphical package tool for maintain packages on the system.

%package -n %{name}-updater
Summary:  Yum Extender updater app
Requires: %{name} = %{version}-%{release}
Requires: python3-gobject
Requires: gtk3
Requires: python3-dbus
Requires: flatpak-libs > 1.15.0
Requires: libappindicator-gtk3

Provides: yumex-dnf5-updater-systray = %{version}-%{release}
Obsoletes: yumex-dnf5-updater-systray < %{version}-%{release}
Provides: yumex-updater-systray = %{version}-%{release}
Obsoletes: yumex-updater-systray < %{version}-%{release}

%description -n %{name}-updater
Daemon to check and notify about available updates.

%prep
%autosetup

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{app_id}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}-flatpakref.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}-rpm.desktop

%build
%meson --buildtype=%{app_build}
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f  %{name}.lang
%doc README.md
%license LICENSE
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/applications/%{app_id}-flatpakref.desktop
%{_datadir}/applications/%{app_id}-rpm.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml

%files -n %{name}-updater
%{_userunitdir}/%{name}-updater.service
%{_libexecdir}/%{name}-updater
%{_datadir}/icons/hicolor/scalable/apps/%{name}-update-*.svg

%changelog
%autochangelog
