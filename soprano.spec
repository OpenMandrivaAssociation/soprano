%ifarch %arm %mips
%define with_java 0
%else
%define with_java 1
%endif
%{?_with_java: %{expand: %%global with_java 1}}

%if %{with_java}
# Do not require java stuff just because we have a java backend
%if %{_use_internal_dependency_generator}
%define _noautoreq 'libjvm.so'
%else
%define _requires_exceptions libjvm\.so
%endif
%endif

%define with_clucene 0

Name:		soprano
Summary:	Library which provides a nice QT interface to RDF
Version:	2.9.0
Release:	1
Epoch:		4
Group:		System/Libraries
License:	LGPLv2+
URL:		http://soprano.sourceforge.net
Source:		http://ovh.dl.sourceforge.net/project/soprano/Soprano/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	cmake >= 2.6.2
BuildRequires:	pkgconfig(redland) >= 1.0.6
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(libiodbc)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtXml)
BuildRequires:	pkgconfig(QtDBus)
BuildRequires:	kde4-macros
%if %{with_java}
BuildRequires:	java-rpmbuild
BuildRequires:	chrpath
%endif
%if %{with_clucene}
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

%if %{with_java}
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

%if %{with_clucene}
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
%if %{with_clucene}
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
%if %{with_java}
export JAVA_HOME=%{java_home}
%endif

%cmake_qt4
%make

%install
%makeinstall_std -C build

%if %{with_java}
# Load libjvm.so from the JRE directory instead of SDK directory. This
# works with Sun-derived JREs, but GCJ/Jamvm etc have libjvm.so in different
# directories. Maybe there should be an alternative pointing to libjvm.so.
old_rpath=$(chrpath -l %{buildroot}%{_libdir}/soprano/libsoprano_sesame2backend.so | cut -d= -f2)
new_rpath=$(echo "$old_rpath" | sed "s,%{java_home},%{_jvmdir},")
chrpath -r "$new_rpath" %{buildroot}%{_libdir}/soprano/libsoprano_sesame2backend.so
%endif

%changelog
* Sun Jul 01 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4:2.8.0-2
- Build with clucene support

* Sun Jul 01 2012 Andrey Bondrov <abondrov@mandriva.org> 4:2.8.0-1
+ Revision: 807674
- Add conditions for clucene-related stuff
- New version 2.8.0, drop no longer needed patch, build without clucene support
- New version 2.7.57, sync with Rosa

* Tue Mar 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 4:2.7.5-1
+ Revision: 784741
- version update 2.7.5

* Thu Mar 01 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.7.3-2
+ Revision: 781642
- Add P0 to try to fix bko #286627

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Use bcond for command line switch enabling or disabling java.

* Fri Nov 25 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.7.3-1
+ Revision: 733477
- Remove clucene support

  + Crispin Boylan <crisb@mandriva.org>
    - New release

* Mon Jun 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.6.51-0.20110606.1
+ Revision: 682934
- New version ( needed for new nepomuk)

* Sat May 07 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4:2.6.0-3
+ Revision: 671947
- clean out legacy rpm stuff
- use %%{EVRD} for dependencies
- fix dependency loops

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 4:2.6.0-2
+ Revision: 669996
- mass rebuild

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 4:2.6.0-1
+ Revision: 637019
- New 2.6.0
- force redland include dir to raptor2

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 4:2.5.63-1mdv2011.0
+ Revision: 601723
- new version 2.5.63 final

* Fri Nov 12 2010 Funda Wang <fwang@mandriva.org> 4:2.5.63-0.git20101104.1mdv2011.0
+ Revision: 596425
- new snapshot needed for kde 4.5.76

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix version in lib packages

* Thu Sep 02 2010 Funda Wang <fwang@mandriva.org> 4:2.5.62-0.1170808.1mdv2011.0
+ Revision: 575228
- new snapshot needed for kde 4.5.67
- add versioned requires for sub packages so that latest packages be picked up
- fix provides of devel package

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 4:2.5.0-1mdv2011.0
+ Revision: 568201
- update to new version 2.5.0

* Wed Jul 28 2010 Funda Wang <fwang@mandriva.org> 4:2.4.64-1mdv2011.0
+ Revision: 562175
- 2.4.64 final

