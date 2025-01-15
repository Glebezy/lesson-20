from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

search_field = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia'))

main_logo = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark'))