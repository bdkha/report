const puppeteer = require('puppeteer');

async function startBrowser(){
	let browser;
	try {
	    console.log("Opening the browser......");
	    browser = await puppeteer.launch({
	        headless: false,
	        args: ["--disable-setuid-sandbox"],
	        'ignoreHTTPSErrors': true,
            userDataDir: './browser'
	    });
        return browser;
	} catch (err) {
	    console.log("Could not create a browser instance => : ", err);
	}
}

module.exports = {
	startBrowser
};