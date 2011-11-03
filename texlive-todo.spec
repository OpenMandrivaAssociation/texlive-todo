# revision 17746
# category Package
# catalog-ctan /macros/latex/contrib/todo
# catalog-date 2010-04-01 21:27:08 +0200
# catalog-license lppl1
# catalog-version 2.142
Name:		texlive-todo
Version:	2.142
Release:	1
Summary:	Make a to-do list for a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/todo
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows you to insert "to do" marks in your
document, to make lists of such items, and to cross-reference
to them.

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
%{_texmfdistdir}/tex/latex/todo/todo.sty
%doc %{_texmfdistdir}/doc/latex/todo/README
%doc %{_texmfdistdir}/doc/latex/todo/todo-spl.pdf
%doc %{_texmfdistdir}/doc/latex/todo/todo-spl.tex
%doc %{_texmfdistdir}/doc/latex/todo/todo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/todo/todo.dtx
%doc %{_texmfdistdir}/source/latex/todo/todo.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
