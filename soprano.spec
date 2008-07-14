%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 804023

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define with_java 1
%{?_with_java: %{expand: %%global with_java 1}}

%if %{unstable}
%define dont_strip 1
%endif

Name: soprano
Summary: Library which provides a nice QT interface to RDF
Version: 2.0.99
%if %branch
Release: %mkrel 0.%{revision}.4
%else
Release: %mkrel 1
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
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: clucene-devel
%if %with_java
BuildRequires: java-1.6.0-openjdk-devel
%endif
BuildRequires: doxygen

%description
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%files
%defattr(-,root,root)
%_bindir/sopranocmd
%_bindir/sopranod
%_bindir/onto2vocabularyclass
%dir %_datadir/soprano/
%_datadir/soprano/*

#---------------------------------------------------------------------------------

%define libsopranomajor 4
%define libsoprano %mklibname soprano %libsopranomajor

%package -n %libsoprano
Summary:    Library for %name
Group:      Development/C
Requires:   %name
Obsoletes: %{_lib}soprano3 < 4:1.97.0-0.725573.5

%description -n %libsoprano
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%if %mdkversion < 200900
%post -n %libsoprano -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsoprano -p /sbin/ldconfig
%endif

%files -n %libsoprano
%defattr(-,root,root)
%_libdir/libsoprano.so.%{libsopranomajor}*
%dir %_libdir/soprano
%_libdir/soprano/*

#---------------------------------------------------------------------------------

%define libsopranoclient %mklibname sopranoclient 1

%package -n %libsopranoclient
Summary: Library for %name
Group: Development/C
Requires: %name
Obsoletes: %{_lib}soprano3 < 4:1.97.0-0.725573.5

%description -n %libsopranoclient
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%if %mdkversion < 200900
%post -n %libsopranoclient -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsopranoclient -p /sbin/ldconfig
%endif

%files -n %libsopranoclient
%defattr(-,root,root)
%_libdir/libsopranoclient.so.*

#---------------------------------------------------------------------------------

%define libsopranoserver %mklibname sopranoserver 1

%package -n %libsopranoserver
Summary: Library for %name
Group: Development/C
Requires: %name
Obsoletes: %{_lib}soprano3 < 4:1.97.0-0.725573.5

%description -n %libsopranoserver
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%if %mdkversion < 200900
%post -n %libsopranoserver -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsopranoserver -p /sbin/ldconfig
%endif

%files -n %libsopranoserver
%defattr(-,root,root)
%_libdir/libsopranoserver.so.*

#---------------------------------------------------------------------------------

%define libsopranoindex %mklibname sopranoindex 1

%package -n %libsopranoindex
Summary: Library for %name
Group: Development/C
Requires: %name
Obsoletes: %{_lib}soprano3 < 4:1.97.0-0.725573.5

%description -n %libsopranoindex
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%if %mdkversion < 200900
%post -n %libsopranoindex -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsopranoindex -p /sbin/ldconfig
%endif

%files -n %libsopranoindex
%defattr(-,root,root)
%_libdir/libsopranoindex.so.*

#---------------------------------------------------------------------------------

%package devel
Summary: Library
Group: Development/C
Provides: libsoprano-devel
Requires: %libsoprano = %{epoch}:%version-%release
Obsoletes: %libsoprano-devel < 3:3.0-0.714066.1
Requires: %libsoprano = %{epoch}:%version-%release
Requires: %libsopranoclient = %{epoch}:%version-%release
Requires: %libsopranoserver = %{epoch}:%version-%release
Requires: %libsopranoindex = %{epoch}:%version-%release

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
%_kde_datadir/dbus-1/interfaces/*

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
	-DCMAKE_BUILD_TYPE=debugfull \
%if %with_java
	-DJAVA_INCLUDE_PATH=/usr/lib/jvm/java-1.6.0-openjdk/include/ \
	-DJAVA_JVM_LIBRARY=/usr/lib/jvm/java-1.6.0-openjdk/include/
%endif
%endif

%make


%install
rm -rf %buildroot
cd build && make DESTDIR=%buildroot install

%clean 
rm -rf %buildroot

