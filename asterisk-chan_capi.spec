Summary:	Asterisk ISDN CAPI channel driver
Summary(pl):	Sterownik kana³u CAPI ISDN dla Asteriska
Name:		asterisk-chan_capi
Version:	0.5.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/chan-capi/chan_capi-cm-%{version}.tar.gz
# Source0-md5:	a7a9c0f90395909ee06528f17fc608d2
URL:		http://sourceforge.net/projects/chan-capi/
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
install -d $RPM_BUILD_ROOT/usr/lib/asterisk/modules

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README capi.conf
/usr/lib/asterisk/modules/*
