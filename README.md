# MarketPlace

## Requirements
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use
### If you need to run application and database/infrastructure.

1. Clone the repository: `git clone https://github.com/webstore-teamchallenge/backend`

2. Create an `.env` file and add your own data following the structure and path of the `.env_example` file.
3. Use `make app` command to run application and database infrastructure.
4. Use `make migrate` command to apply migration and create all needed db.
5. Use `make createsuperuser` command to create admin user.
6. Use `make app-logs` command to follow the logs in app container.




### Available commands:
* `make app` - up application and database infrastructure
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make storages` - up only storages. you should run your application locally for debugging/developing purposes
* `make storages-logs` - follow the logs in storages containers
* `make storages-down` - down all infrastructure
* `make container-shell` - go to container shell
* `make storages-shell` - go to storages shell
* `make migrate` - apply all made migrations
* `make makemigrations` - make migrations to models
* `make createsuperuser` - create admin user
* `make collectstatic` - collect static


### Data generator:
* `python manage.py data_generator` - use this command to generate data for automatic filling/creation of users and their products/categories.


# Project Overview

## Introduction




## Features

### Core Features
- **User Registration/Authentication**: Integration with Google accounts for easy sign-up and login.
- **Listing Management**: Users can create, view, edit, and delete their listings.
- **Contact Visibility**: Contact details are available exclusively to authenticated users.
- **Listing Details**: Each listing will display images and descriptions of the products.
- **Search and Filtering**: Users can search listings by title and filter by categories such as electronics, clothing, appliances, etc.
- **Sorting**: Listings can be sorted by price and date.
- **Pagination**: To improve the user experience, listings will be divided across multiple pages.
- **Favorites**: Users can save listings to a favorites list for easy access.
- **Recently Viewed Products**: The platform will track and display the last 30 viewed products, showcasing random and unsold items in a "recently viewed" section.
- **Recommendations**: Display product recommendations based on recently viewed categories, with a price variation of +-10%.
- **Comments**: Users can leave comments on listings.
- **User Profiles**: Display a user's history of listings for easy management and review.

### Additional Features
- **Private Messaging**: A chat feature tied to listings for communication between buyers and sellers.
- **Import/Export Listings**: Functionality to import and export listings via Excel files.
- **Notifications**: A system to alert users about activity on their listings.
- **Seller and Buyer Ratings**: Implementation of a rating system for both sellers and buyers (details to be determined).
- **Promoted Products**: Special promotion of products, prioritizing those from categories of recently viewed items.
- **Integration with Delivery Services and Maps**: To enhance the buying and selling process.

## Technical Specifications

### Backend
- **Programming Language**: Python 3.11+.
- **Framework**: Django REST Framework.
- **Authentication**: OAuth 2.0 for Google account integration.
- **Database**: PostgreSQL.
- **Caching**: Redis or similar technology for response time optimization.
- **Hosting**: Scalable hosting solution to be determined.

### Frontend
- **Framework**: React (latest stable version).
- **State Management**: Redux or Context API.
- **Styling**: CSS-in-JS library (e.g., styled-components) or SCSS.
- **Responsiveness**: Implementation of Responsive Web Design.
- **Package Manager**: npm or Yarn.
- **Routing**: React Router for navigation.

### UI/UX Requirements
- **Intuitive Design**: Focus on ease of use with a minimalistic approach.
- **Adaptive Design**: Ensure the platform is fully functional on mobile and tablet devices.
- **Unique Branding**: Distinctive and recognizable design.

### Security
- **HTTPS**: Secure connections.
- **Protection**: Measures against XSS, CSRF, and SQL injections.
- **Access Control**: Implementation of user authentication and authorization rules.
- **Testing**: Unit tests for critical components.

## Testing
- **Automated Testing**: For both backend and frontend components.
- **Manual Testing**: Utilizing tools like Postman for API testing.
- **Load Testing**: To assess scalability and robustness.

## Deployment
- **Dockerization**: Simplify deployment and migration processes.

## Documentation
- **Technical Documentation**: Detailed descriptions of the system architecture, data models, and APIs.
- **Developer and User Guides**: Instructions for both developers and end-users.
- **Regular Updates**: Documentation will be updated with each significant system update.

# Using Git at MarketPlace

- Small & frequent commits
- Aim for linear history: Avoid merge-commits - do fast-forward instead
- NEVER: commit secrets

We follow GitHub flow for branching approach ([Read more](https://docs.github.com/en/get-started/quickstart/github-flow)). In a nutshell:

1. Create a feature branch from `main`
2. Make changes
3. Add tests
4. Add documentation
5. Commit changes & `Push` to `origin`
6. Create a `Pull Request` to `main`
7. Ask for review
![image](https://github.com/ValeriyFromUA/MarketPlace/assets/97425138/7e0e938b-2dc4-4ce2-a0e1-b9678e98d9bc)


Branching scheme (for now, very simple):

|branch|description|
|---|---|
|main|The main branch. Merge feature branches here.|
| 1-fix_some_issue | Feature and fix branches. Include issue number, so that can be tied to a Github issue. |



##  Conventional comments with commits

Examples:

      feat: add ability to login; Closes #4

      feat(de): a scoped feature for German; Closes #4

      fix: login not working; Closes #4

      docs: add documentation for login; Closes #4

      style: fix indentation; Closes #4

      refactor: login; Closes #4

      perf: login; Closes #4

      test: login; Closes #4

      chore: login; Closes #4

      build: login; Closes #4

      ci: login; Closes #4

      revert: login; Closes #4

# UA VERSION:
# Огляд проекту маркетплейсу

## Вступ
Мета цього проекту - розробка платформи маркетплейсу, яка дозволяє користувачам створювати оголошення для купівлі або продажу товарів. Платформа надасть зручний пошук, категоризацію та можливість взаємодії між покупцями та продавцями.

## Особливості

### Основні функції
- **Реєстрація/авторизація**: Інтеграція з Google акаунтами для спрощення процесу входу.
- **Управління оголошеннями**: Користувачі можуть створювати, переглядати, редагувати та видаляти свої оголошення.
- **Видимість контактів**: Контактні дані доступні лише для авторизованих користувачів.
- **Деталі оголошень**: Кожне оголошення відображатиме зображення та опис товарів.
- **Пошук та фільтрація**: Користувачі можуть шукати оголошення за назвою та фільтрувати за категоріями, такими як електроніка, одяг, побутова техніка тощо.
- **Сортування**: Оголошення можна сортувати за ціною та датою.
- **Пагінація**: Для поліпшення користувацького досвіду, оголошення будуть розділені по сторінках.
- **Обране**: Користувачі можуть зберігати оголошення в список обраних для легкого доступу.
- **Нещодавно переглянуті товари**: Платформа відстежуватиме та відображатиме останні 30 переглянутих товарів, показуючи випадкові та непродані товари в розділі "нещодавно переглянуті".
- **Рекомендації**: Відображення рекомендованих товарів на основі категорій нещодавно переглянутих товарів, з варіацією ціни +-10%.
- **Коментарі**: Користувачі можуть залишати коментарі до оголошень.
- **Профіль користувача**: Відображення історії оголошень користувача для легкого управління та огляду.

### Додаткові функції
- **Особистий чат**: Функція чату, пов'язана з оголошеннями для спілкування між покупцями та продавцями.
- **Імпорт/експорт оголошень**: Можливість імпорту та експорту оголошень через Excel файли.
- **Сповіщення**: Система повідомлень для користувачів про активність у їх оголошеннях.
- **Рейтинг продавця та покупця**: Впровадження системи рейтингів для обох сторін (деталі потребують уточнення).
- **Промовані товари**: Особлива промоція товарів, з пріоритетом для товарів із категорій нещодавно переглянутих.
- **Інтеграція з службами доставки та картами**: Для поліпшення процесу купівлі та продажу.

## Технічні специфікації

### Бекенд
- **Мова програмування**: Python 3.11+.
- **Фреймворк**: Django REST Framework.
- **Автентифікація**: OAuth 2.0 для інтеграції з Google акаунтами.
- **База даних**: PostgreSQL.
- **Кешування**: Redis або аналогічна технологія для оптимізації часу відповіді.
- **Хостинг**: Рішення для масштабування відповідно до навантаження.

### Фронтенд
- **Фреймворк**: React (остання стабільна версія).
- **Управління станом**: Redux або Context API.
- **Стилізація**: Бібліотека CSS-in-JS (наприклад, styled-components) або SCSS.
- **Відповідність**: Реалізація адаптивного дизайну.
- **Пакетний менеджер**: npm або Yarn.
- **Маршрутизація**: React Router для навігації.

### Вимоги до UI/UX
- **Інтуїтивний дизайн**: Зосередження на легкості використання з мінімалістичним підходом.
- **Адаптивний дизайн**: Повна функціональність на мобільних та планшетних пристроях.
- **Унікальний брендинг**: Виразний та впізнаваний дизайн.

### Безпека
- **HTTPS**: Захищені з'єднання.
- **Захист**: Заходи проти XSS, CSRF та SQL ін'єкцій.
- **Контроль доступу**: Впровадження правил аутентифікації та авторизації користувачів.
- **Тестування**: Unit-тести для критичних компонентів.

## Тестування
- **Автоматизоване тестування**: Для компонентів бекенду та фронтенду.
- **Ручне тестування**: Використання інструментів на кшталт Postman для тестування API.
- **Навантажувальні тести**: Для оцінки масштабованості та стабільності.

## Розгортання
- **Докеризація**: Спрощення процесу розгортання та міграції.

## Документація
- **Технічна документація**: Детальний опис архітектури системи, моделей дани