* Wed Jul 21 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.4.63-0.1132031.1mdv2011.0
+ Revision: 556305
- Update to new snapshot
- Rebuild in release mode

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.4.63-0.1122683.1mdv2010.1
+ Revision: 542019
- Update to 2.4.63 snapshot
  Will be needed by kdebase4-runtime

* Fri Apr 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.4.2-1mdv2010.1
+ Revision: 535463
- New version 2.4.2

* Fri Mar 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.4.1-1mdv2010.1
+ Revision: 527691
- Fix file list
- Update to version 2.4.1

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 4:2.4.0.1-1mdv2010.1
+ Revision: 504724
- New version 2.4.0.1

* Wed Jan 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.71-0.1070828.3mdv2010.1
+ Revision: 486983
- New snapshot

* Sat Jan 02 2010 Funda Wang <fwang@mandriva.org> 4:2.3.71-0.1064411.3mdv2010.1
+ Revision: 485192
- hardrequires on librasql is not needed, as it is already there through file deps

* Sat Jan 02 2010 Funda Wang <fwang@mandriva.org> 4:2.3.71-0.1064411.2mdv2010.1
+ Revision: 485177
- rebuild

* Sun Dec 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.71-0.1064411.1mdv2010.1
+ Revision: 480495
- New snapshot

  + Funda Wang <fwang@mandriva.org>
    - update url

* Mon Nov 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.70-0.1056639.1mdv2010.1
+ Revision: 471743
- New svn snapshot

* Fri Nov 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.67-0.1053357.9mdv2010.1
+ Revision: 470559
- Fix requires in the redland backend

* Fri Nov 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.67-0.1053357.8mdv2010.1
+ Revision: 470527
- Only use virtuoso now
- Add miss %%if
- Seems they still are needed
- Virtuoso is not more optionnal
  Do not install anymore redland nor sesame. We only keep them for compatibility.

* Tue Nov 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.67-0.1053357.6mdv2010.1
+ Revision: 469433
- New snapshot
  Remove merged patch

* Mon Nov 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.67-0.1044611.5mdv2010.1
+ Revision: 469322
- Fix previous patch, i forgot to commit the one that compile
- Fix virtuoso detection
- For the virtuoso backend, virtuoso-opensource 5.0.12 at least is required
- Enable virtuoso

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.67-0.1044611.2mdv2010.1
+ Revision: 464633
- Rebuild against new Qt

* Wed Nov 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.3.67-0.1044611.1mdv2010.1
+ Revision: 460425
- update to a svn snapshot

* Mon Sep 28 2009 Olivier Blin <blino@mandriva.org> 4:2.3.1-7mdv2010.0
+ Revision: 450365
- disable java on arm & mips (from Arnaud Patard)

* Wed Sep 23 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.1-6mdv2010.0
+ Revision: 448050
- Never forget your own rule of not obsoletes libraries. Should fix kde 4.2 -> kde 4.3 upgrades

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.1-4mdv2010.0
+ Revision: 443269
- The plugin modules are tied with their parent libraries, but not manifest itself until dynloaded.
  This made a installed sesame plugins fails everytime since couldn't find proper link library

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.1-3mdv2010.0
+ Revision: 443128
- Devel should requires main soprano as well

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.1-2mdv2010.0
+ Revision: 443034
- Rebuild to fix crazyness of buildsystem

* Mon Sep 14 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.1-1mdv2010.0
+ Revision: 440752
- Updated with current upstream package 2.3.1 as requested by mandriva nepomuk team

* Fri Jul 24 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.0-2mdv2010.0
+ Revision: 399475
- Devel packages requires pplugins as well to test building

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.3.0-1mdv2010.0
+ Revision: 398617
- New upstream version 2.3.0

* Fri Jul 17 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.2.69-3mdv2010.0
+ Revision: 396904
- Use proper sql types

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.69-2mdv2010.0
+ Revision: 388895
- Fix file list
- Update to version 2.2.69

* Fri Jun 19 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.2.68-0.1mdv2010.0
+ Revision: 387366
- Fixed tarball version
- Proper separate plugins, redland included
- Virtuoso now works properly
- Proper compile soprano with iodbc instead of unixODBC. Removed no needed patches

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.67-0.974203.2mdv2010.0
+ Revision: 381083
- Fix BuildRequires
- Fix && Enable virtuoso plugin

* Thu May 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.67-0.974203.1mdv2010.0
+ Revision: 380609
- New snapshot

