import dns.resolver

arquivo = open("/home/phantomglitch/Downloads/wordlist.txt", "r")
subdominios = arquivo.read().splitlines()

res = dns.resolver.Resolver()
alvo = "bancocn.com"
for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." + alvo
		resultado = res.resolve(sub_alvo, "A")
		for ip in resultado:
			print(sub_alvo, "->", ip)
	except:
		pass

	
