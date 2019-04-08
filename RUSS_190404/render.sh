jupyter-nbconvert --to slides presentationRuss.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides StackPythonInstall.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides CalculVisu.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides Pydata.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides StatsML.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides ManipulationGeospatiale.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides web.ipynb --SlidesExporter.reveal_scroll=True \
&& jupyter-nbconvert --to slides RetourDiscussion.ipynb --SlidesExporter.reveal_scroll=True \
&& mv presentationRuss.slides.html index.html \
&& rm -rf ~/code/mthh.github.io/RUSS_190404/* \
&& rm -rf ~/code/mthh.github.io/binder/* \
&& cp -r . ~/code/mthh.github.io/RUSS_190404/ \
&& rm ~/code/mthh.github.io/RUSS_190404/RustKernel.ipynb \
&& mv ~/code/mthh.github.io/RUSS_190404/requirements.txt ~/code/mthh.github.io/binder/ \
&& mv ~/code/mthh.github.io/RUSS_190404/runtime.txt ~/code/mthh.github.io/binder/