* Thu May 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.67-0.970828.4mdv2010.0
+ Revision: 378312
- Bump because of BS failure

* Thu May 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.67-0.970828.3mdv2010.0
+ Revision: 378141
- New snapshot

* Sun May 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.67-0.964921.3mdv2010.0
+ Revision: 374046
- Fix Requires
- Requires the sesame plugin for now

* Thu May 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.67-0.964921.1mdv2010.0
+ Revision: 372986
- New snapshot

* Mon May 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.65-0.963541.1mdv2010.0
+ Revision: 372008
- New snapshot
- Add a conflict
- Move sesame2 plugin on its own package
- Remove old macros

* Wed Apr 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.2.64-0.959000.1mdv2010.0
+ Revision: 369150
- New snapshot ( needed for kde 4.2.70)

* Sat Jan 31 2009 Anssi Hannula <anssi@mandriva.org> 4:2.2.1-2mdv2009.1
+ Revision: 335776
- drop wrong rpath on standard libdir (P0)
- make fixing java rpath more robust

* Thu Jan 29 2009 Nicolas Vigier <nvigier@mandriva.com> 4:2.2.1-1mdv2009.1
+ Revision: 335228
- update to version 2.2.1

* Tue Jan 20 2009 Nicolas Vigier <nvigier@mandriva.com> 4:2.1.67-1mdv2009.1
+ Revision: 331929
- update to version 2.1.67

* Fri Jan 16 2009 Helio Chissini de Castro <helio@mandriva.com> 4:2.1.64-0.912017.1mdv2009.1
+ Revision: 330198
- Update with latest svn, s requires for specific nepomuk requirements

* Wed Dec 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.1.64-0.895232.1mdv2009.1
+ Revision: 312477
- New snapshot

* Tue Oct 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.1.64-0.876764.1mdv2009.1
+ Revision: 297796
- New snapshot ( needed by next nepomuk-kde)

* Sat Oct 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.1.63-0.872741.1mdv2009.1
+ Revision: 294822
- New snapshot
  Remove merged patches

