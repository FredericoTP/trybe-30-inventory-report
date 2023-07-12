from inventory_report.product import Product


def test_product_report() -> None:
    produto_id = "1"
    nome = "Biscoito"
    marca = "Xablau"
    fabricacao = "2022-04-04"
    validade = "2024-08-08"
    serial = "123"
    instrucao = "Ambiente iluminado"

    produto = Product(
        produto_id, nome, marca, fabricacao, validade, serial, instrucao
    )

    report = str(produto)

    assert report == (
        f"The product {produto_id} - {nome} "
        f"with serial number {serial} "
        f"manufactured on {fabricacao} "
        f"by the company {marca} "
        f"valid until {validade} "
        f"must be stored according to the following instructions: "
        f"{instrucao}."
    )
