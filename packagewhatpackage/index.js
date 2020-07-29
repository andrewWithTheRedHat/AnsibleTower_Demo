let data = {}

m.request({url: './data'})
.then(res => {data = res})

m.mount(document.body, {
	view: _v => m('pre', JSON.stringify(data, null, 2))
})