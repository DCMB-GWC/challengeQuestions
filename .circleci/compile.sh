#!/bin/sh

last_compile_commit=$(git log --oneline | grep "Compile PDFs" | head -n 1 | cut -f 1 -d " ")
notebooks_changed=$(git diff --name-only $last_compile_commit HEAD | grep "Keys.*ipynb")
if [ notebooks_changed ]
then
    # install dependences
    echo "*NOTEBOOKS CHANGED*"
    sudo apt-get update
    sudo apt-get install texlive-xetex pandoc
    sudo pip install --upgrade pip
    sudo pip install jupyter

    # compile PDFs
    echo "*COMPILING PDF FILES*"
    for file in $notebooks_changed
    do
        outdir=$(echo $file | sed "s|\(^.*/\).*$|\1|")pdf/
        jupyter nbconvert --to pdf --output-dir=$outdir $file
    done

    # commit new PDFs
    echo "*COMMITTING CHANGES*"
    git config user.email "kellysovacool@gmail.com"
    git config user.name "Kelly Sovacool"
    git add solutions
    git commit -m "Compile PDFs [ci skip]"
    git push
fi
