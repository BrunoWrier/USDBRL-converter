# USDBRL-converter
A chart made with matplotlib, it's a simple currency converter.

Hello everyone, this is a simple project that i made with python and matplotlib. It convert 1 USD to BRL, shows a graphic/chart and also gives you the porcentage in the period of 3 days.

About the apis:
  I am using a free api to convert the currency in 'real time'. Actually the information may be not precise or kinda outdated (a few minutes perhaps) but it's     totaly the api's fault, and you can change the apis for the api of your choise (mostly you have to pay to use a api like this). Well i think that the             important is that it works and you can change it to improve the eficacy.
   
  Besides the slow api (it updates every 30 secconds, but as i said it can be longer sometimes) the aplication will update (request from the api) every 5000ms or   5 seconds. You can change that as you want on the line "ani = FuncAnimation(figure, data, interval=5000)".
   
   api site: https://docs.awesomeapi.com.br/api-de-moedas

Anyway, it's a simple project and i may change and update things someday, just a small note that the function data is basically the "update" function and it's setting all the informations every 5 seconds by default.

Thanks for checking my code :v
