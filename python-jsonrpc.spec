%define _svn_release r19
Summary:	JSON-RPC implementation
Summary(pl):	Implementacja prokokołu JSON-RPC
Name:		python-jsonrpc
Version:	0.%{_svn_release}
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	%{name}-%{_svn_release}.tar.gz
# Source0-md5:	e6ad68f8042fab5fe597015b17141555
URL:		http://json-rpc.org/wiki/python-json-rpc
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-jsonrpc is an implementation of JSON-RPC protocol
(http://json-rpc.org/) in Python

%description -l pl
json.py to implementacja protokołu JSON-RPC (http://json.org/) w
Pythonie.

%prep
%setup -q -n jsonrpc-0.01

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/jsonrpc/*.pyc \
    $RPM_BUILD_ROOT%{py_sitescriptdir}/jsonrpc/*.py \
    $RPM_BUILD_ROOT%{py_sitescriptdir}/*.egg-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/jsonrpc/
%{py_sitescriptdir}/jsonrpc/*.pyo
