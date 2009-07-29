Summary:	Common Lisp (ANSI CL) implementation
Name:		clisp
Version:	2.48
Release:	%mkrel 1
License:	GPLv2
Epoch:		1
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/pub/gnu/clisp/latest/%{name}-%{version}.tar.bz2
URL:		http://clisp.cons.org/
Provides:	ansi-cl
BuildRequires:	imake
BuildRequires:	libsigsegv-devel
BuildRequires:	readline-devel
BuildRequires:  dbus-devel
BuildRequires:  diffutils
BuildRequires:  libfcgi-devel
BuildRequires:  ffcall-devel
BuildRequires:  gdbm-devel
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libice-devel
BuildRequires:  libsm-devel
BuildRequires:  libx11-devel
BuildRequires:  libxaw-devel
BuildRequires:  libxext-devel
BuildRequires:  libxft-devel
BuildRequires:  libxmu-devel
BuildRequires:  libxrender-devel
BuildRequires:  libxt-devel
BuildRequires:  libglade2-devel
BuildRequires:  pcre-devel
BuildRequires:  postgresql-devel
BuildRequires:  zlib-devel
BuildRequires:  db4-devel
BuildRequires:  libpari-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%build
ulimit -s 16384
./configure --prefix=%{_prefix} \
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
            --cbc \
            build CFLAGS="%optflags"


make -C build

%check
make -C build check

%install
rm -rf %{buildroot}
%makeinstall_std  -C build

rm -f %{buildroot}%{_docdir}/clisp/doc/clisp.{dvi,1,ps}
cp -p doc/mop-spec.pdf %{buildroot}%{_docdir}/clisp/doc

%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/clisp
%{_mandir}/*/*
%{_docdir}/clisp
%dir %{_libdir}/%{name}-%{version}/base
%dir %{_libdir}/%{name}-%{version}/full
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/base/lispinit.mem
%{_libdir}/%{name}-%{version}/base/lisp.run
%{_libdir}/%{name}-%{version}/full/lispinit.mem
%{_libdir}/%{name}-%{version}/full/lisp.run
%{_libdir}/%{name}-%{version}/data
%{_datadir}/emacs/site-lisp/*
%{_datadir}/vim/vimfiles/after/syntax/lisp.vim

%files devel
%defattr(-,root,root,-)
%attr(0755,root,root) %{_libdir}/%{name}-%{version}/clisp-link
%{_libdir}/%{name}-%{version}/base/*.a
%{_libdir}/%{name}-%{version}/base/*.o
%{_libdir}/%{name}-%{version}/base/*.h
%{_libdir}/%{name}-%{version}/base/*.dvi
%{_libdir}/%{name}-%{version}/base/makevars
%{_libdir}/%{name}-%{version}/full/*.a
%{_libdir}/%{name}-%{version}/full/*.o
%{_libdir}/%{name}-%{version}/full/*.h
%{_libdir}/%{name}-%{version}/full/*.dvi
%{_libdir}/%{name}-%{version}/full/makevars
%{_libdir}/%{name}-%{version}/linkkit
%{_datadir}/aclocal/clisp.m4
