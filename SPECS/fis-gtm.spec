Name:           fis-gtm
Version:        V5.5.000
Release:        1%{?dist}
Summary:        The FIS-GT.M database 

License:        AGPLv3
URL:            http://sourceforge.net/projects/fis-gtm
Source0:        https://github.com/luisibanez/fis-gtm/tarball/57f2d89

BuildRequires:  cmake,gcc
Requires:       

%description
GT.M is a database engine with scalability proven in large real-time
transaction processing systems that have thousands of concurrent
users, individual database file sizes to the Terabyte range (with
virtually unlimited aggregate database sizes).  Yet the light
footprint of GT.M allows it to also scale down for use in small
applications and software appliances (virtual machines).
.
The GT.M data model is hierarchical associative memory (i.e.,
multi-dimensional array) that imposes no restrictions on the data
types of the indexes or content - the application logic can impose
any schema, dictionary or data organization suited to its problem
domain.  (Database engines that do not impose schemas, but which
allow layered application software to impose and use whatever schema
that is appropriate to the application are popularly referred to as
"document oriented", "schemaless" or "schema-free" databases.)
.
GT.M's compiler for the standard M (also known as MUMPS) scripting
language implements full support for ACID (Atomic, Consistent,
Isolated, Durable) transactions, using optimistic concurrency control
and software transactional memory (STM) that resolves the common
mismatch between databases and programming languages. Its unique
ability to create and deploy logical multi-site configurations of
applications provides unrivaled continuity of business in the face of
not just unplanned events, but also planned events, including planned
events that include changes to application logic and schema.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc



%changelog
