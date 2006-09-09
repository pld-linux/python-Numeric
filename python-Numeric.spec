%define		module	Numeric

Summary:	Python numerical facilities
Summary(pl):	Modu³y do obliczeñ numerycznych dla jêzyka Python
Name:		python-%{module}
Version:	24.2
Release:	3
License:	distributable
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	2ae672656e06716a149acb048cca3093
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
Obsoletes:	python-numpy <= 24.2
# dropped some time ago
Obsoletes:	python-numpy-Properties
# dropped some time ago, should have been "released as separate package", but finally wasn't
Obsoletes:	python-numpy-kinds <= 24.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%description -l pl
Pakiet umo¿liwia wydajne obliczenia numeryczne na macierzach
wielowymiarowych.

%package devel
Summary:	C header files for numerical modules
Summary(pl):	Pliki nag³ówkowe jêzyka C modu³ów numerycznych
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-numpy-devel <= 24.2

%description devel
C header files for numerical modules.

%description devel -l pl
Pliki nag³ówkowe jêzyka C modu³ów numerycznych.

%package FFT
Summary:	Interface to the FFTPACK FORTRAN library
Summary(pl):	Interfejs do biblioteki FFTPACK jêzyka Fortran
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-numpy-FFT <= 24.2

%description FFT
The FFT.py module provides a simple interface to the FFTPACK FORTRAN
library, which is a powerful standard library for doing fast Fourier
transforms of real and complex data sets.

%description FFT -l pl
Modu³ FFT zawiera prosty interfejs do biblioteki FFTPACK jêzyka
Fortran. Ta biblioteka o wysokich mo¿liwo¶ciach jest standardowo
u¿ywana do prowadzenia obliczeñ za pomoc± dyskretnej transformaty
Fouriera na liczba rzeczywistych i zespolonych.

%package MA
Summary:	MA - a facility for dealing with masked arrays
Summary(pl):	Modu³ do obs³ugi macierzy niepe³nych
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-numpy-MA <= 24.2

%description MA
Masked arrays are arrays that may have missing or invalid entries.
Module MA provides a work-alike replacement for Numeric that supports
data arrays with masks.

%description MA -l pl
Macierze niepe³ne s± to macierze, którym mo¿e brakowaæ lub mog±
zawieraæ niepoprawne warto¶ci. Modu³ MA zawiera odpowiednie narzêdzia
do operowania na tego typu macierzach.

%package RNG
Summary:	Random Number Generator Object for NumPy
Summary(pl):	Obiekt generatora liczb losowych dla modu³u NumPy
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-numpy-RNG <= 24.2

%description RNG
RNG provides a random number object to Numerical Python.

%description RNG -l pl
Modu³ ten zawiera implementacjê obiektu generatora liczb losowych dla
jêzyka Python.

%prep
%setup -q -n %{module}-%{version}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/%{module}.pth
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%dir %{py_sitedir}/%{module}/Numeric_headers
%{py_sitedir}/%{module}/Numeric_headers/__init__.*
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/*.py

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}

%files FFT
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/FFT
%attr(755,root,root) %{py_sitedir}/%{module}/FFT/*.so
%{py_sitedir}/%{module}/FFT/*.py[co]
%{py_sitedir}/%{module}/FFT/*.py

#%files kinds
#%defattr(644,root,root,755)
#%dir %{py_sitedir}/%{module}/kinds
#%attr(755,root,root) %{py_sitedir}/%{module}/kinds/*.so
#%{py_sitedir}/%{module}/kinds/*.py[co]

%files MA
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/MA
%{py_sitedir}/%{module}/MA/*.py[co]
%{py_sitedir}/%{module}/MA/*.py

#%files Properties
#%defattr(644,root,root,755)
#%dir %{py_sitedir}/%{module}/PropertiedClasses
#%{py_sitedir}/%{module}/PropertiedClasses/*.py[co]

%files RNG
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/RNG
%attr(755,root,root) %{py_sitedir}/%{module}/RNG/*.so
%{py_sitedir}/%{module}/RNG/*.py[co]
%{py_sitedir}/%{module}/RNG/*.py
