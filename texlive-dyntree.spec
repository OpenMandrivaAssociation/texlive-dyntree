Name:		texlive-dyntree
Version:	1.0
Release:	1
Summary:	Construct Dynkin tree diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dyntree
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dyntree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dyntree.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dyntree.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is intended for users needing to typeset a Dynkin
Tree Diagram--a group theoretical construct consisting of
cartan coefficients in boxes connected by a series of lines.
Such a diagram is a tool for working out the states and their
weights in terms of the fundamental weights and the simple
roots. The package makes use of the author's coollist package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dyntree/dyntree.sty
%doc %{_texmfdistdir}/doc/latex/dyntree/README
%doc %{_texmfdistdir}/doc/latex/dyntree/dyntree.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dyntree/dyntree.dtx
%doc %{_texmfdistdir}/source/latex/dyntree/dyntree.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
