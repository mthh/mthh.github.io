jupyter-nbconvert --to slides presentationRuss.ipynb --SlidesExported.reveal_scroll=True \
&& jupyter-nbconvert --to slides StackPythonInstall.ipynb --SlidesExported.reveal_scroll=True \
&& jupyter-nbconvert --to slides CalculVisu.ipynb --SlidesExported.reveal_scroll=True \
&& jupyter-nbconvert --to slides Pydata.ipynb --SlidesExported.reveal_scroll=True \
&& jupyter-nbconvert --to slides StatsML.ipynb --SlidesExported.reveal_scroll=True \
&& jupyter-nbconvert --to slides web.ipynb --SlidesExported.reveal_scroll=True \
&& jupyter-nbconvert --to slides RetourDiscussion.ipynb --SlidesExported.reveal_scroll=True \
&& mv presentationRuss.slides.html index.html
