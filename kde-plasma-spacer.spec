Name: kde-plasma-spacer
Version: 0.10
Release: %(date +%Y%m%d_%H%M)%{?dist}
Summary: Simple spacer for KDE panels.
Summary(ru): Спейсер для панелей KDE.
License: GPL
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: https://github.com/F1ash/plasmaSimpleSpacer
BuildArch: noarch

%if %{defined fedora}
Requires: python >= 2.6, PyQt4 >= 4.7, PyKDE4 >= 4.6
Conflicts: python >= 3.0
BuildRequires: desktop-file-utils
%endif

%description
kde-plasma-spacer
Simple spacer for KDE panels.

%description -l ru
kde-plasma-spacer
Спейсер для панелей KDE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_kde4_appsdir}/plasma/plasmoids/%{name}
cp -r * $RPM_BUILD_ROOT/%{_kde4_appsdir}/plasma/plasmoids/%{name}/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/kde4/services
cp -r metadata.desktop $RPM_BUILD_ROOT/%{_datadir}/kde4/services/%{name}.desktop


%files
%defattr(-,root,root)
%{_datadir}/kde4/services/%{name}.desktop
%{_kde4_appsdir}/plasma/plasmoids/%{name}/*
%dir %{_kde4_appsdir}/plasma/plasmoids/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Sun Aug 21 2011 Fl@sh <no@mail.me>	-	0.1
-- Build began ;)

