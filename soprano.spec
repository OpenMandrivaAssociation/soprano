%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 725573

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %{unstable}
%define dont_strip 1
%endif

%define icedtea_version 1.7.0.0
%ifarch x86_64
%define icedtea_dir /usr/lib/jvm/java-1.7.0-icedtea-%{icedtea_version}.x86_64
%else
%define icedtea_dir /usr/lib/jvm/java-1.7.0-icedtea-%{icedtea_version}
%endif

Name: soprano
Summary: Soprano (formally known as QRDF) is a library which provides a nice QT interface to RDF
Version: 1.97.0
%if %branch
Release: %mkrel 0.%{revision}.5
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
BuildRequires: qt4-devel
BuildRequires: clucene-devel
BuildRequires: java-1.7.0-icedtea-devel = %{icedtea_version}
BuildRequires: doxygen

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
%_datadir/soprano/plugins/sesame2backend.desktop
%_datadir/soprano/sesame2/openrdf-sesame-2.0-beta5-onejar.jar
%_datadir/soprano/sesame2/slf4j-api-1.4.2.jar
%_datadir/soprano/sesame2/slf4j-simple-1.4.2.jar

#---------------------------------------------------------------------------------

%define libsopranomajor 4
%define libsopranoclientservermajor 1
%define libsopranoindexmajor 1
%define libsoprano %mklibname soprano %libsopranomajor

%package -n %libsoprano
Summary:    Library for %name
Group:      Development/C
Requires:   %name
# fwang: because in such release, it names as libfoo3, but it contains libfoo4
Conflicts:  %{mklibname soprano 3} = 4:1.97.0-%{mkrel -c 724490 1}

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
%_libdir/libsoprano.so.%{libsopranomajor}*
%_libdir/libsopranoclient.so.%{libsopranoclientservermajor}*
%_libdir/libsopranoserver.so.%{libsopranoclientservermajor}*
%_libdir/libsopranoindex.so.%{libsopranoindexmajor}*
%dir %_libdir/soprano
%_libdir/soprano/*

#---------------------------------------------------------------------------------

%package devel
Summary: Library
Group: Development/C
Provides: libsoprano-devel
Requires: %libsoprano = %{epoch}:%version-%release
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
	-DCMAKE_BUILD_TYPE=debugfull \
	-DJAVA_INCLUDE_PATH=%{icedtea_dir}/include/
	-DJAVA_JVM_LIBRARY=%{icedtea_dir}/lib/
%endif

%make


%install
rm -rf %buildroot
cd build && make DESTDIR=%buildroot install

%clean 
rm -rf %buildroot

