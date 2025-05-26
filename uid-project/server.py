#Bradford Fowler bf2525
#Bryce Washington brw2135
#Rayan Hayle rah2236
from flask import Flask, render_template, request, jsonify, abort
from datetime import datetime

app = Flask(__name__)


lesson_slides = [
    {
        "id": 0, 
        "title": "What Is the Bench Press?", 
        "image": ["muscle_diagram.png"],
        "info": """
            <p>The bench press is a compound exercise that targets the chest (pectorals), shoulders (deltoids), and triceps. It’s one of the “big three” powerlifting movements and a popular choice for building upper body mass and strength.</p>
            <p>When done with proper form, it’s a highly effective and safe lift. However, poor technique can increase the risk of shoulder, wrist, or lower back injuries—especially under heavy loads.</p>
        """, 
        "prev_lesson": -1,
        "next_lesson": 1,
    },
    {
        "id": 1, 
        "title": "Setup + Equipment", 
        "image": ["bench_equipment.jpg"],
        "info": """
            <p>Before you even lie down, setting up your environment correctly ensures safety and consistency. Here’s what to check:</p>

            <h5>Bench & Rack</h5>
            <ul>
                <li>Use a flat bench with a stable base—no wobble!</li>
                <li>Rack height should let you unrack without overextending your shoulders</li>
            </ul>

            <h5>Barbell</h5>
            <ul>
                <li>Standard Olympic bar (45 lbs) with knurling to help grip</li>
                <li>Make sure the bar is centered before loading weight</li>
            </ul>

            <h5>Weights & Safety</h5>
            <ul>
                <li>Load plates evenly and use collars to secure them</li>
                <li>If lifting heavy: use safety pins, spotter arms, or have a spotter</li>
            </ul>
        """, 
        "prev_lesson": 0,
        "next_lesson": 2,
    },
    {
        "id": 2, 
        "title": "Starting Position", 
        "image": ["bench_setup.jpg"],
        "info": """
            <p>Before unracking the bar, your body should be in a powerful, stable position. The bench press isn’t just about pushing weight—it’s about creating full-body tension to move efficiently and protect your joints.</p>

            <h5>Checklist for the starting position:</h5>
            <ul>
                <li><strong>Feet:</strong> Flat on the floor and planted—don’t move them!</li>
                <li><strong>Back:</strong> Slight arch with shoulder blades squeezed together and pressed into the bench</li>
                <li><strong>Grip:</strong> Hands just outside shoulder width; bar rests in the heel of your palm, not fingers</li>
                <li><strong>Eyes:</strong> Directly under the barbell</li>
                <li><strong>Wrists:</strong> Straight, stacked over elbows</li>
                <li><strong>Core & Glutes:</strong> Engaged and tight throughout the set</li>
            </ul>
        """, 
        "prev_lesson": 1,
        "next_lesson": 3,
    },
        {
        "id": 3, 
        "title": "Starting Position: Diagram", 
        "image": ["starting_position_diagram.png"],
        "prev_lesson": 2,
        "next_lesson": 4,
    },
    {
        "id": 4, 
        "title": "The Descent", 
        "image": ["shoulder_position.gif", "bar_path.gif"],
        "info": """
            <p>The descent is where many lifters lose tension or form. A good descent sets up a strong press and keeps your joints protected.</p>

            <h5>Here’s how to do it right:</h5>
            <ul>
                <li><strong>Unlock the Bar:</strong> Use your lats to pull the bar out of the rack—not your shoulders.</li>
                <li><strong>Bar Path:</strong> Lower in a slight arc from over your shoulders down to mid-chest.</li>
                <li><strong>Touch Point:</strong> Gently tap the bar on your mid-to-lower chest—no bouncing</li>
            </ul>
        """, 
        "prev_lesson": 3,
        "next_lesson": 5,
    },
    {
        "id": 5, 
        "title": "The Descent: Tip #1", 
        "image": ["elbow_angle.gif"],
        "info": """
            <h5>Tip #1</h5>
            <br>
            <p><strong>Elbows:</strong> Tucked at roughly a 75° angle from your torso—not flared or too close.</p>
        """, 
        "prev_lesson": 4,
        "next_lesson": 6,
    },
    {
        "id": 6, 
        "title": "The Descent: Tip #2", 
        "image": ["wrist_angle.gif"],
        "info": """
            <h5>Tip #2</h5>
            <br>
            <p><strong>Wrists & Forearms:</strong> Stay vertical under the bar for maximum control.</p>
        """, 
        "prev_lesson": 5,
        "next_lesson": 7,
    },
    {
        "id": 7, 
        "title": "The Press", 
        "image": ["press.gif"],
        "info": """
        <p>Once the bar has touched your chest, it’s time to press it back to the starting position. This is where leg drive, bar path, and total-body tension all come together.</p>

        <h5>Key points for the press:</h5>
        <ul>
            <li><strong>Press Up & Slightly Back:</strong> Follow the same arc as the descent—from chest to over shoulders</li>
            <li><strong>Drive Through Your Feet:</strong> Use leg drive to stabilize and generate force without lifting your heels</li>
            <li><strong>Keep Elbows Under the Bar:</strong> Maintain stacked alignment—this ensures power and shoulder safety</li>
            <li><strong>Lockout With Control:</strong> Fully extend your arms, but don’t overextend or shrug</li>
        </ul>
        """, 
        "prev_lesson": 6,
        "next_lesson": 8,
    },
    {
        "id": 8, 
        "title": "Common Mistakes", 
        "info": """
            <table class="table table-bordered table-striped">
                <thead>
                    <tr>
                        <th style="text-align: center;">❌ Mistake</th>
                        <th style="text-align: center;">✅ How to Fix It</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Elbows flared out</td>
                        <td>Keep elbows tucked at ~75° from torso to reduce shoulder strain</td>
                    </tr>
                    <tr>
                        <td>Feet off the ground</td>
                        <td>Plant your feet flat and use leg drive for stability and power</td>
                    </tr>
                    <tr>
                        <td>Bouncing bar off chest</td>
                        <td>Lower with control; tap the chest lightly—don’t rely on momentum</td>
                    </tr>
                    <tr>
                        <td>Wrists bent back</td>
                        <td>Keep wrists straight with the bar in the heel of your palm</td>
                    </tr>
                    <tr>
                        <td>Loose upper back (no scapular retraction)</td>
                        <td>Squeeze shoulder blades together and maintain tension before unracking</td>
                    </tr>
                </tbody>
            </table>
        """, 
        "prev_lesson": 7,
        "next_lesson": 9,
    },
    {
        "id": 9, 
        "title": "Injury Prevention", 
        "image": ["injury_prevention.gif"],
        "info": """
            <ul>
                <li><strong>Warm Up Thoroughly:</strong> Use light weights or resistance bands to get blood flowing to the chest, shoulders, and triceps</li>
                <li><strong>Use Proper Form Every Rep:</strong> Focus on setup, bar path, and control—especially when you’re tired</li>
                <li><strong>Progress Gradually:</strong> Increase weight slowly over time; don’t chase PRs without consistent training</li>
                <li><strong>Use a Spotter or Safety Pins:</strong> Always have a backup plan in case a rep fails</li>
                <li><strong>Check Equipment:</strong> Make sure the bench is stable, the rack is even, and collars are on tight</li>
                <li><strong>Recover Between Sessions:</strong> Allow at least 48 hours of rest for your pressing muscles before hitting heavy bench again</li>
            </ul>
        """, 
        "prev_lesson": 8,
        "next_lesson": 10,
    },

    {
    "id": 10,
    "title": "You're Almost There!",
    "image": ["quiz-homepage.jpg"],
    "info": """
        <div class="text-center">
            <p class="fs-4">You've made it through the entire lesson series — great job!</p>
            <p class="fs-5">Take a deep breath, get focused, and when you're ready...</p>
            <h3 class="mt-3 fw-bold text-success">💪 It's Quiz Time!</h3>
            <p class="mt-3">This short quiz will check how well you’ve understood the material. Don’t worry — you’ve got this.</p>
        </div>
    """,
    "prev_lesson": 9,
    "next_lesson": 11
},
]

