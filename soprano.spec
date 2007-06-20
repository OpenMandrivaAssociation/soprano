%define date_package 20070614

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %{unstable}
%define dont_strip 1
%endif

Name: soprano
Summary: Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF.
Version: 3.0
Release: %mkrel 0.%{date_package}.1
Epoch: 2
Group: System/Libraries
License: LGPL
URL: http://api.kde.org/kdesupport-api/kdesupport-apidocs/soprano/html/
Source:	soprano-%version.%{date_package}.tar.bz2
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
mkdir build && cd build
export QTDIR=%qt4dir
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %unstable
      -DCMAKE_BUILD_TYPE=debugfull \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -rf %buildroot
cd build && make DESTDIR=%buildroot install

%clean 
rm -rf %buildroot

