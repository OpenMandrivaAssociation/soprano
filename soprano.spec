%ifarch %{arm} %{mips}
%bcond_with java
%else
%bcond_without java
%endif

%if %{with java}
# Do not require java stuff just because we have a java backend
%if %{_use_internal_dependency_generator}
%define __noautoreq 'libjvm\\.so(.*)'
%else
%define _requires_exceptions libjvm\.so
%endif
%endif

%bcond_with clucene

Summary:	Library which provides a nice QT interface to RDF
Name:		soprano
Version:	2.9.4
Release:	9
Epoch:		4
License:	LGPLv2+
Group:		System/Libraries
Url:		http://soprano.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/soprano/Soprano/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	cmake >= 2.6.2
BuildRequires:	pkgconfig(redland) >= 1.0.6
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(libiodbc)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtXml)
BuildRequires:	pkgconfig(QtDBus)
BuildRequires:	kde4-macros
%if %{with java}
BuildRequires:	java-rpmbuild
BuildRequires:	java-devel
BuildRequires:	chrpath
%endif
%if %{with clucene}
BuildRequires:	clucene-devel
%else
BuildConflicts:	clucene-devel
Obsoletes:	%{mklibname sopranoindex 1} < %{EVRD}
%endif
BuildRequires:	doxygen
Requires:	soprano-plugin-virtuoso = %{EVRD}

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
%{_bindir}/sopranocmd
%{_bindir}/sopranod
%dir %{_datadir}/soprano
%{_datadir}/soprano/rules

#---------------------------------------------------------------------------------

%if %{with java}
%package plugin-sesame2
Summary:	Sesame2 soprano plugin
Group:		System/Libraries
Requires:	soprano-plugin-common = %{EVRD}
Requires:	java

%description plugin-sesame2
This package provide the sesame2 java indexer plugin for soprano.

%files plugin-sesame2
%dir %{_datadir}/soprano/plugins
%{_datadir}/soprano/plugins/sesame2backend.desktop
%{_datadir}/soprano/sesame2
%dir %{_libdir}/soprano
%{_libdir}/soprano/libsoprano_sesame2backend.so
%endif

#---------------------------------------------------------------------------------

%package plugin-virtuoso
Summary:	Virtuoso soprano plugin
Group:		System/Libraries
Requires:	virtuoso-opensource >= 5.0.12
Requires:	soprano-plugin-common = %{EVRD}

%description plugin-virtuoso
This package provide the virtuoso plugin for soprano.

%files plugin-virtuoso
%dir %{_datadir}/soprano/plugins
%{_datadir}/soprano/plugins/virtuosobackend.desktop
%dir %{_libdir}/soprano
%{_libdir}/soprano/libsoprano_virtuosobackend.so

#---------------------------------------------------------------------------------

%package plugin-redland
Summary:	redland soprano plugin
Group:		System/Libraries
Requires:	soprano-plugin-common = %{EVRD}

%description plugin-redland
This package provide the redland indexer plugin for soprano.

%files plugin-redland
%dir %{_datadir}/soprano/plugins
%{_datadir}/soprano/plugins/redlandbackend.desktop
%dir %{_libdir}/soprano
%{_libdir}/soprano/libsoprano_redlandbackend.so

#---------------------------------------------------------------------------------

%package plugin-common
Summary:	Common parsers and serializers
Group:		System/Libraries

%description plugin-common
Common parser and serializers

