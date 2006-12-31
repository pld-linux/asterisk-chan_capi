Summary:	Asterisk ISDN CAPI channel driver
Summary(pl):	Sterownik kana³u CAPI ISDN dla Asteriska
Name:		asterisk-chan_capi
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.chan-capi.org/chan-capi/chan_capi-%{version}.tar.gz
# Source0-md5:	2e9809373b30932293295dd9f759d6cb
URL:		http://www.melware.org/ChanCapi
BuildRequires:	asterisk-devel
BuildRequires:	capi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN CAPI Channel driver (chan_capi) for the Asterisk Open Source VOIP
Platform.

%description -l pl
Sterownik kana³u CAPI ISDN (chan_capi) dla Asteriska - platformy VOIP
o otwartych ¼ród³ach.

%prep
%setup -q -n chan_capi-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -D chan_capi.so $RPM_BUILD_ROOT%{_libdir}/asterisk/modules/chan_misdn.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README capi.conf
%{_libdir}/asterisk/modules/*
