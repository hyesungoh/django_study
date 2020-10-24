# django_study

### crud4likelion - issue
- 20.07.12 / static css update doesnt working > cmd + shift + r
- 20.07.23 / OperationalError no such table > db.sqlite3 파일 삭제 후 migrate

### dino_history (공아역) - issue
- 20.10.16 / Value Error - invalid literal for int() with base 10, 모델 integerField 값을 수정할 때 발생한 에러. admin으로 생성된 user를 admin page에서 값을 수정했더니 fix됨
- 20.10.24 / Custom Template Filter import error - html 파일에 `{% load problems_num %}`을 {% load 'problems_num' %}으로 작성해서 나타난 오류 ..

### codieboogie - issue
- 20.10.22 / ERROR/MainProcess] consumer: Cannot connect to amqp://guest:**@127.0.0.1:5672//: [Errno 111] Connection refused. redis-server가 켜진 상태에서 celery를 키지 않아사 발생한 오류
