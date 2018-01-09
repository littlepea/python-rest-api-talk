git commit -a -m "update slides"

git checkout -B gh-pages
jupyter-nbconvert --to slides talk.ipynb
mv talk.slides.html index.html
git add index.html
git commit -a -m "update pages"
git pull origin gh-pages && git push origin gh-pages

git checkout master
rm -rf index.html
git pull origin master && git push origin master