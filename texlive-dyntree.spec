%global tl_name dyntree
%global tl_revision 67016

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Construct Dynkin tree diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dyntree
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dyntree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dyntree.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dyntree.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is intended for users needing to typeset a Dynkin Tree
Diagram--a group theoretical construct consisting of cartan coefficients
in boxes connected by a series of lines. Such a diagram is a tool for
working out the states and their weights in terms of the fundamental
weights and the simple roots. The package makes use of the author's
coollist package.

