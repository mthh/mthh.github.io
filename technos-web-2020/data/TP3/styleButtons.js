var a = document.createElement('div');
a.style.position = 'absolute';
a.style.top = 0;
a.style.right = '15px';
a.innerHTML = `
<p style="padding: 0.5em;border-top-left-radius: 0.25em;border-top-right-radius: 0.25em;background: lightgreen;margin: auto;"onclick="document.getElementsByTagName('link')[0].href='style0.css';"><a href="#">Style 1</a></p>
<p style="padding: 0.5em;background: cornsilk;margin: auto;"onclick="document.getElementsByTagName('link')[0].href='style1.css';"><a href="#">Style 2</a></p>
<p style="padding: 0.5em;border-bottom-left-radius: 0.25em;border-bottom-right-radius: 0.25em;background: #3690df;margin: auto;"onclick="document.getElementsByTagName('link')[0].href='style2.css';"><a href="#">Style 3</a></p>`;
document.body.appendChild(a);
