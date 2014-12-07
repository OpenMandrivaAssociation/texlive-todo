# revision 17746
# category Package
# catalog-ctan /macros/latex/contrib/todo
# catalog-date 2010-04-01 21:27:08 +0200
# catalog-license lppl1
# catalog-version 2.142
Name:		texlive-todo
Version:	2.142
Release:	9
Summary:	Make a to-do list for a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/todo
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/todo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to insert "to do" marks in your
document, to make lists of such items, and to cross-reference
to them.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.142-2
+ Revision: 757003
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.142-1
+ Revision: 719774
- texlive-todo
- texlive-todo
- texlive-todo

