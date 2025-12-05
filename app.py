from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World. I am trying to publish my siteweb on render.com"

if __name__ == '__main__':
    # هاد السطر كيعني أن التطبيق غيخدم غير فالبيسي ديالك للتجربة
    # Render ما كيخدمش بهاد السطر، هو كيستعمل Gunicorn
    app.run(host='0.0.0.0', port=5000, debug=True)
