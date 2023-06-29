class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[>>Código {self.codigo} Saldo {self.saldo}<<]'
    
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]
print(contas[0])

conta_do_gui.deposita(100)
print(contas[0])

def deposita_para_contas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_contas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

deposita_para_contas(contas)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

deposita(conta_do_gui)

usuarios = [guilherme, daniela]
usuarios.append(('Paulo', 39, 1979))

usuarios[0][0] = 'Guilherme Silveira'

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(2348760)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

for conta in contas:
    print(conta)