# clisp can't run properly if LTO is used
%define _disable_lto 1

# define missing macro for Emacs
%{?!%_emacs_bytecompile:%global _emacs_bytecompile emacs -batch --no-init-file --no-site-file --eval '(progn (setq load-path (cons "." load-path)))' -f batch-byte-compile}
%{?!%_emacs_sitelispdir:%global _emacs_sitelispdir %{_datadir}/emacs/site-lisp}
%{?!%_emacs_sitestartdir:%global _emacs_sitestartdir %{_datadir}/emacs/site-lisp/site-start.d}

# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		79cbafdbc6337d6dcd8f2dbad69fb7ebf7a46012
	%global commitdate	20230212
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

%bcond_without	db
%bcond_without	dbus
%bcond_without	fgci
%bcond_without	gdbm
# gtk3 is not supported, for now
%bcond_with		gtk2
%bcond_without	libsvm
%bcond_without	libx
%bcond_without	pari
%bcond_without	postgresql
%bcond_with	tests

Summary:	ANSI Common Lisp implementation
Name:		clisp
Version:	2.49.93
Release:	2
Group:		Development/Other
License:	GPLv2
%if 0%{?snapshot}
Source0:	https://gitlab.com/gnu-clisp/clisp/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
%else
#Source0:	https://ftp.gnu.org/pub/gnu/clisp/latest/%{name}-%{version}.tar.bz2
#Source0:	https://gitlab.com/gnu-clisp/clisp/-/archive/%{name}-%{version}-approx/clisp-%{name}-%{version}-approx.tar.bz2
Source0:	https://downloads.sourceforge.net/clisp/%{name}-%{version}.tar.bz2
%endif
# Upstream dropped this file from the distribution
Source1:	https://gitlab.com/sam-s/clhs/-/raw/master/clhs.el
# https://sourceforge.net/tracker/?func=detail&aid=3572516&group_id=1355&atid=301355
Patch0:		%{name}-db.patch
# https://sourceforge.net/tracker/?func=detail&aid=3529607&group_id=1355&atid=301355
Patch1:		%{name}-format.patch
# The combination of register and volatile is nonsensical
Patch2:		%{name}-register-volatile.patch
# A test that writes to /dev/pts/0 succeeds or fails apparently at random.
# I can only guess that /dev/pts/0 may or may not be what the test expects.
# Perhaps we are racing with something else that allocates a pty.  Disable
# the test for now.
Patch3:		%{name}-pts-access.patch
Patch4:		%{name}-c99.patch
# (upstream) https://sourceforge.net/tracker/?func=detail&aid=3529615&group_id=1355&atid=301355
#Patch1:		%{name}-arm.patch
# (upstream) https://sourceforge.net/tracker/?func=detail&aid=3572511&group_id=1355&atid=301355
#Patch2:		%{name}-libsvm.patch
# Linux-specific fixes.  Sent upstream 25 Jul 2012.
Patch5:		%{name}-linux.patch
# (fedora)
Patch10:	%{name}-pari.patch

