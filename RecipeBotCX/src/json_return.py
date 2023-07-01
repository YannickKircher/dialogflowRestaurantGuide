def rich_text(texts:list,content_type="chips"):
    return {
            "richContent": [
                [
                    {
                        "options": [{"text": text} for text in texts],
                        "type": content_type
                    }
                ]
            ]
        }


def json_recipe_data(recipe_id,recipe_name,ingredients,directions):
  
  lines = [recipe_name]+["\n".join(["<b>Ingredients:</b>"]+ingredients)]+["\n".join(["<b>Directions:</b>"]+directions)]
  
  return {
   "fulfillment_response": {
     "messages": [
       {
         "text": {
           "text": [line]
         }
       } for line in lines 
     ]
   },
   "sessionInfo": {
     "parameters": {
          "recipe_id": recipe_id
     }
   }
 }


def test_text2(recipe_id,recipe_name,ingredients):
    return {
   "fulfillment_response": {
     "messages": [
       {
         "text": {
           "text": "\n".join([recipe_name]+ingredients)
         }
       } 
     ]
   },
   "sessionInfo": {
     "parameters": {
          "recipe_id": recipe_id
     }
   }
 }