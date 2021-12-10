from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/inquiry")
def inquiry_page():
    mock_data = [{
      "id": 0,
      "title": "나는 0번째 질문, 존재하지않지",
      "name": "김상훈",
      "content": "넌 나를 볼 수 없다",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-04",
      "phone": "010-1234-5678",
      "replied": True
    },{
      "id": 1,
      "title": "커버 색깔 추가해주심 안되나요?",
      "name": "김상일",
      "content": "핑크색이랑 버건디색이 있으면 좋을것 같아요 ㅠ",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-05",
      "phone": "010-1234-5678",
      "replied": True
    },{
      "id": 2,
      "title": "두번째 질문입니다만?",
      "name": "정율리",
      "content": "두번쨰 질문의 내용입니다만",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-06",
      "phone": "010-1234-5678",
      "replied": True
    },{
      "id": 3,
      "title": "시집 크기는 못정하나요?",
      "name": "김상삼",
      "content": "더 작은사이즈로 인쇄하고 싶은데요",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-07",
      "phone": "010-1234-5678",
      "replied": False
    },{
      "id": 4,
      "title": "네번째엔 무슨 질문을 해볼까요?",
      "name": "정율삼",
      "content": "그것이 미스테리",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-08",
      "phone": "010-1234-5678",
      "replied": False
    },{
      "id": 5,
      "title": "폰트가 조금 더 다양했으면 좋겠네요",
      "name": "김상사",
      "content": "더 추가하실 계획은 없나요?",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-09",
      "phone": "010-1234-5678",
      "replied": False
    }]

    return  render_template('inquiry.html',inquiries=mock_data)

@app.route("/inquiry/<inquiry_id>")
def page(inquiry_id):
    mock_data = [{
      "id": 0,
      "title": "나는 0번째 질문, 존재하지않지",
      "name": "김상훈",
      "content": "넌 나를 볼 수 없다",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-04",
      "phone": "010-1234-5678",
      "replied": True
    },{
      "id": 1,
      "title": "커버 색깔 추가해주심 안되나요?",
      "name": "김상일",
      "content": "핑크색이랑 버건디색이 있으면 좋을것 같아요 ㅠ",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-05",
      "phone": "010-1234-5678",
      "replied": True
    },{
      "id": 2,
      "title": "두번째 질문입니다만?",
      "name": "정율리",
      "content": "두번쨰 질문의 내용입니다만",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-06",
      "phone": "010-1234-5678",
      "replied": True
    },{
      "id": 3,
      "title": "시집 크기는 못정하나요?",
      "name": "김상삼",
      "content": "더 작은사이즈로 인쇄하고 싶은데요",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-07",
      "phone": "010-1234-5678",
      "replied": False
    },{
      "id": 4,
      "title": "네번째엔 무슨 질문을 해볼까요?",
      "name": "정율삼",
      "content": "그것이 미스테리",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-08",
      "phone": "010-1234-5678",
      "replied": False
    },{
      "id": 5,
      "title": "폰트가 조금 더 다양했으면 좋겠네요",
      "name": "김상사",
      "content": "더 추가하실 계획은 없나요?",
      "email": "sanghunkim.nz@gmail.com",
      "date": "2021-12-09",
      "phone": "010-1234-5678",
      "replied": False
    }]

    return render_template('inquiry_reply.html', inquiry_example = mock_data[int(inquiry_id)]);

@app.route("/order")
def order_page():
    mock_order_data = [
      {
        "id": 1,
        "name": "김상훈",
        "email": "sanghunkim.nz@gmail.com",
        "phone": "010-1234-5678",
        "date": "2021-12-05",
        "status": "배송완료"
      },{
        "id": 2,
        "name": "김상훈",
        "email": "sanghunkim.nz@gmail.com",
        "phone": "010-1234-5678",
        "date": "2021-12-06",
        "status": "배송완료"
      },{
        "id": 3,
        "name": "김상훈",
        "email": "sanghunkim.nz@gmail.com",
        "phone": "010-1234-5678",
        "date": "2021-12-09",
        "status": "배송중"
      },{
        "id": 4,
        "name": "김상훈",
        "email": "sanghunkim.nz@gmail.com",
        "phone": "010-1234-5678",
        "date": "2021-12-09",
        "status": "배송준비"
      },{
        "id": 5,
        "name": "김상훈",
        "email": "sanghunkim.nz@gmail.com",
        "phone": "010-1234-5678",
        "date": "2021-12-09",
        "status": "입금완료"
      },{
        "id": 5,
        "name": "김상훈",
        "email": "sanghunkim.nz@gmail.com",
        "phone": "010-1234-5678",
        "date": "2021-12-09",
        "status": "입금대기"
      }
    ]
    return render_template('order.html', orders = mock_order_data)