%define modname	Statistics-TTest
%define	modver	1.1.0

Summary:	Perl module to perform T-test on 2 independent samples
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Statistics/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Statistics::Descriptive) >= 2.60.0
BuildRequires:	perl(Statistics::Distributions) >= 0.70.0

%description
This is the Statistical T-Test module to compare 2 independent
samples. It takes 2 array of point measures, compute the confidence
intervals using the PointEstimation module (which is also included in
this package) and use the T-statistic to test the null hypothesis. If
the null hypothesis is rejected, the difference will be given as the
lower_clm and upper_clm of the TTest object. 

%prep
%setup -qn %{modname}-%{modver}

# perl path hack
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Statistics/*.pm
%{_mandir}/man3/*

