%define revision 983983

%define with_java 1
%{?_with_java: %{expand: %%global with_java 1}}

%if %{with_java}
# Do not require java stuff just because we have a java backend
%define _requires_exceptions libjvm\.so
%endif

Name: soprano
Summary: Library which provides a nice QT interface to RDF
Version: 2.2.69
Release: %mkrel 3
Epoch: 4
Group: System/Libraries
License: LGPLv2+
URL: http://soprano.sourceforge.net
Source: soprano-%version.tar.bz2
Patch0: soprano-2.2.69-use-proper-sql-types.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.6.2
BuildRequires: redland-devel >= 1.0.6
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: clucene-devel >= 0.9.19
BuildRequires: kde4-macros
%if %with_java
BuildRequires: java-rpmbuild
BuildRequires: chrpath
Suggests: soprano-plugin-sesame2
%endif
BuildRequires: doxygen
BuildRequires: iodbc-devel
Suggests: soprano-plugin-redland
Suggests: soprano-plugin-virtuoso


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
%dir %_datadir/soprano
%_datadir/soprano/rules

#---------------------------------------------------------------------------------

%if %with_java
%package    plugin-sesame2
Summary:    Sesame2 soprano plugin
Group:      System/Libraries
Obsoletes:  %{_lib}soprano3 < 4:1.97.0-0.725573.5
Obsoletes:  soprano < 4:2.2.69
Obsoletes:  %{_lib}soprano4 < 4:2.2.69
Requires:   soprano-plugin-common

%description plugin-sesame2
This package provide the sesame2 plugin for soprano.

%files plugin-sesame2
%defattr(-,root,root)
%dir %_datadir/soprano/plugins
%_datadir/soprano/plugins/sesame2backend.desktop
%_datadir/soprano/sesame2
%dir %_libdir/soprano
%_libdir/soprano/libsoprano_sesame2backend.so
%endif

#---------------------------------------------------------------------------------

%package    plugin-virtuoso
Summary:    Virtuoso soprano plugin
Group:      System/Libraries
Obsoletes:  soprano < 4:2.2.69
Obsoletes:  %{_lib}soprano4 < 4:2.2.69
Requires:   virtuoso-opensource
Requires:   soprano-plugin-common

%description plugin-virtuoso
This package provide the virtuoso plugin for soprano.

%files plugin-virtuoso
%defattr(-,root,root)
%dir %_datadir/soprano/plugins
%_datadir/soprano/plugins/virtuosobackend.desktop
%dir %_libdir/soprano
%_libdir/soprano/libsoprano_virtuosobackend.so

#---------------------------------------------------------------------------------

%package    plugin-redland
Summary:    redland soprano plugin
Group:      System/Libraries
Obsoletes:  soprano < 4:2.2.69
Obsoletes:  %{_lib}soprano4 < 4:2.2.69
Requires:   soprano-plugin-common

%description plugin-redland
This package provide the redland plugin for soprano.

%files plugin-redland
%defattr(-,root,root)
%dir %_datadir/soprano/plugins
%_datadir/soprano/plugins/redlandbackend.desktop
%dir %_libdir/soprano
%_libdir/soprano/libsoprano_redlandbackend.so

#---------------------------------------------------------------------------------

%package    plugin-common
Summary:    Common parsers and serializers
Group:      System/Libraries
Obsoletes:  soprano < 4:2.2.69
Obsoletes:  %{_lib}soprano4 < 4:2.2.69

%description plugin-common
Common parser and serializers

%files plugin-common
%defattr(-,root,root)
%dir %_datadir/soprano/plugins
%_datadir/soprano/plugins/*parser.desktop
%_datadir/soprano/plugins/*serializer.desktop
%dir %_libdir/soprano
%_libdir/soprano/libsoprano_*serializer.so
%_libdir/soprano/libsoprano_*parser.so

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

%files -n %libsoprano
%defattr(-,root,root)
%_libdir/libsoprano.so.%{libsopranomajor}*

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

%files -n %libsopranoindex
%defattr(-,root,root)
%_libdir/libsopranoindex.so.*

#---------------------------------------------------------------------------------

%package  devel
Summary:  Library
Group:    Development/C
Provides: libsoprano-devel
Requires: %libsoprano = %{epoch}:%version-%release
Obsoletes:%libsoprano-devel < 3:3.0-0.714066.1
Requires: %libsoprano = %{epoch}:%version-%release
Requires: %libsopranoclient = %{epoch}:%version-%release
Requires: %libsopranoserver = %{epoch}:%version-%release
Requires: %libsopranoindex = %{epoch}:%version-%release
Requires: %name-plugin-sesame2
Requires: %name-plugin-virtuoso

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
%_datadir/dbus-1/interfaces/*
%_kde_appsdir/cmake/modules/SopranoAddOntology.cmake

#---------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%if %with_java
export JAVA_HOME=%{java_home}
%endif

%cmake_qt4 

%make


%install
rm -rf %buildroot
%makeinstall_std -C build

%if %with_java
# Load libjvm.so from the JRE directory instead of SDK directory. This
# works with Sun-derived JREs, but GCJ/Jamvm etc have libjvm.so in different
# directories. Maybe there should be an alternative pointing to libjvm.so.
old_rpath=$(chrpath -l %{buildroot}%{_libdir}/soprano/libsoprano_sesame2backend.so | cut -d= -f2)
new_rpath=$(echo "$old_rpath" | sed "s,%{java_home},%{_jvmdir},")
chrpath -r "$new_rpath" %{buildroot}%{_libdir}/soprano/libsoprano_sesame2backend.so
%endif

%clean 
rm -rf %buildroot

