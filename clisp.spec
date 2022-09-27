%define _disable_ld_no_undefined 1

# git snapshot
%global commit	de01f0f47bb44d3a0f9e842464cf2520b238f356
%global date	20180218

Summary:	ANSI Common Lisp implementation
Name:		clisp
Version:	2.49.93
Release:	1
Group:		Development/Other
License:	GPLv2
#Source0:	https://downloads.sourceforge.net/clisp/%{name}-%{version}.tar.bz2
#Source0:	ftp://ftp.gnu.org/pub/gnu/clisp/latest/%{name}-%{version}.tar.bz2
Source0:	https://gitlab.com/gnu-clisp/clisp/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
# Upstream dropped this file from the distribution
Source1:	https://gitlab.com/sam-s/clhs/-/raw/master/clhs.el
# https://sourceforge.net/tracker/?func=detail&aid=3529607&group_id=1355&atid=301355
Patch0:		%{name}-format.patch
# https://sourceforge.net/tracker/?func=detail&aid=3529615&group_id=1355&atid=301355
#Patch1:		%{name}-arm.patch
# https://sourceforge.net/tracker/?func=detail&aid=3572511&group_id=1355&atid=301355
#Patch2:		%{name}-libsvm.patch
# https://sourceforge.net/tracker/?func=detail&aid=3572516&group_id=1355&atid=301355
Patch3:		%{name}-db.patch
# Linux-specific fixes.  Sent upstream 25 Jul 2012.
Patch4:		%{name}-linux.patch
# (fedora)
Patch5:		%{name}-pari.patch

BuildRequires:	locales-en
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:	pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)

BuildRequires:	db5-devel
BuildRequires:	diffutils
BuildRequires:	dbus-devel
BuildRequires:	emacs
BuildRequires:	fcgi-devel
BuildRequires:	ffcall-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
##BuildRequires:	ghostscript
##BuildRequires:	groff
BuildRequires:	gtk+2.0-devel
BuildRequires:	imake
BuildRequires:	libsigsegv-devel
BuildRequires:	libsvm-devel
#BuildRequires:	libxft-devel
#BuildRequires:	libxrender-devel
BuildRequires:  fcgi-devel
BuildRequires:	locales-en
BuildRequires:	pari
BuildRequires:	libpari-devel
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pcre-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	xaw-devel
BuildRequires:  pkgconfig(zlib)

Provides:	ansi-cl

%description
ANSI Common Lisp is a high-level, general-purpose programming
language.  GNU CLISP is a Common Lisp implementation by Bruno Haible
of Karlsruhe University and Michael Stoll of Munich University, both
in Germany.  It mostly supports the Lisp described in the ANSI Common
Lisp standard.  It runs on most Unix workstations (GNU/Linux, FreeBSD,
NetBSD, OpenBSD, Solaris, Tru64, HP-UX, BeOS, NeXTstep, IRIX, AIX and
others) and on other systems (Windows NT/2000/XP, Windows 95/98/ME)
and needs only 4 MiB of RAM.

It is Free Software and may be distributed under the terms of GNU GPL,
while it is possible to distribute commercial proprietary applications
compiled with GNU CLISP.

The user interface comes in English, German, French, Spanish, Dutch,
Russian and Danish, and can be changed at run time.  GNU CLISP
includes an interpreter, a compiler, a debugger, CLOS, MOP, a foreign
language interface, sockets, i18n, fast bignums and more.  An X11
interface is available through CLX, Garnet, CLUE/CLIO.  GNU CLISP runs
Maxima, ACL2 and many other Common Lisp packages.

