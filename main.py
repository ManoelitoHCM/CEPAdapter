from CEPAdapter import CEPAdapter


def main():

    cep_a_consultar = input("Digite aqui o CEP que deseja consultar: ")

    # Criar uma instância do CEPAdapter
    cep_adapter = CEPAdapter()

    # Consultar o endereço a partir do CEP
    endereco = cep_adapter.get_endereco(cep_a_consultar)

    if endereco:
        print("Endereço obtido:")
        print(f"CEP: {endereco.cep}, Logradouro: {endereco.logradouro}, Bairro: {endereco.bairro}, Localidade: {endereco.localidade}, Estado: {endereco.uf}")
    else:
        print("Falha ao obter o endereço.")


if __name__ == '__main__':
    main()

