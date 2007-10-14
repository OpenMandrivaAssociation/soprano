%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 724490

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %{unstable}
%define dont_strip 1
%endif

Name: soprano
Summary: Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF
Version: 1.97.0
%if %branch
Release: %mkrel 0.%{revision}.1
%else
Release: %mkrel 0.1
%endif
Epoch: 4
Group: System/Libraries
License: LGPL
URL: http://api.kde.org/kdesupport-api/kdesupport-apidocs/soprano/html/
%if %branch
Source: soprano-%version.%{revision}.tar.bz2
%else
Source: soprano-%version.tar.bz2
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.4.5
BuildRequires: redland-devel
BuildRequires: qt4-devel

%description
Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF storage solutions. 
It has a modular structure which allows to replace the actual RDF storage implementation used. 
Currently two implementations are working. 
The first and most important backend used in Soprano is based on librdf, the Redland RDF Application Framework.
The second backend is the more interesting one as it uses the NEPOMUK-KDE backbone library to connect to a 
NEPOMUK RDF triple service, thus providing a nice interface for applications not aware of Nepomuk services.

%files
%defattr(-,root,root)
%_bindir/sopranocmd
%_bindir/sopranod
%_datadir/dbus-1/interfaces/org.soprano.Model.xml
%_datadir/dbus-1/interfaces/org.soprano.NodeIterator.xml
%_datadir/dbus-1/interfaces/org.soprano.QueryResultIterator.xml
%_datadir/dbus-1/interfaces/org.soprano.Server.xml
%_datadir/dbus-1/interfaces/org.soprano.StatementIterator.xml
%_datadir/soprano/plugins/raptorparser.desktop
%_datadir/soprano/plugins/raptorserializer.desktop
%_datadir/soprano/plugins/redlandbackend.desktop
%_datadir/soprano/rules/nrl.rules
%_datadir/soprano/rules/rdfs.rules

#---------------------------------------------------------------------------------

%define libsoprano %mklibname soprano 3

%package -n %libsoprano
Summary:    Library for %name
Group:      Development/C
Requires:   %name

%description -n %libsoprano
Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF storage solutions. 
It has a modular structure which allows to replace the actual RDF storage implementation used. 
Currently two implementations are working. 
The first and most important backend used in Soprano is based on librdf, the Redland RDF Application Framework.
The second backend is the more interesting one as it uses the NEPOMUK-KDE backbone library to connect to a 
NEPOMUK RDF triple service, thus providing a nice interface for applications not aware of Nepomuk services.

%post -n %libsoprano -p /sbin/ldconfig
%postun -n %libsoprano -p /sbin/ldconfig

%files -n %libsoprano
%defattr(-,root,root)
%_libdir/*.so.*
%dir %_libdir/soprano
%_libdir/soprano/*

#---------------------------------------------------------------------------------

%package devel
Summary: Library
Group: Development/C
Provides: libsoprano-devel
Requires: %libsoprano
Obsoletes: %libsoprano-devel < 3:3.0-0.714066.1

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files devel
%defattr(-,root,root)
%dir %_includedir/soprano/
%_includedir/soprano/*
%dir %_includedir/Soprano/
%_includedir/Soprano/*
%_libdir/pkgconfig/soprano.pc
%_libdir/*.so
#---------------------------------------------------------------------------------

%prep
%if ! %branch
%setup -q -n %name
%else
%setup -q -n %name-%version
%endif

%build
%cmake_qt4 \
%if %unstable
      -DCMAKE_BUILD_TYPE=debugfull 
%endif

%make


%install
rm -rf %buildroot
cd build && make DESTDIR=%buildroot install

%clean 
rm -rf %buildroot

