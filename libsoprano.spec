%define name libsoprano
%define version	3.0
%define lib_name %mklibname soprano 3
%define date_package 20070514

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/


Name: 		%{name}
Summary: 	Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF.
Version: 	%{version}
Release:       %mkrel 0.%{date_package}.1
Epoch:		2
Group: 		System/Libraries
License: 	LGPL
URL: 		http://download.tuxfamily.org/eigen/
Source:		soprano-%version-%{date_package}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  cmake >= 2.4.5
BuildRequires: redland-devel
BuildRequires:  qt4-devel

%description
Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF storage solutions. 
It has a modular structure which allows to replace the actual RDF storage implementation used. 
Currently two implementations are working. 
The first and most important backend used in Soprano is based on librdf, the Redland RDF Application Framework.
The second backend is the more interesting one as it uses the NEPOMUK-KDE backbone library to connect to a 
NEPOMUK RDF triple service, thus providing a nice interface for applications not aware of Nepomuk services.


%package -n %{lib_name}
Summary:        Library for %name
Group:          Development/C

%description -n %{lib_name}
Library

%package -n %{lib_name}-devel
Summary: 	Library.
Group: 		Development/C
Provides: 	soprano-devel = %epoch:%{version}-%{release}
Requires:	%lib_name 

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n soprano-%version-%{date_package}

%build
cd $RPM_BUILD_DIR/soprano-%version-%{date_package}/
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
      -DCMAKE_BUILD_TYPE=Debug \
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/soprano-%version-%{date_package}/build/
make DESTDIR=%buildroot install




%clean 
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig


%files -n %{lib_name}
%defattr(-,root,root)
%_libdir/libsoprano.so.*
%dir %_libdir/soprano/
%_libdir/soprano/libsoprano_redlandbackend.so



%files -n %{lib_name}-devel
%defattr(-,root,root)
%dir %_includedir/soprano/
%_includedir/soprano/*.h
%_libdir/libsoprano.so


