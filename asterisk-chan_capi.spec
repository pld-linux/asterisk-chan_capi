# TODO: optflags
Summary:	Asterisk ISDN CAPI channel driver
Summary(pl.UTF-8):	Sterownik kanału CAPI ISDN dla Asteriska
Name:		asterisk-chan_capi
Version:	1.1.5
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.chan-capi.org/chan-capi/chan_capi-%{version}.tar.gz
# Source0-md5:	78ec53c5964fd1bddfd68bf0d13dea9d
URL:		http://www.melware.org/ChanCapi
BuildRequires:	asterisk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN CAPI Channel driver (chan_capi) for the Asterisk Open Source VOIP
Platform.

%description -l pl.UTF-8
Sterownik kanału CAPI ISDN (chan_capi) dla Asteriska - platformy VOIP
o otwartych źródłach.

%prep
%setup -q -n chan_capi-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -D chan_capi.so $RPM_BUILD_ROOT%{_libdir}/asterisk/modules/chan_capi.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README capi.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/*
