%define with_lightning		0

Summary:	Common Lisp (ANSI CL) implementation
Name:		clisp
Version:	2.49
Release:	2
License:	GPLv2
Epoch:		1
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/pub/gnu/clisp/latest/%{name}-%{version}.tar.bz2
Patch0:		clisp-2.49-debian-bdb-5.1.patch
Patch1:		clisp-2.49-rosa-disable-socket-test.patch
URL:		http://clisp.cons.org/
Provides:	ansi-cl
BuildRequires:	imake
BuildRequires:	libsigsegv-devel
%if %{with_lightning}
BuildRequires:	lightning
%endif
BuildRequires:	readline-devel
BuildRequires:	dbus-devel
BuildRequires:	diffutils
BuildRequires:	libfcgi-devel
BuildRequires:	ffcall-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext
BuildRequires:	gtk2-devel
BuildRequires:	libice-devel
BuildRequires:	libsm-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	libxaw-devel
BuildRequires:	libxext-devel
BuildRequires:	libxft-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxt-devel
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pcre-devel
BuildRequires:	postgresql-devel
BuildRequires:	zlib-devel
BuildRequires:	db5-devel
BuildRequires:	libpari-devel

%description
Common Lisp is a high-level, all-purpose programming language.

CLISP is a Common Lisp implementation by Bruno Haible of Karlsruhe
University and Michael Stoll of Munich University, both in Germany.

It mostly supports Common Lisp as described in the ANSI CL standard.
It runs on microcomputers (DOS, OS/2, Windows NT, Windows 95, Amiga
500-4000, Acorn RISC PC) as well as on Unix workstations (Linux,
SVR4, Sun4, DEC Alpha OSF, HP-UX, NeXTstep, SGI, AIX, Sun3 and others) 
and needs only 2 MB of RAM.

It is free software and may be distributed under the terms of GNU GPL,
while it is possible to distribute commercial applications compiled
with CLISP.

The user interface comes in German, English, French and Spanish.
CLISP includes an interpreter, a compiler, a large subset of CLOS,
a foreign language interface and a socket interface.

An X11 interface is available through CLX and Garnet.

%package	devel
Summary:	Development files for CLISP
Group:		Development/Other
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	devel
Files necessary for linking CLISP.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

# socket test fails on i586...
%ifarch %{ix86}
%patch1 -p1
%endif

%build
ulimit -s 16384
./configure	--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--mandir=%{_mandir} \
		--docdir=%{_docdir}/clisp \
		--fsstnd=redhat \
		--hyperspec=http://www.lispworks.com/documentation/HyperSpec/ \
		--with-module=bindings/glibc \
		--with-module=clx/new-clx \
		--with-module=dbus \
		--with-module=fastcgi \
		--with-module=gdbm \
		--with-module=gtk2 \
		--with-module=i18n \
		--with-module=pcre \
		--with-module=postgresql \
		--with-module=rawsock \
		--with-module=regexp \
		--with-module=syscalls \
		--with-module=wildcard \
		--with-module=zlib \
		--with-readline \
%if %{with_lightning}
		--with-jitc=lightning \
%endif
		--cbc \
		build CFLAGS="%optflags"


make -C build

%check
make -C build check

%install
%makeinstall_std  -C build

rm -f %{buildroot}%{_docdir}/clisp/doc/clisp.{dvi,1,ps}
cp -p doc/mop-spec.pdf %{buildroot}%{_docdir}/clisp/doc

find %{buildroot}/%{_libdir} -name '*.so' -exec chmod +x {} \;

%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang

