jupyter-nbconvert --to slides presentationRuss.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides StackPythonInstall.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides CalculVisu.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides Pydata.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides StatsML.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides web.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides RetourDiscussion.ipynb --SlidesExporter.reveal_scroll=True \
&& mv presentationRuss.slides.html index.html
