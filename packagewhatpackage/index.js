const jsonData = '{"foo":"bar", "gronk": ["fleebles", "sepulveda"]}'

const pre = document.createElement('pre')
pre.textContent = JSON.stringify(JSON.parse(jsonData), null, 2)

document.body.appendChild(pre)