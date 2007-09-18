%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 714066

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %{unstable}
%define dont_strip 1
%endif

Name: soprano
Summary: Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF.
Version: 3.0
Release: %mkrel 0.%{revision}.1
Epoch: 3
Group: System/Libraries
License: LGPL
URL: http://api.kde.org/kdesupport-api/kdesupport-apidocs/soprano/html/
Source:	soprano-%version.%{revision}.tar.bz2
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

#---------------------------------------------------------------------------------

%define libsoprano %mklibname soprano 3

%package -n %libsoprano
Summary: Library for %name
Group: Development/C

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
Summary: Library.
Group: Development/C
Provides: libsoprano-devel
Requires: %libsoprano
Obsoletes: %libsoprano-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files devel
%defattr(-,root,root)
%dir %_includedir/soprano/
%_includedir/soprano/*
%_libdir/*.so

#---------------------------------------------------------------------------------

%prep
%setup -q

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

