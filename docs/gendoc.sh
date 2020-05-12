
cd ../
OUTPUT_FOLDER=$PWD/dist/gh-pages/
cd docs/
declare -a THEMES=("hackish", "milkish", "fandango", "clear", "fluid", "garri", "water", "sugar")
if [[ -d $OUTPUT_FOLDER ]]; then 
    rm -R $OUTPUT_FOLDER
fi
mkdir -p $OUTPUT_FOLDER

sphinx-build -b html -d build/doctrees ./ build/html
mv build/html/* $OUTPUT_FOLDER

for i in "${THEMES[@]}"
do
    echo "$PWD/$i"
    ls
    # sphinx-build -b html -d build/doctrees ./ build/html
    # mv build/html/* $OUTPUT_FOLDER
    cd ../
done
