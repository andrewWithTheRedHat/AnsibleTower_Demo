const fs = require('fs')
const express = require('express')
const app = express()
const port = '8000'

app.get('/', (req, res) => { res.sendFile(`${ __dirname }/index.html`) })
app.get('/index.js', (req, res) => { res.sendFile(`${ __dirname }/index.js`) })
app.get('/styles.css', (req, res) => { res.sendFile(`${ __dirname }/styles.css`) })
app.get('/data', (req, res) => { 
	const data = fs.readFileSync(`${ __dirname }/bat-data.json`, 'utf8')
	res.send(data)
})


app.listen(port, () => {
	console.log(`Server listening on port ${port}`)	
})
