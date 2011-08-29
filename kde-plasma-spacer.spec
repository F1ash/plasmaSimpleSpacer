Name: kde-plasma-spacer
Version: 0.10
Release: 3%{?dist}
Summary: Simple spacer for KDE panels.
Summary(ru): Спейсер для панелей KDE.
Group: Applications/Miscellanious
License: GPL
Source0: http://cloud.github.com/downloads/F1ash/plasmaSimpleSpacer/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: https://github.com/F1ash/plasmaSimpleSpacer
BuildArch: noarch

Requires: python, PyQt4, PyKDE4

%description
kde-plasma-spacer
Simple spacer for KDE panels.

%description -l ru
kde-plasma-spacer
Спейсер для панелей KDE.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT/usr

%files
%defattr(-,root,root)
%{_datadir}/kde4/services/%{name}.desktop
%{_datadir}/kde4/apps/plasma/plasmoids/%{name}/*
%dir %{_datadir}/kde4/apps/plasma/plasmoids/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Mon Aug 29 2011 Fl@sh <kaperang07@gmail.com> - 0.10-3
- fixed Makefile

* Mon Aug 29 2011 Fl@sh <kaperang07@gmail.com> - 0.10-2
- fixed Makefile

* Mon Aug 22 2011 Fl@sh <kaperang07@gmail.com> - 0.10-1
- Initial build