BuildRequires:	gettext-devel
BuildRequires:	imake
BuildRequires:	locales-en
%if %{with db}
BuildRequires:	db-devel	
%endif
BuildRequires:	diffutils
BuildRequires:	emacs
%if %{with fcgi}
BuildRequires:	fcgi-devel
%endif
BuildRequires:	ffcall-devel
%if %{with gdbm}
BuildRequires:	gdbm-devel
%endif
##BuildRequires:	ghostscript
##BuildRequires:	groff
BuildRequires:	libsigsegv-devel
%if %{with libsvm}
BuildRequires:	libsvm-devel
%endif
%if %{with pari}
BuildRequires:	pari
BuildRequires:	libpari-devel
%endif
%if %{with dbus}
BuildRequires:	pkgconfig(dbus-1)
%endif
%if %{with gtk2}
BuildRequires:	pkgconfig(gtk-2.0)
%endif
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libxcrypt)
%if %{with postgresql}
BuildRequires:	pkgconfig(libpq)
%endif
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xext)
#BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xpm)
#BuildRequires:	pkgconfig(xrender)
%if %{with libz}
BuildRequires:	pkgconfig(zlib)
%endif

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
%dir %{_libdir}/%{name}-%{version}+/
%dir %{_libdir}/%{name}-%{version}+/asdf/
%{_libdir}/%{name}-%{version}+/asdf/asdf.fas
%dir %{_libdir}/%{name}-%{version}+/base/
%{_libdir}/%{name}-%{version}+/base/lispinit.mem
%{_libdir}/%{name}-%{version}+/base/lisp.run
%if %{with db}
%dir %{_libdir}/%{name}-%{version}+/berkeley-db/
%{_libdir}/%{name}-%{version}+/berkeley-db/*.fas
%{_libdir}/%{name}-%{version}+/berkeley-db/preload.lisp
%endif
%dir %{_libdir}/%{name}-%{version}+/bindings/
%dir %{_libdir}/%{name}-%{version}+/bindings/glibc/
%{_libdir}/%{name}-%{version}+/bindings/glibc/*.fas
%dir %{_libdir}/%{name}-%{version}+/clx/
%dir %{_libdir}/%{name}-%{version}+/clx/new-clx/
%{_libdir}/%{name}-%{version}+/clx/new-clx/*.fas
%{_libdir}/%{name}-%{version}+/clx/new-clx/clx-preload.lisp
%{_libdir}/%{name}-%{version}+/data/
%if %{with dbus}
%dir %{_libdir}/%{name}-%{version}+/dbus/
%{_libdir}/%{name}-%{version}+/dbus/*.fas
%endif
%{_libdir}/%{name}-%{version}+/dynmod/
%if %{with fcgi}
%dir %{_libdir}/%{name}-%{version}+/fastcgi/
%{_libdir}/%{name}-%{version}+/fastcgi/*.fas
%endif
%dir %{_libdir}/%{name}-%{version}+/full/
%{_libdir}/%{name}-%{version}+/full/lispinit.mem
%{_libdir}/%{name}-%{version}+/full/lisp.run
%if %{with gdbm}
%dir %{_libdir}/%{name}-%{version}+/gdbm/
%{_libdir}/%{name}-%{version}+/gdbm/*.fas
%{_libdir}/%{name}-%{version}+/gdbm/preload.lisp
%endif
%if %{with gtk2}
%dir %{_libdir}/%{name}-%{version}+/gtk2/
%{_libdir}/%{name}-%{version}+/gtk2/*.fas
%{_libdir}/%{name}-%{version}+/gtk2/preload.lisp
%endif
%if %{with libsvm}
%dir %{_libdir}/%{name}-%{version}+/libsvm/
%{_libdir}/%{name}-%{version}+/libsvm/*.fas
%{_libdir}/%{name}-%{version}+/libsvm/preload.lisp
%endif
%if %{with pari}
%dir %{_libdir}/%{name}-%{version}+/pari/
%{_libdir}/%{name}-%{version}+/pari/*.fas
%{_libdir}/%{name}-%{version}+/pari/preload.lisp
%endif
%dir %{_libdir}/%{name}-%{version}+/pcre/
%{_libdir}/%{name}-%{version}+/pcre/*.fas
%{_libdir}/%{name}-%{version}+/pcre/preload.lisp
%if %{with postgresql}
%dir %{_libdir}/%{name}-%{version}+/postgresql/
%{_libdir}/%{name}-%{version}+/postgresql/*.fas
%endif
%dir %{_libdir}/%{name}-%{version}+/rawsock/
%{_libdir}/%{name}-%{version}+/rawsock/*.fas
%{_libdir}/%{name}-%{version}+/rawsock/preload.lisp
%if %{with libz}
%dir %{_libdir}/%{name}-%{version}+/zlib/
%{_libdir}/%{name}-%{version}+/zlib/*.fas
%endif
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
%{_libdir}/%{name}-%{version}+/asdf/Makefile
%{_libdir}/%{name}-%{version}+/asdf/*.lisp
%{_libdir}/%{name}-%{version}+/asdf/*.sh
%{_libdir}/%{name}-%{version}+/base/*.a
%{_libdir}/%{name}-%{version}+/base/*.o
%{_libdir}/%{name}-%{version}+/base/*.h
%{_libdir}/%{name}-%{version}+/base/makevars
%if %{with db}
%{_libdir}/%{name}-%{version}+/berkeley-db/Makefile
%{_libdir}/%{name}-%{version}+/berkeley-db/*.h
%{_libdir}/%{name}-%{version}+/berkeley-db/*.lisp
%{_libdir}/%{name}-%{version}+/berkeley-db/*.o
%{_libdir}/%{name}-%{version}+/berkeley-db/*.sh
%endif
%{_libdir}/%{name}-%{version}+/bindings/glibc/Makefile
%{_libdir}/%{name}-%{version}+/bindings/glibc/*.lisp
%{_libdir}/%{name}-%{version}+/bindings/glibc/*.o
%{_libdir}/%{name}-%{version}+/bindings/glibc/*.sh
%{_libdir}/%{name}-%{version}+/build-aux/
%{_libdir}/%{name}-%{version}+/clx/new-clx/demos/
%{_libdir}/%{name}-%{version}+/clx/new-clx/README
%{_libdir}/%{name}-%{version}+/clx/new-clx/Makefile
%{_libdir}/%{name}-%{version}+/clx/new-clx/*.h
%{_libdir}/%{name}-%{version}+/clx/new-clx/*.lisp
%{_libdir}/%{name}-%{version}+/clx/new-clx/*.o
%{_libdir}/%{name}-%{version}+/clx/new-clx/*.sh
%{_libdir}/%{name}-%{version}+/config.h
%if %{with dbus}
%{_libdir}/%{name}-%{version}+/dbus/Makefile
%{_libdir}/%{name}-%{version}+/dbus/*.h
%{_libdir}/%{name}-%{version}+/dbus/*.lisp
%{_libdir}/%{name}-%{version}+/dbus/*.o
%{_libdir}/%{name}-%{version}+/dbus/*.sh
%endif
%if %{with fcgi}
%{_libdir}/%{name}-%{version}+/fastcgi/README
%{_libdir}/%{name}-%{version}+/fastcgi/Makefile
%{_libdir}/%{name}-%{version}+/fastcgi/*.h
%{_libdir}/%{name}-%{version}+/fastcgi/*.lisp
%{_libdir}/%{name}-%{version}+/fastcgi/*.o
%{_libdir}/%{name}-%{version}+/fastcgi/*.sh
%endif
%{_libdir}/%{name}-%{version}+/full/*.a
%{_libdir}/%{name}-%{version}+/full/*.h
%{_libdir}/%{name}-%{version}+/full/*.o
%{_libdir}/%{name}-%{version}+/full/makevars
%if %{with gdbm}
%{_libdir}/%{name}-%{version}+/gdbm/Makefile
%{_libdir}/%{name}-%{version}+/gdbm/*.h
%{_libdir}/%{name}-%{version}+/gdbm/*.lisp
%{_libdir}/%{name}-%{version}+/gdbm/*.o
%{_libdir}/%{name}-%{version}+/gdbm/*.sh
%endif
%if %{with gtk2}
%{_libdir}/%{name}-%{version}+/gtk2/Makefile
%{_libdir}/%{name}-%{version}+/gtk2/*.h
%{_libdir}/%{name}-%{version}+/gtk2/*.cfg
%{_libdir}/%{name}-%{version}+/gtk2/*.glade
%{_libdir}/%{name}-%{version}+/gtk2/*.lisp
%{_libdir}/%{name}-%{version}+/gtk2/*.o
%{_libdir}/%{name}-%{version}+/gtk2/*.sh
%endif
%if %{with libsvm}
%{_libdir}/%{name}-%{version}+/libsvm/README
%{_libdir}/%{name}-%{version}+/libsvm/Makefile
%{_libdir}/%{name}-%{version}+/libsvm/*.h
%{_libdir}/%{name}-%{version}+/libsvm/*.lisp
%{_libdir}/%{name}-%{version}+/libsvm/*.o
%{_libdir}/%{name}-%{version}+/libsvm/*.sh
%endif
%{_libdir}/%{name}-%{version}+/linkkit/
%if %{with pari}
%{_libdir}/%{name}-%{version}+/pari/README
%{_libdir}/%{name}-%{version}+/pari/Makefile
%{_libdir}/%{name}-%{version}+/pari/*.h
%{_libdir}/%{name}-%{version}+/pari/*.lisp
%{_libdir}/%{name}-%{version}+/pari/*.o
%{_libdir}/%{name}-%{version}+/pari/*.sh
%endif
%{_libdir}/%{name}-%{version}+/pcre/Makefile
%{_libdir}/%{name}-%{version}+/pcre/*.h
%{_libdir}/%{name}-%{version}+/pcre/*.lisp
%{_libdir}/%{name}-%{version}+/pcre/*.o
%{_libdir}/%{name}-%{version}+/pcre/*.sh
%if %{with postgresql}
%{_libdir}/%{name}-%{version}+/postgresql/README
%{_libdir}/%{name}-%{version}+/postgresql/Makefile
%{_libdir}/%{name}-%{version}+/postgresql/*.h
%{_libdir}/%{name}-%{version}+/postgresql/*.lisp
%{_libdir}/%{name}-%{version}+/postgresql/*.o
%{_libdir}/%{name}-%{version}+/postgresql/*.sh
%endif
%{_libdir}/%{name}-%{version}+/rawsock/demos/
%{_libdir}/%{name}-%{version}+/rawsock/Makefile
%{_libdir}/%{name}-%{version}+/rawsock/*.h
%{_libdir}/%{name}-%{version}+/rawsock/*.lisp
%{_libdir}/%{name}-%{version}+/rawsock/*.o
%{_libdir}/%{name}-%{version}+/rawsock/*.sh
%if %{with libz}
%{_libdir}/%{name}-%{version}+/zlib/Makefile
%{_libdir}/%{name}-%{version}+/zlib/*.lisp
%{_libdir}/%{name}-%{version}+/zlib/*.h
%{_libdir}/%{name}-%{version}+/zlib/*.o
%{_libdir}/%{name}-%{version}+/zlib/*.sh
%endif
%{_datadir}/aclocal/clisp.m4

#---------------------------------------------------------------------------

%prep
%autosetup -p0 -n %{?snapshot:%{name}-%{commit}}
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
export LC_ALL=C.UTF-8
#setup_compile_flags
#ulimit -s unlimited

# Do not need to specify base modules: i18n, readline, regexp, syscalls.
# The dirkey module currently can only be built on Windows/Cygwin/MinGW.
# The editor module is not in good enough shape to use.
# The matlab, netica, and oracle modules require proprietary code to build.
# The queens module is intended as an example only, not for actual use.
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--docdir=%{_docdir}/%{name}-%{version}+ \
	--fsstnd=%{vendor}redhat \
	--hyperspec=https://www.lispworks.com/documentation/HyperSpec/ \
	--with-module=asdf \
%if %{with db}
	--with-module=berkeley-db \
%endif
	--with-module=bindings/glibc \
	--with-module=clx/new-clx \
%if %{with dbus}
	--with-module=dbus \
%endif
%if %{with fcgi}
	--with-module=fastcgi \
%endif
%if %{with gdbm}
	--with-module=gdbm \
%endif
%if %{with gtk2}
	--with-module=gtk2 \
%endif
%if %{with libsvm}
	--with-module=libsvm \
%endif
%if %{with pari}
	--with-module=pari \
%endif
	--with-module=pcre \
%if %{with postgresql}
	--with-module=postgresql \
%endif
	--with-module=rawsock \
%if %{with libz}
	--with-module=zlib \
%endif
	--with-libreadline \
	--with-ffcall \
	--config \
	build \
	CPPFLAGS="-I%{_includedir}/libsvm" \
	CFLAGS="%{optflags} -Wa,--noexecstack" \
	LDFLAGS="%{optflags} -Wl,--as-needed -Wl,-z,relro -Wl,-z,noexecstack"

# Workaround libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' build/libtool
%make -j1 -C build

%install
%make_install -C build DESTDIR=%{buildroot}
cp -a build/full %{buildroot}%{_libdir}/%{name}-%{version}+
rm -f %{buildroot}%{_docdir}/clisp-%{version}+/doc/clisp.{dvi,1,ps}
rm -f %{buildroot}%{_docdir}/clisp-%{version}+/{COPYRIGHT,GNU-GPL}
mkdir -p %{buildroot}%{_docdir}/clisp-%{version}+/doc
cp -p doc/mop-spec.pdf %{buildroot}%{_docdir}/clisp-%{version}+/doc
cp -p doc/*.png %{buildroot}%{_docdir}/clisp-%{version}+/doc
cp -p doc/Why-CLISP* %{buildroot}%{_docdir}/clisp-%{version}+/doc
cp -p doc/regexp.html %{buildroot}%{_docdir}/clisp-%{version}+/doc
find %{buildroot}%{_libdir} -name '*.dvi' | xargs rm -f

# locales
%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang

# Compile the Emacs interface
pushd %{buildroot}%{_datadir}/emacs/site-lisp
%{_emacs_bytecompile} *.el
popd

# Put back the original config.rpath, and fix executable bits
cp -p config.rpath.orig %{buildroot}/%{_libdir}/%{name}-%{version}+/build-aux/config.rpath

# Fix paths in the Makefiles
for mk in $(find %{buildroot}%{_libdir} -name Makefile); do
	sed -e "s,$PWD/modules,%{_libdir}/%{name}-%{version}+," \
		-e "s,$PWD/build/clisp,%{_bindir}/clisp," \
		-e "s,$PWD/build/linkkit,%{_libdir}/%{name}-%{version}+/linkkit," \
		-i $mk
done
for mk in %{buildroot}%{_libdir}/%{name}-%{version}+/{base,full}/makevars; do
	sed -e "s, -I$PWD[^']*,," \
		-e "s,%{_libdir}/lib\([[:alnum:]]*\)\.so,-l\1,g" \
		-i $mk
done

# Install config.h, which is needed in some cases
for dir in %{buildroot}%{_libdir}/%{name}-%{version}+/*; do
	cp -p build/$(basename $dir)/config.h $dir || :
done
cp -p build/config.h %{buildroot}%{_libdir}/%{name}-%{version}+
cp -p build/clx/new-clx/config.h \
	%{buildroot}%{_libdir}/%{name}-%{version}+/clx/new-clx
 
# Fix broken symlinks in the full set
pushd %{buildroot}%{_libdir}/%{name}-%{version}+/full
for obj in calls gettext readline regexi; do
	rm -f ${obj}.o
	ln -s ../base/${obj}.o ${obj}.o	
done
for obj in libgnu libnoreadline lisp; do
	rm -f ${obj}.a
	ln -s ../base/${obj}.a ${obj}.a
done
%if %{with fcgi}
for obj in fastcgi fastcgi_wrappers; do
	rm -f ${obj}.o
	ln -s ../fastcgi/${obj}.o ${obj}.o
done
%endif
%if %{with pari}
for obj in cpari pari; do
	rm -f ${obj}.o
	ln -s ../pari/${obj}.o ${obj}.o
done
%endif
%if %{with db}
rm -f bdb.o
ln -s ../berkeley-db/bdb.o bdb.o
%endif
rm -f clx.o
ln -s ../clx/new-clx/clx.o clx.o
rm -f cpcre.o
ln -s ../pcre/cpcre.o cpcre.o
%if %{with dbus}
rm -f dbus.o
ln -s ../dbus/dbus.o dbus.o
%endif
%if %{with gdbm}
rm -f gdbm.o
ln -s ../gdbm/gdbm.o gdbm.o
%endif
%if %{with gtk2}
rm -f gtk.o
ln -s ../gtk2/gtk.o gtk.o
%endif
%if %{with libsvm}
rm -f libsvm.o
ln -s ../libsvm/libsvm.o libsvm.o
%endif
rm -f linux.o
ln -s ../bindings/glibc/linux.o linux.o
%if %{with postgresql}
rm -f postgresql.o
ln -s ../postgresql/postgresql.o postgresql.o
%endif
rm -f rawsock.o
ln -s ../rawsock/rawsock.o rawsock.o
%if %{with libz}
rm -f zlib.o
ln -s ../zlib/zlib.o zlib.o
%endif
popd
 
# Help the debuginfo generator
ln -s ../../src/modules.c build/base/modules.c
ln -s ../../src/modules.c build/full/modules.c

%if %{with tests}
%check
export LC_ALL=C.UTF-8
%make -j1 -C build check
%make -j1 -C build extracheck
%make -j1 -C build base-mod-check
%endif