quiz_slides = [
    {
        "id": 0,
        "title": "Myth or Fact: 'You should always bench with a completely flat back.",
        "image": "/static/images/flatback.jpg",
        "choices": {
            "A": "Myth",
            "B": "Fact"
        },
        "correct_answer": "A",
        "refrence_id": 2,
        "prev_lesson": -1,
        "next_lesson": 1,
       
    },
    {
        "id": 1,
        "title": "Myth or Fact: 'Touching the bar to your chest is required in most powerlifting competitions.'",
        "image": "/static/images/bartochest.jpg",
        "choices": {
            "A": "Myth",
            "B": "Fact"
        },
        "correct_answer": "B",
        "refrence_id": 4,
        "prev_lesson": 0,
        "next_lesson": 2,
    },
    {
        "id": 2,
        "title": "Myth or Fact: 'Wider grip means more chest activation and is always better.'",
        "image": "/static/images/widergrip.jpg",
        "choices": {
            "A": "Myth",
            "B": "Fact"
        },
        "correct_answer": "A",
        "refrence_id": 2,
        "prev_lesson": 1,
        "next_lesson": 3
    },
    {
        "id": 3,
        "title": "Myth or Fact: 'Using leg drive helps stabilize and add power to the lift.'",
        "image":  "/static/images/legdrive.jpg",
        "choices": {
            "A": "Myth",
            "B": "Fact"
        },
        "correct_answer": "B",
        "refrence_id": 7,
        "prev_lesson": 2,
        "next_lesson": 4
    },

    {
        "id": 4,
        "title": "Which of these shows proper bench form?",
        "image": "",  #quiz 2b
        "choices": {
            "A": "/static/images/quiz2a.jpg",
            "B": "/static/images/quiz2b.jpg",
            "C": "/static/images/quiz2c.jpg"
        },
        "correct_answer": "C",
        "refrence_id": 2,
        "prev_lesson": 3,
        "next_lesson": 5
    },

    {
        "id": 5,
        "title": "Which of these bar paths represents safe and effective bench press technique?",
        "image": "",  # quiz3b
        "choices": {
            "A": "/static/images/quiz3a.jpg",
            "B": "/static/images/quiz3b.jpg",
            "C": "/static/images/quiz3c.jpg"
        },
        "correct_answer": "B",
        "refrence_id": 4,
        "prev_lesson": 4,
        "next_lesson": 6,
        
    },
    
        {
        "id": 6,
        "title": "Watch the video above. What mistake is the lifter making?",
        "video": "/static/images/bench_press_video.mp4",
        "choices": {
            "A": "Bar is lowered too low on the chest",
            "B": "Elbows are tucked too much",
            "C": "Elbows are flared out too wide",
            "D": "Grip is too narrow"
        },
        "correct_answer": "C",
        "refrence_id": 5,
        "prev_lesson": 5,
        "next_lesson": 7
    },

]

