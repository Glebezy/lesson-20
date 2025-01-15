## Проект Mobile автотестов Wikipedia

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Appium" src="images/logo/appium.png"></code>
  <code><img width="5%" title="Browserstack" src="images/logo/browserstack.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

### Что проверяем
* Прохождение онбординга
* Пропуск онбординга
* Навигация по онбордингу 

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/16-glebezy-python-unit20/)

##### При нажатии на "Build with Parameters" открывается форма заполнения параметров
##### после которой происходит сборка тестов и их прохождение, через виртуальную машину в BrowserStack.
![This is an image](images/screenshots/jenkins.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритизации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Behaviors находятся собранные тест кейсы, у которых описаны шаги и приложены аттачи о прохождении теста
![This is an image](images/screenshots/allure_suites.png)

<!-- Appium -->


### <img width="3%" title="Appium" src="images/logo/appium.png"> Скринкаст прохождения тестов используя Appium



https://github.com/user-attachments/assets/bbef3612-7e24-47f2-8c88-b57f35cd5791




<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram-бот приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/tg_bot.png)
