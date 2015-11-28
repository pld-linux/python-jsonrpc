%define subver r19
Summary:	JSON-RPC implementation
Summary(pl.UTF-8):	Implementacja prokokołu JSON-RPC
Name:		python-jsonrpc
Version:	0.%{subver}
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	%{name}-%{subver}.tar.gz
# Source0-md5:	e6ad68f8042fab5fe597015b17141555
URL:		http://json-rpc.org/wiki/python-json-rpc
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-jsonrpc is an implementation of JSON-RPC protocol
(http://json-rpc.org/) in Python.

%description -l pl.UTF-8
python-jsonrpc to implementacja protokołu JSON-RPC (http://json.org/) w
Pythonie.

%prep
%setup -q -n jsonrpc-0.01

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/jsonrpc*
