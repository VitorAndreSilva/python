from sklearn import tree
import requests

#jogos = [[1, 7, 8], [0, 6, 4], [1, 9, 10], [0, 9, 9], [0, 6.5, 7], [1, 8, 7], [0, 9, 10], [0, 8, 4], [1, 9, 9], [0, 7, 7], [0, 6, 10.5], [1, 8, 8], [0, 8, 10], [1, 7, 11], [1, 7, 7], [0, 9, 9], [0, 9, 1.5]]
#pontos = [1, 3, 3, 1, 3, 1, 3, 3, 3, 1, 1, 0, 3, 3, 3, 1, 0]
#resultados = [[2, 2], [0, 3], [3, 2], [0, 0], [1, 2], [0, 0], [0, 1], [0, 1], [3, 1], [1, 1], [0, 0], [0, 2], [2, 0], [1, 0], [1, 0], [0, 0], [3, 2]]
#cartoes = [2, 1, 4, 5, 3, 2, 4, 7, 3, 5, 6, 4, 10, 6, 4, 2, 2]

games = ['https://www.sofascore.com/api/v1/event/13014050/statistics', 'https://www.sofascore.com/api/v1/event/12117277/statistics', 'https://www.sofascore.com/api/v1/event/12117267/statistics', 'https://www.sofascore.com/api/v1/event/12903989/statistics']

headers = { #simulando navegador
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
}
for url in games:
  response = requests.get(url, headers=headers) #pegando requisições com url e com o headers
  data = response.json()

  all_data = [] #todas as informaçoes requisitadas

  for match_stat in data['statistics']: #pegue as estatisticas
    period = match_stat['period'] #tempo de jogo

    for group in match_stat['groups']: #grupos de informações coletadas
        group_name = group['groupName']

        for item in group['statisticsItems']: #itens de estatísticas do jogo
          stat_name = item.get('name') #nomes dos itens
          home_value = item.get('home') #time da casa
          away_value = item.get('away') #time de fora

          all_data.append({
              'Tempo': period,
              'Análise': group_name,
              'Estatística': stat_name,
              'Flamengo': home_value,
              'Adversário': away_value })

claudinha = tree.DecisionTreeClassifier()
claudinha = claudinha.fit(jogos, pontos)

local, nivel, titulares = input("Digite o local (1 para casa e 0 para fora) e o nível (de 0 a 10) do próximo jogo e quantos titulares se esperam jogar: ").split()

predict = claudinha.predict([[local, nivel, titulares]])
claudinha = claudinha.fit(jogos, resultados)
result = claudinha.predict([[local, nivel, titulares]])

if predict == 1:
  print("seu time empatará o próximo jogo por", result)
elif predict == 3:
  print("seu time vencerá o próximo jogo por", result)
else:
  print("Seu time perderá o próximo jogo por", result)

cartao = input("Quer saber quantos cartões acontecerão neste jogo? ")

if "sim" in cartao or "quero" in cartao:
  #claudinha = tree.DecisionTreeClassifier()
  claudinha = claudinha.fit(jogos, cartoes)
  predict = claudinha.predict([[local, nivel, titulares]])
  print("Haverá", predict, "cartões neste jogo")
else:
  print("Ok! SRN!")
