
mkdir -p dist/gh-pages/
cd dist/gh-pages/
git clone -b gh-pages https://github.com/Thecarisma/themata.git
cd themata/
cp -r ../../../dist/gendoc/* ./
touch .nojekyll
git config --local user.email "azeezadewale98@gmail.com"
git config --local user.name "travis-ci.org"
git add .; git commit -m "Travis build=${TRAVIS_BUILD_NUMBER}. Update Documentation from Travis CI"
git push -f https://Thecarisma:${GITHUB_TOKEN}@github.com/Thecarisma/themata.git HEAD:gh-pages;
cd ../../../


mkdir -p dist/main/
cd dist/main/
git clone -b main https://github.com/Thecarisma/themata.git
cd themata/
mkdir -p ./docs/
mkdir -p ./themata/
cp -r ../../../docs/* ./docs/
cp -r ../../../themata/* ./themata/
cp -r ../../../.gitattributes ./
cp -r ../../../MANIFEST.in ./
cp -r ../../../README.rst ./
cp -r ../../../setup.cfg ./
cp -r ../../../setup.py ./
git config --local user.email "azeezadewale98@gmail.com"
git config --local user.name "travis-ci.org"
git add .; git commit -m "Automated Push. Travis build=${TRAVIS_BUILD_NUMBER}. Update the main branch"
git push -f https://Thecarisma:${GITHUB_TOKEN}@github.com/Thecarisma/themata.git HEAD:main;
cd ../../