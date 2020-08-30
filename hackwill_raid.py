import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



vk_session = vk_api.VkApi(token='5f548714cd1b9435990bd9c60ac41884e731be04888e03fef540506cbd178b7162c22b93abce5b012b9fd') #токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,198326143) #цифровой id вашей группы
def main():

	keyboard1 = VkKeyboard(one_time=False) # False - клавиатура после нажатия не будет закрываться. True - будет.

	keyboard1.add_button('HhH vto.pe', color=VkKeyboardColor.POSITIVE)	
	
	keyboard1.add_button('DdD vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	keyboard1.add_line() 
	keyboard1.add_button('HhH vto.pe', color=VkKeyboardColor.POSITIVE)	
	
	keyboard1.add_button('DdD vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	keyboard1.add_line() 
	keyboard1.add_button('HhH vto.pe', color=VkKeyboardColor.NEGATIVE)	
	
	keyboard1.add_button('DdD vto.pe', color=VkKeyboardColor.NEGATIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.NEGATIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.NEGATIVE)			

	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("успешно")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="Рейд",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('') 

if __name__ == '__main__':
	main()