const browserObject = require("./browser");
const scraperController = require("./pageController");
const loginData = require("./login.json");
const { reportLinks } = require("./reportLinks");
//Start the browser and create a browser instance

const login = async () => {
  try {
    let browser = await browserObject.startBrowser();

    if (!browser) return;
    const page = await browser.newPage();
    await page.goto(loginData.url);
    const loginKeyInput = await page.$('input[name="loginKey"]');
    const passwordInput = await page.$('input[name="password"]');

    console.log("button", loginKeyInput.isVisible);

    await loginKeyInput.type(loginData.phone);
    await passwordInput.type(loginData.password);

    const submitButton = await page.$(
      ".wyhvVD._1EApiB.hq6WM5.L-VL8Q.cepDQ1._7w24N1"
    );
    await submitButton.click();
  } catch (error) {}
};

const reportLink = async (link) => {};

const report = async () => {
  try {
    let browser = await browserObject.startBrowser();
    if (!browser) return;
    const page = await browser.newPage();
    let i = 0;

    while (i < reportLinks.length * 30) {
      await page.goto(reportLinks[i % reportLinks.length]);

      await page.waitForSelector(".GyD5JO");
      const reporttButton = await page.$(".GyD5JO");
      await reporttButton.click();

      await page.waitForTimeout(2000);
      const divElement = await page.$(".yXGF8k ul li");
      await divElement.click();

      const textAreaReason = await page.$(".yxKRoU textarea");
      await textAreaReason.type("Vũ khí nguy hiểm, hàng cấm");

      const submitButton = await page.$(".dwUHUF button");
      await submitButton.click();

      await page.waitForTimeout(20000);
      i++;
    }
    page.close();
    browser.close();
  } catch (error) {}
};

report();

// Pass the browser instance to the scraper controller