# This will change dynamically. As the user goes back and fixes a question, it will update.
results=[]
time_store=[]
lesson_pairs = [(lesson["id"], lesson["title"]) for lesson in lesson_slides]

@app.route('/')
def homePage():
    return render_template('home.html', lesson_pairs=lesson_pairs)

@app.route('/learn/<int:id>')
def learn(id):
    # Validate lesson exists
    current_time = datetime.now()
    if id < 0:
        abort(404)
    elif id==len(lesson_slides):
        time_store.append({ "id": id, "time": current_time})
        question = quiz_slides[0]
        print(time_store)
        return render_template('quiz.html', lesson_pairs=lesson_pairs, question=question, id=id, totalSlides=len(quiz_slides))
    lesson=lesson_slides[id]
    time_store.append({ "id": id, "time": current_time})
    print(time_store)
    return render_template('learning.html', lesson_pairs=lesson_pairs, lesson=lesson, id=id, totalSlides=len(lesson_slides))


@app.route('/quiz/<int:id>')
def quiz(id):
    
    if id < 0:
        abort(404)
    
    elif id == len(quiz_slides):
        correct_count = sum(1 for entry in results if entry['correct'] == 1)
        total_count = len(results)
        print(results)
        return render_template('quizresults.html', lesson_pairs=lesson_pairs, quiz_slides=quiz_slides, results=results, correct=correct_count, total=total_count)
    
    question = quiz_slides[id]
    return render_template('quiz.html', lesson_pairs=lesson_pairs, question=question, id=id, totalSlides=len(quiz_slides))





@app.route('/submit/answer', methods=['POST'])
def api_data():
    data = request.get_json()
    print("Received data:", data)  # TEMP: Helps debug any incoming issues

    correct = int(data['correct'])
    choice = data['choice']
    id = int(data['id'])

    # Update or insert into results
    for entry in results:
        if entry['id'] == id:
            entry['correct'] = correct
            entry['choice'] = choice
            break
    else:
        results.append({
            "id": id,
            "choice": choice,
            "correct": correct
        })

    print("Updated results list:", results)  # TEMP: See what's stored
    return '', 204



# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5001)