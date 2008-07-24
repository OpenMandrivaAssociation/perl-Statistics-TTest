%define real_name Statistics-TTest
%define	name perl-%{real_name}
%define	version 1.1.0
%define	release %mkrel 4

Summary:	Statistics::TTest - Perl module to perform T-test on 2 independent samples
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Statistics-Descriptive >= 2.6
BuildRequires:	perl-Statistics-Distributions >= 0.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the Statistical T-Test module to compare 2 independent
samples. It takes 2 array of point measures, compute the confidence
intervals using the PointEstimation module (which is also included in
this package) and use the T-statistic to test the null hypothesis. If
the null hypothesis is rejected, the difference will be given as the
lower_clm and upper_clm of the TTest object. 

%prep
%setup -q -n %{real_name}-%{version} 

# perl path hack
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Statistics/*.pm
%{_mandir}/man3/*

