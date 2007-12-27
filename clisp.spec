%define	name	clisp
%define	version	2.41a
%define	release	%mkrel 2

Summary:	Common Lisp (ANSI CL) implementation
Name:		clisp
Version:	%{version}
Release:	%{release}
License:	GPL
Epoch:		1
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/pub/gnu/clisp/latest/%{name}-%{version}.tar.bz2
Patch0:		clisp-2.41-postgresql.patch
URL:		http://clisp.cons.org/
Provides:	ansi-cl
BuildRequires:	readline-devel gettext pcre-devel postgresql-devel libsigsegv-devel
BuildRequires:	db4.2-devel zlib-devel libice-devel libsm-devel libx11-devel libxaw-devel
BuildRequires:  libxext-devel libxft-devel libxmu-devel libxrender-devel libxt-devel
BuildRequires:	imake termcap-devel

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
Requires:	%{name} = %{version}-%{release}

%description	devel
Files necessary for linking CLISP.

%prep
%setup -q -n %{name}-2.41
%patch0 -p1 -b .postgresql

%build
CFLAGS="" \
./configure	--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--fsstnd=redhat \
		--with-dynamic-ffi \
		--with-module=berkeley-db \
		--with-module=clx/new-clx \
		--with-module=pcre \
		--with-module=postgresql \
		--with-module=rawsock \
		--with-module=wildcard \
		--with-module=zlib \
		--with-module=bindings/glibc \
		--with-readline \
		--build build

%check
cd build
make check

%install
rm -rf %{buildroot}
%makeinstall_std -C build docdir=%{_docdir}/clisp-%{version}
rm -f $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}/doc/clisp.{dvi,1,ps}
cp -p doc/mop-spec.pdf $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}/doc
%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/clisp
%{_mandir}/*/*
%{_docdir}/clisp-%{version}
%dir %{_libdir}/clisp/base
%dir %{_libdir}/clisp/full
%dir %{_libdir}/clisp
%{_libdir}/clisp/base/lispinit.mem
%{_libdir}/clisp/base/lisp.run
%{_libdir}/clisp/full/lispinit.mem
%{_libdir}/clisp/full/lisp.run
%{_libdir}/clisp/data
%{_datadir}/emacs/site-lisp/*

%files devel
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/clisp/clisp-link
%{_libdir}/clisp/base/*.a
%{_libdir}/clisp/base/*.o
%{_libdir}/clisp/base/*.h
%{_libdir}/clisp/base/*.dvi
%{_libdir}/clisp/base/makevars
%{_libdir}/clisp/full/*.a
%{_libdir}/clisp/full/*.o
%{_libdir}/clisp/full/*.h
%{_libdir}/clisp/full/*.dvi
%{_libdir}/clisp/full/makevars
%{_libdir}/clisp/linkkit
