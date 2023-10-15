const { Browser } = require("puppeteer");
const loginData = require("./login.json");
const login = async (browserInstance: Promise<Browser | undefined>) => {
  const browser = await browserInstance;
  if (!browser) return;
};
