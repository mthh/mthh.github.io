#!/usr/bin/env python3
with open('index.html', 'r') as f:
  data = f.read()

a = """<section>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="img/ui_data_import.gif"></p>

</div>
</div>
</div></section>"""

b = """<section>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="img/animation_reload.gif"/></p>

</div>
</div>
</div></section>"""

c = """<section>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="img/animation_complete_map.gif"></p>"""

data = data.replace(a, """<section data-background-image="img/ui_data_import.gif">
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
</div>
</div>
</div></section>""")

data = data.replace(b, """<section data-background-image="img/animation_reload.gif">
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
</div>
</div>
</div></section>""")

data = data.replace(c, """<section data=background-image="img/animation_complete_map.gif">
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">""")

with open('index.html', 'w') as f:
    f.write(data)
