# Mercurial snapshot
%global hgver 20130208hg

Epoch:		1
Name:		clisp
Summary:	ANSI Common Lisp implementation
Version:	2.49
Release:	2.%{hgver}

Group:		Development/Other
License:	GPLv2

# The source for this package was pulled from upstream's mercurial repository.
# Use the following commands to generate the tarball:
#   hg clone -u 6c160a19948d \
#     http://clisp.hg.sourceforge.net:8000/hgroot/clisp/clisp clisp-2.49
#   rm -fr clisp-2.49/.hg*
#   tar cvjf clisp-2.49-20130208hg.tar.bz2 clisp-2.49
Source0:	%{name}-%{version}-%{hgver}.tar.bz2   
#Source0:	http://downloads.sourceforge.net/clisp/%{name}-%{version}.tar.bz2
# http://sourceforge.net/tracker/?func=detail&aid=3529607&group_id=1355&atid=301355
Patch0:		%{name}-format.patch
# http://sourceforge.net/tracker/?func=detail&aid=3529615&group_id=1355&atid=301355
Patch1:		%{name}-arm.patch
# http://sourceforge.net/tracker/?func=detail&aid=3572511&group_id=1355&atid=301355
Patch2:		%{name}-libsvm.patch
# http://sourceforge.net/tracker/?func=detail&aid=3572516&group_id=1355&atid=301355
Patch3:		%{name}-db.patch
# Linux-specific fixes.  Sent upstream 25 Jul 2012.
Patch4:		%{name}-linux.patch

Provides:	ansi-cl
BuildRequires:	db5-devel
BuildRequires:	diffutils
BuildRequires:	dbus-devel
BuildRequires:	emacs
BuildRequires:	fcgi-devel
BuildRequires:	ffcall-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	gtk+2.0-devel
#BuildRequires:	libpari-devel
BuildRequires:	libsigsegv-devel
BuildRequires:	libsvm-devel
BuildRequires:	libxft-devel
BuildRequires:	libxrender-devel
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pcre-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	xaw-devel
BuildRequires:	zlib-devel

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

%package	devel
Summary:	Development files for CLISP
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description	devel
Files necessary for linking CLISP.

%prep
%setup -q -n %{name}-%{version}
%patch0
%patch1
%patch2
%patch3
%patch4

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

# Enable firefox to be the default browser for displaying documentation
sed -i 's/;; \((setq \*browser\* .*)\)/\1/' src/cfgunix.lisp