%files plugin-common
%dir %{_datadir}/soprano/plugins
%{_datadir}/soprano/plugins/*parser.desktop
%{_datadir}/soprano/plugins/*serializer.desktop
%dir %{_libdir}/soprano
%{_libdir}/soprano/libsoprano_*serializer.so
%{_libdir}/soprano/libsoprano_*parser.so

#---------------------------------------------------------------------------------

%define libsopranomajor 4
%define libsoprano %mklibname soprano %{libsopranomajor}

%package -n %{libsoprano}
Summary:	Library for %{name}
Group:		Development/C

%description -n %{libsoprano}
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%files -n %{libsoprano}
%{_libdir}/libsoprano.so.%{libsopranomajor}*

#---------------------------------------------------------------------------------

%define sopranoclient_major 1
%define libsopranoclient %mklibname sopranoclient %{sopranoclient_major}

%package -n %{libsopranoclient}
Summary:	Library for %{name}
Group:		Development/C

%description -n %{libsopranoclient}
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%files -n %{libsopranoclient}
%{_libdir}/libsopranoclient.so.%{sopranoclient_major}*

#---------------------------------------------------------------------------------

%define sopranoserver_major 1
%define libsopranoserver %mklibname sopranoserver %{sopranoserver_major}

%package -n %{libsopranoserver}
Summary:	Library for %{name}
Group:		Development/C

%description -n %{libsopranoserver}
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%files -n %{libsopranoserver}
%{_libdir}/libsopranoserver.so.%{sopranoserver_major}*

#---------------------------------------------------------------------------------

%if %{with clucene}
%define sopranoindex_major 1
%define libsopranoindex %mklibname sopranoindex %{sopranoindex_major}

%package -n %{libsopranoindex}
Summary:	Library for %{name}
Group:		Development/C

%description -n %{libsopranoindex}
Soprano (formally known as QRDF) is a library which provides a nice QT
interface to RDF storage solutions.  It has a modular structure which allows to
replace the actual RDF storage implementation used.  Currently two
implementations are working.  The first and most important backend used in
Soprano is based on librdf, the Redland RDF Application Framework.  The second
backend is the more interesting one as it uses the NEPOMUK-KDE backbone library
to connect to a NEPOMUK RDF triple service, thus providing a nice interface for
applications not aware of Nepomuk services.

%files -n %{libsopranoindex}
%{_libdir}/libsopranoindex.so.%{sopranoindex_major}*
%endif

#---------------------------------------------------------------------------------

%package devel
Summary:	Library
Group:		Development/C
Provides:	libsoprano-devel = %{EVRD}
Requires:	%{libsoprano} = %{EVRD}
Obsoletes:	%{libsoprano}-devel < 3:3.0-0.714066.1
Requires:	%{libsoprano} = %{EVRD}
Requires:	%{libsopranoclient} = %{EVRD}
Requires:	%{libsopranoserver} = %{EVRD}
%if %{with clucene}
Requires:	%{libsopranoindex} = %{EVRD}
%endif
Requires:	soprano = %{EVRD}
Requires:	%{name}-plugin-virtuoso = %{EVRD}
Requires:	%{name}-plugin-redland = %{EVRD}

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files devel
%{_bindir}/onto2vocabularyclass
%dir %{_includedir}/soprano/
%{_includedir}/soprano/*
%dir %{_includedir}/Soprano/
%{_includedir}/Soprano/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/soprano/cmake

#---------------------------------------------------------------------------------

%prep
%setup -q

%build
%if %{with java}
export JAVA_HOME=%{java_home}
%endif

%cmake_qt4 \
%if !%{with clucene}
	-DSOPRANO_DISABLE_CLUCENE_INDEX=True
%endif

%make

%install
%makeinstall_std -C build

%if %{with java}
# Load libjvm.so from the JRE directory instead of SDK directory. This
# works with Sun-derived JREs, but GCJ/Jamvm etc have libjvm.so in different
# directories. Maybe there should be an alternative pointing to libjvm.so.
old_rpath=$(chrpath -l %{buildroot}%{_libdir}/soprano/libsoprano_sesame2backend.so | cut -d= -f2)
new_rpath=$(echo "$old_rpath" | sed "s,%{java_home},%{_jvmdir},")
chrpath -r "$new_rpath" %{buildroot}%{_libdir}/soprano/libsoprano_sesame2backend.so
%endif