%files -f %{name}.lang
%{_bindir}/clisp
%{_mandir}/*/*
%doc %{_docdir}/clisp
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/base/lispinit.mem
%{_libdir}/%{name}-%{version}/base/lisp.run
%{_libdir}/%{name}-%{version}/bindings/glibc/*.fas
%{_libdir}/%{name}-%{version}/bindings/glibc/*.lisp
%{_libdir}/%{name}-%{version}/clx/new-clx/*.fas
%{_libdir}/%{name}-%{version}/clx/new-clx/*.lisp
%{_libdir}/%{name}-%{version}/data
%dir %{_libdir}/%{name}-%{version}/dbus
%{_libdir}/%{name}-%{version}/dbus/*.fas
%{_libdir}/%{name}-%{version}/dbus/*.lisp
%dir %{_libdir}/%{name}-%{version}/fastcgi
%{_libdir}/%{name}-%{version}/fastcgi/*.fas
%{_libdir}/%{name}-%{version}/fastcgi/*.lisp
%dir %{_libdir}/%{name}-%{version}/gdbm
%{_libdir}/%{name}-%{version}/gdbm/*.fas
%{_libdir}/%{name}-%{version}/gdbm/*.lisp
%dir %{_libdir}/%{name}-%{version}/gtk2
%{_libdir}/%{name}-%{version}/gtk2/*.fas
%{_libdir}/%{name}-%{version}/gtk2/*.lisp
%{_libdir}/%{name}-%{version}/dynmod
%dir %{_libdir}/%{name}-%{version}/pcre
%{_libdir}/%{name}-%{version}/pcre/*.fas
%{_libdir}/%{name}-%{version}/pcre/*.lisp
%dir %{_libdir}/%{name}-%{version}/postgresql
%{_libdir}/%{name}-%{version}/postgresql/*.fas
%{_libdir}/%{name}-%{version}/postgresql/*.lisp
%dir %{_libdir}/%{name}-%{version}/rawsock
%{_libdir}/%{name}-%{version}/rawsock/*.fas
%{_libdir}/%{name}-%{version}/rawsock/*.lisp
%dir %{_libdir}/%{name}-%{version}/wildcard
%{_libdir}/%{name}-%{version}/wildcard/*.fas
%{_libdir}/%{name}-%{version}/wildcard/*.lisp
%dir %{_libdir}/%{name}-%{version}/zlib
%{_libdir}/%{name}-%{version}/zlib/*.fas
%{_libdir}/%{name}-%{version}/zlib/*.lisp
%{_datadir}/emacs/site-lisp/*
%{_datadir}/vim/vimfiles/after/syntax/lisp.vim

%files devel
%attr(0755,root,root) %{_bindir}/clisp-link
%{_libdir}/%{name}-%{version}/base/*.a
%{_libdir}/%{name}-%{version}/base/*.o
%{_libdir}/%{name}-%{version}/base/*.h
%{_libdir}/%{name}-%{version}/base/makevars
%{_libdir}/%{name}-%{version}/bindings/glibc/*.o
%{_libdir}/%{name}-%{version}/bindings/glibc/*.sh
%{_libdir}/%{name}-%{version}/bindings/glibc/Makefile
%{_libdir}/%{name}-%{version}/build-aux/*
%{_libdir}/%{name}-%{version}/clx/new-clx/*.o
%{_libdir}/%{name}-%{version}/clx/new-clx/*.sh
%{_libdir}/%{name}-%{version}/clx/new-clx/demos
%{_libdir}/%{name}-%{version}/clx/new-clx/Makefile
%{_libdir}/%{name}-%{version}/clx/new-clx/README
%{_libdir}/%{name}-%{version}/dbus/*.o
%{_libdir}/%{name}-%{version}/dbus/*.sh
%{_libdir}/%{name}-%{version}/dbus/Makefile
%{_libdir}/%{name}-%{version}/fastcgi/*.o
%{_libdir}/%{name}-%{version}/fastcgi/*.sh
%{_libdir}/%{name}-%{version}/fastcgi/Makefile
%{_libdir}/%{name}-%{version}/fastcgi/README
%{_libdir}/%{name}-%{version}/gdbm/*.o
%{_libdir}/%{name}-%{version}/gdbm/*.sh
%{_libdir}/%{name}-%{version}/gdbm/Makefile
%{_libdir}/%{name}-%{version}/gtk2/*.cfg
%{_libdir}/%{name}-%{version}/gtk2/*.glade
%{_libdir}/%{name}-%{version}/gtk2/*.o
%{_libdir}/%{name}-%{version}/gtk2/*.sh
%{_libdir}/%{name}-%{version}/gtk2/Makefile
%{_libdir}/%{name}-%{version}/linkkit
%{_libdir}/%{name}-%{version}/pcre/*.o
%{_libdir}/%{name}-%{version}/pcre/*.sh
%{_libdir}/%{name}-%{version}/pcre/Makefile
%{_libdir}/%{name}-%{version}/postgresql/*.o
%{_libdir}/%{name}-%{version}/postgresql/*.sh
%{_libdir}/%{name}-%{version}/postgresql/Makefile
%{_libdir}/%{name}-%{version}/postgresql/README
%{_libdir}/%{name}-%{version}/rawsock/*.o
%{_libdir}/%{name}-%{version}/rawsock/*.sh
%{_libdir}/%{name}-%{version}/rawsock/demos
%{_libdir}/%{name}-%{version}/rawsock/Makefile
%{_libdir}/%{name}-%{version}/wildcard/*.a
%{_libdir}/%{name}-%{version}/wildcard/*.o
%{_libdir}/%{name}-%{version}/wildcard/*.sh
%{_libdir}/%{name}-%{version}/wildcard/Makefile
%{_libdir}/%{name}-%{version}/wildcard/README
%{_libdir}/%{name}-%{version}/zlib/*.o
%{_libdir}/%{name}-%{version}/zlib/*.sh
%{_libdir}/%{name}-%{version}/zlib/Makefile
%{_datadir}/aclocal/clisp.m4


%changelog
* Fri Aug 06 2010 Paulo Andrade <pcpa@mandriva.com.br> 1:2.49-1mdv2011.0
+ Revision: 567191
- Update to version 2.49

* Wed Aug 19 2009 Paulo Andrade <pcpa@mandriva.com.br> 1:2.48-2mdv2010.0
+ Revision: 418280
- Make the -I option completely ignore readline
  # This is an at least "somewhat" elegant version of an alternate ugly hack
  # required to make sagemath python-pexpect interface work correctly with
  # clisp

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.48-1mdv2010.0
+ Revision: 404036
- Update to new version 2.48
- Sync configure options and BuildRequires with Fedora (more
  modules are available now)

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.47-2mdv2009.1
+ Revision: 346030
- rebuild against new readline

* Tue Nov 11 2008 Frederik Himpe <fhimpe@mandriva.org> 1:2.47-1mdv2009.1
+ Revision: 302178
- Update to new version 2.47
- Remove patch fixing postgresql detection, integrated upstream
- Specifically buildrequire version 4.6 of berkeleydb, it does not
  build with db 4.7

* Wed Aug 13 2008 Frederik Himpe <fhimpe@mandriva.org> 1:2.46-1mdv2009.0
+ Revision: 271576
- Update to new version 2.46

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1:2.45-2mdv2009.0
+ Revision: 266536
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Frederik Himpe <fhimpe@mandriva.org> 1:2.45-1mdv2009.0
+ Revision: 217754
- New version 2.45
- Remove postgresql patch, it is included upstream. Replace it by new pgsql
  patch because upstream configure script has an error finding the headers
- Remove topdir patch: install it in versioned lib directory, like upstream,
  Fedora and Debian are doing
- Needs bigger stack size to succeed in building
- Small Adaptatations to make it build in directory named build
- Build gtk2 module

* Tue Feb 26 2008 Frederik Himpe <fhimpe@mandriva.org> 1:2.44.1-1mdv2008.1
+ Revision: 175504
- New upstream bugfix release

* Wed Feb 13 2008 Frederik Himpe <fhimpe@mandriva.org> 1:2.44-1mdv2008.1
+ Revision: 167118
- New upstream release
- Add libffcall-devel BuildRequires

* Mon Jan 07 2008 Pascal Terjan <pterjan@mandriva.org> 1:2.43-2mdv2008.1
+ Revision: 146277
- Make the -devel installable

* Mon Dec 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1:2.43-1mdv2008.1
+ Revision: 139851
- 2.43

* Thu Dec 27 2007 Oden Eriksson <oeriksson@mandriva.com> 1:2.41a-2mdv2008.1
+ Revision: 138227
- build against db4.2-devel for now
- rebuilt against bdb 4.6.x libs

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 31 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.41a-1mdv2008.0
+ Revision: 33431
- fix buildrequires
- remove icon
- 2.41a
- add url for source
- update to 2.41 (with help from Frederik Himpe)
- fix detection of postgresql headers (P0 from Frederik)
- Import clisp



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1:2.38-2mdv2007.0
- Rebuild

* Sat May 20 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.38-1mdk
- 2.38
- sort out some build issues with flags etc
- build with dynamic modules support
- build against libsigsegv
- lib64 fix
- fix buildrequires
- %%mkrel
- move check to new %%check stage

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.33.2-3mdk
- Rebuild

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.33.2-2mdk
- rebuild for new readline

* Sat Jun 05 2004 Per ?yvind Karlsen <peroyvind@linux-mandrake.com> 2.33.2-1mdk
- 2.33.2
- drop P0

* Sat Apr 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.33-2mdk
- fix buildrequires

* Fri Apr 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.33-1mdk
- 2.33
- clean docs
- update P0 from debian
- minor fixes
- disable parallell build

* Mon Jun 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.30-2mdk
- fix prefix etc. (from Mark Draheim <rickscafe.casablanca@gmx.net>)
- fix %%files list

* Tue Jun 17 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.30-1mdk
- 2.30
- cleanups
- P0 from debian, dropped alpha patch
- alot of spec file fixes

* Tue Jul 17 2001 Daouda LO <daouda@mandrakesoft.com> 2.27-1mdk
- release 2.27
  o The default extension of Lisp source files for CLISP is now ".lisp"
    instead of ".lsp". When both "foo.lisp" and "foo.lsp" exist, 
    (LOAD "foo") will load "foo.lisp".

  o Changed bytecode format. All .fas files generated by previous CLISP
     versions  are invalid and must be recompiled.
  o More Ansi CL compliances  
  o See more of the changelog: http://sourceforge.net/forum/forum.php?forum_id=72006 

- update URL.  
- new versioning scheme.
- merge ppc build.
- s|config.lsp|config.lisp| in ppc build.

* Wed Apr 25 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 2000.03.06-4mdk
- Make it build on the Alpha platform.
- Quiet output when uncompressing the source because it is really too annoying
  to watch.

* Sun Nov 05 2000 David BAUDENS <baudens@mandrakesoft.com> 2000.03.06-3mdk
- Rewrite spec following Clisp Install documentation to be able to build this
  package on all archs
- Have an intelligent description

* Sun Jul 23 2000 Pixel <pixel@mandrakesoft.com> 2000.03.06-2mdk
- *much* cleanup, macorizaiton, BM

* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 2000.03.06-1mdk
- Update to 2000.03.06

* Tue Feb 22 2000 Stefan van der Eijk <s.vandereijk@chello.nl>
- rewrote most of .spec file
- updated to 1999.07.22
