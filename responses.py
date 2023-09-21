import genshinstats as gs
import bot




def handle_response(message: str, user_info_list) -> str:
    if message.startswith("$resin "):
        _, user_name = message.split(" ", 1)  
        user_name = user_name.lower()
        for user_info in user_info_list:
            if user_name == user_info["name"].lower():
                uid = user_info["uid"]
                gs.set_cookie(ltuid=user_info["ltuid"], ltoken=user_info["ltoken"])  
                notes = gs.get_notes(uid)
                
                current_resin = notes['resin']
                time_until_full = (160 - current_resin) * 8  

                hours, minutes = divmod(time_until_full, 60)
                
                response = f"Current resin for {user_info['name']}: {notes['resin']}/{notes['max_resin']}\n"
                response += f"Current realm currency: {notes['realm_currency']}/{notes['max_realm_currency']}\n"
                response += f"Resin will be full in approximately {hours} hours {minutes} minutes."
                return response
        
        return f"User '{user_name}' not found."
    
  
    return "Invalid command. Try again."