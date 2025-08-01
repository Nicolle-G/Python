from quart import Quart, request, jsonify
from main import is_palindrome

app = Quart(__name__)

@app.route('/palindrome', methods=['POST'])
async def check_palindrome():
   data = await request.get_json()
   word = data["word"]
   result = is_palindrome(word)
   return jsonify({
    "word": word,
    "is_palindrome": result 
   })   
    
if __name__ == "__main__":
     app.run()  