%files -f %{name}.lang
%{_bindir}/clisp
%{_mandir}/man1/clisp.1*
%{_docdir}/clisp-%{version}+
%dir %{_libdir}/clisp-2.49.93+/
%dir %{_libdir}/clisp-2.49.93+/asdf/
%{_libdir}/clisp-2.49.93+/asdf/asdf.fas
%dir %{_libdir}/clisp-2.49.93+/base/
%{_libdir}/clisp-2.49.93+/base/lispinit.mem
%{_libdir}/clisp-2.49.93+/base/lisp.run
%dir %{_libdir}/clisp-2.49.93+/berkeley-db/
%{_libdir}/clisp-2.49.93+/berkeley-db/*.fas
%dir %{_libdir}/clisp-2.49.93+/bindings/
%dir %{_libdir}/clisp-2.49.93+/bindings/glibc/
%{_libdir}/clisp-2.49.93+/bindings/glibc/*.fas
%dir %{_libdir}/clisp-2.49.93+/clx/
%dir %{_libdir}/clisp-2.49.93+/clx/new-clx/
%{_libdir}/clisp-2.49.93+/clx/new-clx/*.fas
%{_libdir}/clisp-2.49.93+/data/
%dir %{_libdir}/clisp-2.49.93+/dbus/
%{_libdir}/clisp-2.49.93+/dbus/*.fas
%{_libdir}/clisp-2.49.93+/dynmod/
%dir %{_libdir}/clisp-2.49.93+/fastcgi/
%{_libdir}/clisp-2.49.93+/fastcgi/*.fas
%dir %{_libdir}/clisp-2.49.93+/full/
%{_libdir}/clisp-2.49.93+/full/lispinit.mem
%{_libdir}/clisp-2.49.93+/full/lisp.run
%dir %{_libdir}/clisp-2.49.93+/gdbm/
%{_libdir}/clisp-2.49.93+/gdbm/*.fas
%dir %{_libdir}/clisp-2.49.93+/gtk2/
%{_libdir}/clisp-2.49.93+/gtk2/*.fas
%dir %{_libdir}/clisp-2.49.93+/libsvm/
%{_libdir}/clisp-2.49.93+/libsvm/*.fas
%dir %{_libdir}/clisp-2.49.93+/pari/
%{_libdir}/clisp-2.49.93+/pari/*.fas
%dir %{_libdir}/clisp-2.49.93+/pcre/
%{_libdir}/clisp-2.49.93+/pcre/*.fas
%dir %{_libdir}/clisp-2.49.93+/postgresql/
%{_libdir}/clisp-2.49.93+/postgresql/*.fas
%dir %{_libdir}/clisp-2.49.93+/rawsock/
%{_libdir}/clisp-2.49.93+/rawsock/*.fas
%dir %{_libdir}/clisp-2.49.93+/zlib/
%{_libdir}/clisp-2.49.93+/zlib/*.fas
%{_datadir}/emacs/site-lisp/*
%{_datadir}/vim/vimfiles/after/syntax/*

#---------------------------------------------------------------------------

%package	devel
Summary:	Development files for CLISP
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description	devel
Files necessary for linking CLISP.

%files devel
%doc modules/clx/clx-manual
%{_bindir}/clisp-link
%{_mandir}/man1/clisp-link.1*
%{_libdir}/clisp-2.49.93+/asdf/Makefile
%{_libdir}/clisp-2.49.93+/asdf/*.lisp
%{_libdir}/clisp-2.49.93+/asdf/*.sh
%{_libdir}/clisp-2.49.93+/base/*.a
%{_libdir}/clisp-2.49.93+/base/*.o
%{_libdir}/clisp-2.49.93+/base/*.h
%{_libdir}/clisp-2.49.93+/base/makevars
%{_libdir}/clisp-2.49.93+/berkeley-db/Makefile
%{_libdir}/clisp-2.49.93+/berkeley-db/*.h
%{_libdir}/clisp-2.49.93+/berkeley-db/*.lisp
%{_libdir}/clisp-2.49.93+/berkeley-db/*.o
%{_libdir}/clisp-2.49.93+/berkeley-db/*.sh
%{_libdir}/clisp-2.49.93+/bindings/glibc/Makefile
%{_libdir}/clisp-2.49.93+/bindings/glibc/*.lisp
%{_libdir}/clisp-2.49.93+/bindings/glibc/*.o
%{_libdir}/clisp-2.49.93+/bindings/glibc/*.sh
%{_libdir}/clisp-2.49.93+/build-aux/
%{_libdir}/clisp-2.49.93+/clx/new-clx/demos/
%{_libdir}/clisp-2.49.93+/clx/new-clx/README
%{_libdir}/clisp-2.49.93+/clx/new-clx/Makefile
%{_libdir}/clisp-2.49.93+/clx/new-clx/*.h
%{_libdir}/clisp-2.49.93+/clx/new-clx/*.lisp
%{_libdir}/clisp-2.49.93+/clx/new-clx/*.o
%{_libdir}/clisp-2.49.93+/clx/new-clx/*.sh
%{_libdir}/clisp-2.49.93+/config.h
%{_libdir}/clisp-2.49.93+/dbus/Makefile
%{_libdir}/clisp-2.49.93+/dbus/*.h
%{_libdir}/clisp-2.49.93+/dbus/*.lisp
%{_libdir}/clisp-2.49.93+/dbus/*.o
%{_libdir}/clisp-2.49.93+/dbus/*.sh
%{_libdir}/clisp-2.49.93+/fastcgi/README
%{_libdir}/clisp-2.49.93+/fastcgi/Makefile
%{_libdir}/clisp-2.49.93+/fastcgi/*.h
%{_libdir}/clisp-2.49.93+/fastcgi/*.lisp
%{_libdir}/clisp-2.49.93+/fastcgi/*.o
%{_libdir}/clisp-2.49.93+/fastcgi/*.sh
%{_libdir}/clisp-2.49.93+/full/*.a
%{_libdir}/clisp-2.49.93+/full/*.h
%{_libdir}/clisp-2.49.93+/full/*.o
%{_libdir}/clisp-2.49.93+/full/makevars
%{_libdir}/clisp-2.49.93+/gdbm/Makefile
%{_libdir}/clisp-2.49.93+/gdbm/*.h
%{_libdir}/clisp-2.49.93+/gdbm/*.lisp
%{_libdir}/clisp-2.49.93+/gdbm/*.o
%{_libdir}/clisp-2.49.93+/gdbm/*.sh
%{_libdir}/clisp-2.49.93+/gtk2/Makefile
%{_libdir}/clisp-2.49.93+/gtk2/*.h
%{_libdir}/clisp-2.49.93+/gtk2/*.cfg
%{_libdir}/clisp-2.49.93+/gtk2/*.glade
%{_libdir}/clisp-2.49.93+/gtk2/*.lisp
%{_libdir}/clisp-2.49.93+/gtk2/*.o
%{_libdir}/clisp-2.49.93+/gtk2/*.sh
%{_libdir}/clisp-2.49.93+/libsvm/README
%{_libdir}/clisp-2.49.93+/libsvm/Makefile
%{_libdir}/clisp-2.49.93+/libsvm/*.h
%{_libdir}/clisp-2.49.93+/libsvm/*.lisp
%{_libdir}/clisp-2.49.93+/libsvm/*.o
%{_libdir}/clisp-2.49.93+/libsvm/*.sh
%{_libdir}/clisp-2.49.93+/linkkit/
%{_libdir}/clisp-2.49.93+/pari/README
%{_libdir}/clisp-2.49.93+/pari/Makefile
%{_libdir}/clisp-2.49.93+/pari/*.h
%{_libdir}/clisp-2.49.93+/pari/*.lisp
%{_libdir}/clisp-2.49.93+/pari/*.o
%{_libdir}/clisp-2.49.93+/pari/*.sh
%{_libdir}/clisp-2.49.93+/pcre/Makefile
%{_libdir}/clisp-2.49.93+/pcre/*.h
%{_libdir}/clisp-2.49.93+/pcre/*.lisp
%{_libdir}/clisp-2.49.93+/pcre/*.o
%{_libdir}/clisp-2.49.93+/pcre/*.sh
%{_libdir}/clisp-2.49.93+/postgresql/README
%{_libdir}/clisp-2.49.93+/postgresql/Makefile
%{_libdir}/clisp-2.49.93+/postgresql/*.h
%{_libdir}/clisp-2.49.93+/postgresql/*.lisp
%{_libdir}/clisp-2.49.93+/postgresql/*.o
%{_libdir}/clisp-2.49.93+/postgresql/*.sh
%{_libdir}/clisp-2.49.93+/rawsock/demos/
%{_libdir}/clisp-2.49.93+/rawsock/Makefile
%{_libdir}/clisp-2.49.93+/rawsock/*.h
%{_libdir}/clisp-2.49.93+/rawsock/*.lisp
%{_libdir}/clisp-2.49.93+/rawsock/*.o
%{_libdir}/clisp-2.49.93+/rawsock/*.sh
%{_libdir}/clisp-2.49.93+/zlib/Makefile
%{_libdir}/clisp-2.49.93+/zlib/*.lisp
%{_libdir}/clisp-2.49.93+/zlib/*.h
%{_libdir}/clisp-2.49.93+/zlib/*.o
%{_libdir}/clisp-2.49.93+/zlib/*.sh
%{_datadir}/aclocal/clisp.m4

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{commit}
cp -p %{SOURCE1} emacs

# Change URLs not affected by the --hyperspec argument to configure
sed -i.orig 's|lisp.org/HyperSpec/Body/chap-7.html|lispworks.com/documentation/HyperSpec/Body/07_.htm|' \
    src/clos-package.lisp
touch -r src/clos-package.lisp.orig src/clos-package.lisp
rm -f src/clos-package.lisp.orig
for f in src/_README.*; do
  sed -i.orig 's|lisp.org/HyperSpec/FrontMatter|lispworks.com/documentation/HyperSpec/Front|' $f
  touch -r ${f}.orig $f
  rm -f ${f}.orig
done

# We only link against libraries in system directories, so we need -L dir in
# place of -Wl,-rpath -Wl,dir
cp -p src/build-aux/config.rpath config.rpath.orig
sed -i -e 's/${wl}-rpath ${wl}/-L/g' src/build-aux/config.rpath

# Fix modules that need access to symbols in libgnu.a
sed -i 's/\(${GLLIB_A}\) \(${LIBS}\)/-Wl,--whole-archive \1 -Wl,--no-whole-archive \2 -ldl/' src/makemake.in

# When building modules, put -Wl,--as-needed before the libraries to link
sed -i "s/CC='\${CC}'/CC='\${CC} -Wl,--as-needed'/" src/makemake.in

# Enable firefox to be the default browser for displaying documentation
sed -i 's/;; \((setq \*browser\* .*)\)/\1/' src/cfgunix.lisp

# Unpack the CLX manual
tar -C modules/clx -xzf modules/clx/clx-manual.tar.gz
chmod a+rx modules/clx/clx-manual/html
chmod a+r modules/clx/clx-manual/html/*

%build
%setup_compile_flags
#ulimit -s unlimited
# Do not need to specify base modules: i18n, readline, regexp, syscalls.
# The dirkey module currently can only be built on Windows/Cygwin/MinGW.
# The editor module is not in good enough shape to use.
# The matlab, netica, and oracle modules require proprietary code to build.
# The pari module only works with pari 2.3.  Fedora currently has pari 2.5.
# The queens module is intended as an example only, not for actual use.
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--docdir=%{_docdir}/clisp-2.49.93+ \
	--fsstnd=redhat \
	--hyperspec=https://www.lispworks.com/documentation/HyperSpec/ \
	--with-module=asdf \
	--with-module=berkeley-db \
	--with-module=bindings/glibc \
	--with-module=clx/new-clx \
	--with-module=dbus \
	--with-module=fastcgi \
	--with-module=gdbm \
	--with-module=gtk2 \
	--with-module=libsvm \
	--with-module=pari \
	--with-module=pcre \
	--with-module=postgresql \
	--with-module=rawsock \
	--with-module=zlib \
	--with-libreadline \
	--with-ffcall \
	--config \
	build \
	CPPFLAGS="-I%{_includedir}/libsvm" \
	CFLAGS="${RPM_OPT_FLAGS} -Wa,--noexecstack" \
	LDFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed -Wl,-z,relro -Wl,-z,noexecstack"

# Workaround libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' build/libtool
make -C build

%install
%make_install -C build DESTDIR=$RPM_BUILD_ROOT
cp -a build/full %{buildroot}%{_libdir}/clisp-2.49.93+
rm -f $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc/clisp.{dvi,1,ps}
rm -f $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/{COPYRIGHT,GNU-GPL}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/mop-spec.pdf $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/*.png $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/Why-CLISP* $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/regexp.html $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
find $RPM_BUILD_ROOT%{_libdir} -name '*.dvi' | xargs rm -f
%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang
 
# Put back the original config.rpath, and fix executable bits
pwd
ls -l config.rpath.orig $RPM_BUILD_ROOT/%{_libdir}/clisp-2.49.93+/build-aux/
cp -p config.rpath.orig $RPM_BUILD_ROOT/%{_libdir}/clisp-2.49.93+/build-aux/config.rpath

# Fix paths in the Makefiles
for mk in $(find %{buildroot}%{_libdir} -name Makefile); do
  sed -e "s,$PWD/modules,%{_libdir}/clisp-2.49.93+," \
      -e "s,$PWD/build/clisp,%{_bindir}/clisp," \
      -e "s,$PWD/build/linkkit,%{_libdir}/clisp-2.49.93+/linkkit," \
      -i $mk
done
for mk in %{buildroot}%{_libdir}/clisp-2.49.93+/{base,full}/makevars; do
  sed -e "s, -I$PWD[^']*,," \
      -e "s,%{_libdir}/lib\([[:alnum:]]*\)\.so,-l\1,g" \
      -i $mk
done

# Install config.h, which is needed in some cases
for dir in %{buildroot}%{_libdir}/clisp-2.49.93+/*; do
  cp -p build/$(basename $dir)/config.h $dir || :
done
cp -p build/config.h %{buildroot}%{_libdir}/clisp-2.49.93+
cp -p build/clx/new-clx/config.h \
   %{buildroot}%{_libdir}/clisp-2.49.93+/clx/new-clx
 
# Fix broken symlinks in the full set
pushd %{buildroot}%{_libdir}/clisp-2.49.93+/full
for obj in calls gettext readline regexi; do
  rm -f ${obj}.o
  ln -s ../base/${obj}.o ${obj}.o	
done
for obj in libgnu libnoreadline lisp; do
  rm -f ${obj}.a
  ln -s ../base/${obj}.a ${obj}.a
done
for obj in fastcgi fastcgi_wrappers; do
  rm -f ${obj}.o
  ln -s ../fastcgi/${obj}.o ${obj}.o
done
for obj in cpari pari; do
  rm -f ${obj}.o
  ln -s ../pari/${obj}.o ${obj}.o
done
rm -f bdb.o
ln -s ../berkeley-db/bdb.o bdb.o
rm -f clx.o
ln -s ../clx/new-clx/clx.o clx.o
rm -f cpcre.o
ln -s ../pcre/cpcre.o cpcre.o
rm -f dbus.o
ln -s ../dbus/dbus.o dbus.o
rm -f gdbm.o
ln -s ../gdbm/gdbm.o gdbm.o
rm -f gtk.o
ln -s ../gtk2/gtk.o gtk.o
rm -f libsvm.o
ln -s ../libsvm/libsvm.o libsvm.o
rm -f linux.o
ln -s ../bindings/glibc/linux.o linux.o
rm -f postgresql.o
ln -s ../postgresql/postgresql.o postgresql.o
rm -f rawsock.o
ln -s ../rawsock/rawsock.o rawsock.o
rm -f zlib.o
ln -s ../zlib/zlib.o zlib.o
popd
 
# Help the debuginfo generator
ln -s ../../src/modules.c build/base/modules.c
ln -s ../../src/modules.c build/full/modules.c

%check
make -C build check