# Unpack the CLX manual
tar -C modules/clx -xzf modules/clx/clx-manual.tar.gz
chmod a+rx modules/clx/clx-manual/html
chmod a+r modules/clx/clx-manual/html/*

%build

# Why keep reverting when switching back to ld.bfd
# like all other distros do...
mkdir bin
ln -sf %{_bindir}/ld.bfd bin/ld
export PATH=$PWD/bin:$PATH

ulimit -s unlimited
# Do not need to specify base modules: i18n, readline, regexp, syscalls.
# The dirkey module currently can only be built on Windows/Cygwin/MinGW.
# The editor module is not in good enough shape to use.
# The matlab, netica, and oracle modules require proprietary code to build.
# The pari module only works with pari 2.3.  Fedora currently has pari 2.5.
# The queens module is intended as an example only, not for actual use.
./configure --prefix=%{_prefix} \
	    --libdir=%{_libdir} \
	    --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
	    --docdir=%{_docdir}/clisp-%{version}+ \
	    --fsstnd=redhat \
	    --hyperspec=http://www.lispworks.com/documentation/HyperSpec/ \
	    --with-module=asdf \
	    --with-module=berkeley-db \
	    --with-module=bindings/glibc \
	    --with-module=clx/new-clx \
	    --with-module=dbus \
	    --with-module=fastcgi \
	    --with-module=gdbm \
	    --with-module=gtk2 \
	    --with-module=libsvm \
	    --with-module=pcre \
	    --with-module=postgresql \
	    --with-module=rawsock \
	    --with-module=zlib \
	    --with-libreadline \
	    --cbc \
	    build \
	    CPPFLAGS="-I%{_includedir}/libsvm" \
	    CFLAGS="${RPM_OPT_FLAGS} -Wa,--noexecstack" \
	    LDFLAGS="${RPM_LD_FLAGS} -Wl,-z,noexecstack"

make -C build

%check
make -C build check

%install
make -C build DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc/clisp.{dvi,1,ps}
cp -p doc/mop-spec.pdf $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/*.png $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/Why-CLISP* $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
cp -p doc/regexp.html $RPM_BUILD_ROOT%{_docdir}/clisp-%{version}+/doc
find $RPM_BUILD_ROOT%{_libdir} -name '*.dvi' | xargs rm -f
%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang

# Put back the original config.rpath, and fix executable bits
cp -p config.rpath.orig $RPM_BUILD_ROOT/%{_libdir}/clisp-%{version}+/build-aux/config.rpath
chmod a+x \
  $RPM_BUILD_ROOT/%{_libdir}/clisp-%{version}+/build-aux/config.guess \
  $RPM_BUILD_ROOT/%{_libdir}/clisp-%{version}+/build-aux/config.sub \
  $RPM_BUILD_ROOT/%{_libdir}/clisp-%{version}+/build-aux/depcomp \
  $RPM_BUILD_ROOT/%{_libdir}/clisp-%{version}+/build-aux/install-sh \

%files -f %{name}.lang
%{_bindir}/clisp
%{_mandir}/man1/clisp.1*
%{_docdir}/clisp-%{version}+
%dir %{_libdir}/clisp-%{version}+/
%dir %{_libdir}/clisp-%{version}+/asdf/
%{_libdir}/clisp-%{version}+/asdf/asdf.fas
%dir %{_libdir}/clisp-%{version}+/base/
%{_libdir}/clisp-%{version}+/base/lispinit.mem
%{_libdir}/clisp-%{version}+/base/lisp.run
%dir %{_libdir}/clisp-%{version}+/berkeley-db/
%{_libdir}/clisp-%{version}+/berkeley-db/*.fas
%dir %{_libdir}/clisp-%{version}+/bindings/
%dir %{_libdir}/clisp-%{version}+/bindings/glibc/
%{_libdir}/clisp-%{version}+/bindings/glibc/*.fas
%dir %{_libdir}/clisp-%{version}+/clx/
%dir %{_libdir}/clisp-%{version}+/clx/new-clx/
%{_libdir}/clisp-%{version}+/clx/new-clx/*.fas
%{_libdir}/clisp-%{version}+/data/
%dir %{_libdir}/clisp-%{version}+/dbus/
%{_libdir}/clisp-%{version}+/dbus/*.fas
%{_libdir}/clisp-%{version}+/dynmod/
%dir %{_libdir}/clisp-%{version}+/fastcgi/
%{_libdir}/clisp-%{version}+/fastcgi/*.fas
%dir %{_libdir}/clisp-%{version}+/gdbm/
%{_libdir}/clisp-%{version}+/gdbm/*.fas
%dir %{_libdir}/clisp-%{version}+/gtk2/
%{_libdir}/clisp-%{version}+/gtk2/*.fas
%dir %{_libdir}/clisp-%{version}+/libsvm/
%{_libdir}/clisp-%{version}+/libsvm/*.fas
#%%dir %%{_libdir}/clisp-%%{version}/pari/
#%%{_libdir}/clisp-%%{version}/pari/*.fas
%dir %{_libdir}/clisp-%{version}+/pcre/
%{_libdir}/clisp-%{version}+/pcre/*.fas
%dir %{_libdir}/clisp-%{version}+/postgresql/
%{_libdir}/clisp-%{version}+/postgresql/*.fas
%dir %{_libdir}/clisp-%{version}+/rawsock/
%{_libdir}/clisp-%{version}+/rawsock/*.fas
%dir %{_libdir}/clisp-%{version}+/zlib/
%{_libdir}/clisp-%{version}+/zlib/*.fas
%{_datadir}/emacs/site-lisp/*
%{_datadir}/vim/vimfiles/after/syntax/*

%files devel
%doc modules/clx/clx-manual
%{_bindir}/clisp-link
%{_mandir}/man1/clisp-link.1*
%{_libdir}/clisp-%{version}+/asdf/Makefile
%{_libdir}/clisp-%{version}+/asdf/*.lisp
%{_libdir}/clisp-%{version}+/asdf/*.sh
%{_libdir}/clisp-%{version}+/base/*.a
%{_libdir}/clisp-%{version}+/base/*.o
%{_libdir}/clisp-%{version}+/base/*.h
%{_libdir}/clisp-%{version}+/base/makevars
%{_libdir}/clisp-%{version}+/berkeley-db/Makefile
%{_libdir}/clisp-%{version}+/berkeley-db/*.lisp
%{_libdir}/clisp-%{version}+/berkeley-db/*.o
%{_libdir}/clisp-%{version}+/berkeley-db/*.sh
%{_libdir}/clisp-%{version}+/bindings/glibc/Makefile
%{_libdir}/clisp-%{version}+/bindings/glibc/*.lisp
%{_libdir}/clisp-%{version}+/bindings/glibc/*.o
%{_libdir}/clisp-%{version}+/bindings/glibc/*.sh
%{_libdir}/clisp-%{version}+/build-aux/
%{_libdir}/clisp-%{version}+/clx/new-clx/demos/
%{_libdir}/clisp-%{version}+/clx/new-clx/README
%{_libdir}/clisp-%{version}+/clx/new-clx/Makefile
%{_libdir}/clisp-%{version}+/clx/new-clx/*.lisp
%{_libdir}/clisp-%{version}+/clx/new-clx/*.o
%{_libdir}/clisp-%{version}+/clx/new-clx/*.sh
%{_libdir}/clisp-%{version}+/dbus/Makefile
%{_libdir}/clisp-%{version}+/dbus/*.lisp
%{_libdir}/clisp-%{version}+/dbus/*.o
%{_libdir}/clisp-%{version}+/dbus/*.sh
%{_libdir}/clisp-%{version}+/fastcgi/README
%{_libdir}/clisp-%{version}+/fastcgi/Makefile
%{_libdir}/clisp-%{version}+/fastcgi/*.lisp
%{_libdir}/clisp-%{version}+/fastcgi/*.o
%{_libdir}/clisp-%{version}+/fastcgi/*.sh
%{_libdir}/clisp-%{version}+/gdbm/Makefile
%{_libdir}/clisp-%{version}+/gdbm/*.lisp
%{_libdir}/clisp-%{version}+/gdbm/*.o
%{_libdir}/clisp-%{version}+/gdbm/*.sh
%{_libdir}/clisp-%{version}+/gtk2/Makefile
%{_libdir}/clisp-%{version}+/gtk2/*.cfg
%{_libdir}/clisp-%{version}+/gtk2/*.glade
%{_libdir}/clisp-%{version}+/gtk2/*.lisp
%{_libdir}/clisp-%{version}+/gtk2/*.o
%{_libdir}/clisp-%{version}+/gtk2/*.sh
%{_libdir}/clisp-%{version}+/libsvm/README
%{_libdir}/clisp-%{version}+/libsvm/Makefile
%{_libdir}/clisp-%{version}+/libsvm/*.lisp
%{_libdir}/clisp-%{version}+/libsvm/*.o
%{_libdir}/clisp-%{version}+/libsvm/*.sh
%{_libdir}/clisp-%{version}+/linkkit/
#%%{_libdir}/clisp-%%{version}/pari/README
#%%{_libdir}/clisp-%%{version}/pari/Makefile
#%%{_libdir}/clisp-%%{version}/pari/*.lisp
#%%{_libdir}/clisp-%%{version}/pari/*.o
#%%{_libdir}/clisp-%%{version}/pari/*.sh
%{_libdir}/clisp-%{version}+/pcre/Makefile
%{_libdir}/clisp-%{version}+/pcre/*.lisp
%{_libdir}/clisp-%{version}+/pcre/*.o
%{_libdir}/clisp-%{version}+/pcre/*.sh
%{_libdir}/clisp-%{version}+/postgresql/README
%{_libdir}/clisp-%{version}+/postgresql/Makefile
%{_libdir}/clisp-%{version}+/postgresql/*.lisp
%{_libdir}/clisp-%{version}+/postgresql/*.o
%{_libdir}/clisp-%{version}+/postgresql/*.sh
%{_libdir}/clisp-%{version}+/rawsock/demos/
%{_libdir}/clisp-%{version}+/rawsock/Makefile
%{_libdir}/clisp-%{version}+/rawsock/*.lisp
%{_libdir}/clisp-%{version}+/rawsock/*.o
%{_libdir}/clisp-%{version}+/rawsock/*.sh
%{_libdir}/clisp-%{version}+/zlib/Makefile
%{_libdir}/clisp-%{version}+/zlib/*.lisp
%{_libdir}/clisp-%{version}+/zlib/*.o
%{_libdir}/clisp-%{version}+/zlib/*.sh
%{_datadir}/aclocal/clisp.m4
