#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RandomFields
Version  : 3.3.14
Release  : 53
URL      : https://cran.r-project.org/src/contrib/RandomFields_3.3.14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RandomFields_3.3.14.tar.gz
Summary  : Simulation and Analysis of Random Fields
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: R-RandomFields-lib = %{version}-%{release}
Requires: R-RandomFieldsUtils
Requires: R-sp
BuildRequires : R-RandomFieldsUtils
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-RandomFields package.
Group: Libraries

%description lib
lib components for the R-RandomFields package.


%prep
%setup -q -c -n RandomFields
cd %{_builddir}/RandomFields

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642610245

%install
export SOURCE_DATE_EPOCH=1642610245
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RandomFields
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RandomFields
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RandomFields
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RandomFields || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RandomFields/CITATION
/usr/lib64/R/library/RandomFields/DESCRIPTION
/usr/lib64/R/library/RandomFields/INDEX
/usr/lib64/R/library/RandomFields/LICENCE.for.sse2neon.h
/usr/lib64/R/library/RandomFields/Meta/Rd.rds
/usr/lib64/R/library/RandomFields/Meta/data.rds
/usr/lib64/R/library/RandomFields/Meta/features.rds
/usr/lib64/R/library/RandomFields/Meta/hsearch.rds
/usr/lib64/R/library/RandomFields/Meta/links.rds
/usr/lib64/R/library/RandomFields/Meta/nsInfo.rds
/usr/lib64/R/library/RandomFields/Meta/package.rds
/usr/lib64/R/library/RandomFields/NAMESPACE
/usr/lib64/R/library/RandomFields/R/RandomFields
/usr/lib64/R/library/RandomFields/R/RandomFields.rdb
/usr/lib64/R/library/RandomFields/R/RandomFields.rdx
/usr/lib64/R/library/RandomFields/data/ca20.rda
/usr/lib64/R/library/RandomFields/data/soil.txt.gz
/usr/lib64/R/library/RandomFields/data/weather.rda
/usr/lib64/R/library/RandomFields/help/AnIndex
/usr/lib64/R/library/RandomFields/help/RandomFields.rdb
/usr/lib64/R/library/RandomFields/help/RandomFields.rdx
/usr/lib64/R/library/RandomFields/help/aliases.rds
/usr/lib64/R/library/RandomFields/help/macros/allg_defn.Rd
/usr/lib64/R/library/RandomFields/help/macros/def.Rd
/usr/lib64/R/library/RandomFields/help/macros/defn.Rd
/usr/lib64/R/library/RandomFields/help/macros/lit.Rd
/usr/lib64/R/library/RandomFields/help/paths.rds
/usr/lib64/R/library/RandomFields/html/00Index.html
/usr/lib64/R/library/RandomFields/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RandomFields/libs/RandomFields.so
/usr/lib64/R/library/RandomFields/libs/RandomFields.so.avx2
/usr/lib64/R/library/RandomFields/libs/RandomFields.so.avx512
