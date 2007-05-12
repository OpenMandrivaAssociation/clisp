%define	name	clisp
%define	version	2.38
%define	release	%mkrel 2

Summary:	Common Lisp (ANSI CL) implementation
Name:		clisp
Version:	%{version}
Release:	%{release}
Icon:		clisp.gif
License:	GPL
Epoch:		1
Group:		Development/Other
Source0:	ftp://seagull.cdrom.com/pub/lisp/clisp/source/%{name}-%{version}.tar.bz2
#Patch0:	%{name}-2.33.2-debian-patches.patch.bz2
URL:		http://sourceforge.net/projects/clisp/
Provides:	ansi-cl
BuildRequires:	readline-devel ncurses-devel ffi-devel libsigsegv-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%prep
%setup -q
#%patch0 -p1

%build
COPTS="--prefix=%{_prefix} --libdir=%{_libdir} --fsstnd=redhat --with-dynamic-modules --with-readline --with-dynamic-ffi"
XCFLAGS="$RPM_OPT_FLAGS -fexpensive-optimizations" \
./configure $COPTS
cd src 
./makemake $COPTS > Makefile
make config.lisp
make
cd -

%check
cd src
make check
cd -

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{makeinstall_std}
cd -

%{find_lang} %{name}

#(peroyvind) weird problems, ugly perl hack for now
perl -pi -e "s#clisp.mo#clisp\*.mo#g" %{name}.lang

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/clisp
%dir %{_libdir}/clisp
%{_libdir}/clisp/*
%doc ANNOUNCE SUMMARY src/clisp.html src/README doc/*
%{_mandir}/*/*
