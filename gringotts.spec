%define major 2
%define libname %mklibname gringotts %{major}
%define develname %mklibname gringotts -d
%define staticdevelname %mklibname gringotts -d -s

Name:		libgringotts
Version:	1.2.1
Release:	%mkrel 2
Summary:	A data encapsulation and encryption library
Group:		System/Libraries
License:	GPLv2+
Url:		https://gringotts.berlios.de/
Source0:	http://download.berlios.de/gringotts/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libmcrypt-devel
BuildRequires:	mhash-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	textutils

%description
A small, easy-to-use, thread-safe C library originally developed for 
Gringotts; its purpose is to encapsulate data (generic: ASCII but 
also binary data) in an encrypted and compressed file. It uses strong
encryption algorithms, to ensure the data is as safe as possible, and
allows the user to have the complete control over all the algorithms 
used in the process. 

%package -n %{libname}
Summary:	A data encapsulation and encryption library
Group:		System/Libraries

%description -n %{libname}
A small, easy-to-use, thread-safe C library originally developed for
Gringotts; its purpose is to encapsulate data (generic: ASCII but
also binary data) in an encrypted and compressed file. It uses strong
encryption algorithms, to ensure the data is as safe as possible, and
allows the user to have the complete control over all the algorithms
used in the process.

%package -n %{develname}
Summary:	Development files for the libgringotts library
Group:		Development/C

Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package provides development files for the libgringotts library.

%package -n %{staticdevelname}
Summary:        Static development files for the libgringotts library
Group:          Development/C

Requires:       %{develname} = %{version}-%{release}
Provides:       %{name}-static-devel = %{version}-%{release}

%description -n %{staticdevelname}
This package provides static development files for the libgringotts 
library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove installed doc files
rm -rf %{buildroot}%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO docs/manual.htm
%{_libdir}/%{name}.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/%{name}.a