* Sun Sep 28 2008 Anssi Hannula <anssi@mandriva.org> 4:2.1.1-3mdv2009.0
+ Revision: 289000
- do not require java libs, most users do not need them
- fix java backend to look up libjvm.so in a better directory (still
  only works with Sun-derived JREs since other JREs have it in different
  directories

* Thu Aug 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.1.1-2mdv2009.0
+ Revision: 272135
- Update soprano to trunk ( asked by strueg)

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 4:2.1.1-1mdv2009.0
+ Revision: 257848
- New version 2.1.1

* Sun Jul 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4:2.1-2mdv2009.0
+ Revision: 250650
- use %%java_home macro instead of hardcoding paths to java place
- use buildrequire on java-rpmbuild instead of specific java devel packages

* Sat Jul 26 2008 Funda Wang <fwang@mandriva.org> 4:2.1-1mdv2009.0
+ Revision: 250124
- New version 2.1 final
- fix url

* Sat Jul 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.99-0.830350.3mdv2009.0
+ Revision: 250103
- Fix use of java backend thanks to  Adrien BUSTANY

* Sun Jul 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.99-0.830350.2mdv2009.0
+ Revision: 239218
- Disable java support this is still broken

* Tue Jul 15 2008 Helio Chissini de Castro <helio@mandriva.com> 4:2.0.99-0.830350.1mdv2009.0
+ Revision: 236091
- New svn snapshot
- Soprano is qt only, so services is in datadir
- Proper java for old distros

* Mon Jul 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.99-0.804023.5mdv2009.0
+ Revision: 234535
- Add kde4-macros as BuildRequires
- Fix java detection for non 32 bit
- Fix java detection for openjdk
- Fix java detection for openjdk

  + Helio Chissini de Castro <helio@mandriva.com>
    - Proper interface dir

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.99-0.804023.3mdv2009.0
+ Revision: 209226
- Disable java build because it gave an undefined symbol: JNI_CreateJavaVM

* Mon May 05 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.99-0.804023.2mdv2009.0
+ Revision: 201348
- Rebuild with right path

* Sun May 04 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.99-0.804023.1mdv2009.0
+ Revision: 201207
- Fix tarball
- New snapshot needed by next kdelibs4
- Versionate qt4-devel BR
- Update to version 2.0.98 (needed by kdebase4-runtime 4.0.70 )

  + Helio Chissini de Castro <helio@mandriva.com>
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Thu Feb 21 2008 Helio Chissini de Castro <helio@mandriva.com> 4:2.0.2-0.777761.1mdv2008.1
+ Revision: 173629
- Update for soprano 2.0.2 trunk to match nepomuk playground tool

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix description-line-too-long

* Sat Jan 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:2.0.0-0.758303.3mdv2008.1
+ Revision: 158162
- Fix File list
- Build with java enable as it build now

* Mon Jan 07 2008 Helio Chissini de Castro <helio@mandriva.com> 4:2.0.0-0.758303.2mdv2008.1
+ Revision: 146283
- Proper split
- Update for 2.0.0 from svn
- Removed another useless patch

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:1.99.0-0.746844.7mdv2008.1
+ Revision: 116999
- New release 1.99.0
  Add a switch for java support, do not activate it for the moment ( do not build )

* Wed Nov 07 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:1.97.1-0.733572.7mdv2008.1
+ Revision: 106780
- Fix version in version.h

* Wed Nov 07 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:1.97.1-0.733572.6mdv2008.1
+ Revision: 106638
- New snapshot needed for the upcoming rpms of KDE4

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:1.97.0-0.725573.6mdv2008.1
+ Revision: 102219
- Fix conflict

  + Thierry Vignaud <tv@mandriva.org>
    - revert conflicts, better use rpmlint to kill the bogus package thus enabling
      smoother upgrade with yet not updated third party lib users

  + Funda Wang <fwang@mandriva.org>
    - use icedtea provided alternative symbolink

* Wed Oct 17 2007 Funda Wang <fwang@mandriva.org> 4:1.97.0-0.725573.5mdv2008.1
+ Revision: 99480
- add icedtea dir macro for x86_64 building
- add conflict on incorrectly named package to ease upgrading

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add doxygen as buildrequire
    - Say hello to sesame backend

* Tue Oct 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:1.97.0-0.725573.4mdv2008.1
+ Revision: 99219
- Do not activate sesam for the moment
- Fix BuildRequires
- New snapshot
  Fix file list

* Mon Oct 15 2007 Funda Wang <fwang@mandriva.org> 4:1.97.0-0.724490.2mdv2008.1
+ Revision: 98710
- new major of libsoprano

* Sun Oct 14 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 4:1.97.0-0.724490.1mdv2008.1
+ Revision: 98344
- New svn snapshot
  Use real release number

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Thu Sep 27 2007 Tiago Salem <salem@mandriva.com.br> 3:3.0-0.714066.3mdv2008.0
+ Revision: 93396
- Bumping release and fixing Obsoletes tag

* Wed Sep 19 2007 Tiago Salem <salem@mandriva.com.br> 3:3.0-0.714066.2mdv2008.0
+ Revision: 91171
- Making Obsoletes tags versioned

* Tue Sep 18 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 3:3.0-0.714066.1mdv2008.0
+ Revision: 89812
- Fix version making it possible to submit

  + Tiago Salem <salem@mandriva.com.br>
    - Revision update to 714066

  + Helio Chissini de Castro <helio@mandriva.com>
    - Upgrade for revision 688549

* Thu Jul 05 2007 Helio Chissini de Castro <helio@mandriva.com> 3:3.0-0.674845.1mdv2008.0
+ Revision: 48592
- Update from revision 674845

* Wed Jun 20 2007 Helio Chissini de Castro <helio@mandriva.com> 2:3.0-0.20070614.1mdv2008.0
+ Revision: 41914
- Added proper obsoletes

  + Michael Scherer <misc@mandriva.org>
    - fix url

* Thu Jun 14 2007 Helio Chissini de Castro <helio@mandriva.com> 2:3.0-0.20070614mdv2008.0
+ Revision: 39544
- Update from 20070614 svn date
- New svn update
- New package layout

* Mon May 14 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.0-0.20070514.1mdv2008.0
+ Revision: 26680
- New snapshot

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 2:3.0-0.20070502.4mdv2008.0
+ Revision: 20572
- Fix install

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 2:3.0-0.20070502.3mdv2008.0
+ Revision: 20471
- Remove release
- aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- Update it

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 2:3.0-0.20070502.2mdv2008.0
+ Revision: 20448
- Add package version date
- New version

