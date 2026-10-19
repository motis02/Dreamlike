from flask import Flask, render_template
from dream_generator import RandomDreamGenerator

app = Flask(__name__)
dream_generator = RandomDreamGenerator()

@app.route('/')
def index():
    # 打开网页就自动生成一个新梦境
    new_dream = dream_generator.generate_dream()
    dream_text = dream_generator.format_dream_text(new_dream)
    image_prompt = dream_generator.build_image_prompt(new_dream)
    
    return render_template('index.html', 
                           dream_id=new_dream['dream_id'],
                           dream_text=dream_text,
                           image_prompt=image_prompt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)