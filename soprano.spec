%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define revision 959000

%define with_java 1
%{?_with_java: %{expand: %%global with_java 1}}

%if %{with_java}
# Do not require java stuff just because we have a java backend
%define _requires_exceptions libjvm\.so
%endif

Name: soprano
Summary: Library which provides a nice QT interface to RDF
Version: 2.2.64
%if %branch
Release: %mkrel 0.%{revision}.1
%else
Release: %mkrel 2
%endif
Epoch: 4
Group: System/Libraries
License: LGPLv2+
URL: http://soprano.sourceforge.net
%if %branch
Source: soprano-%version.%{revision}.tar.bz2
%else
Source: soprano-%version.tar.bz2
%endif
# Drop wrong unneeded rpath=%{_libdir}
Patch0: soprano-drop-rpath.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake >= 2.6.2
BuildRequires: redland-devel >= 1.0.6
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: clucene-devel >= 0.9.19
BuildRequires: kde4-macros
%if %with_java
BuildRequires: java-rpmbuild
BuildRequires: chrpath
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
%_datadir/dbus-1/interfaces/*

#---------------------------------------------------------------------------------

%prep
%setup -q -n %name
%patch0 -p1

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

