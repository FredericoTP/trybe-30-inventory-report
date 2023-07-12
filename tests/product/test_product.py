from inventory_report.product import Product


def test_create_product() -> None:
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

    assert produto.id == produto_id
    assert produto.product_name == nome
    assert produto.company_name == marca
    assert produto.manufacturing_date == fabricacao
    assert produto.expiration_date == validade
    assert produto.serial_number == serial
    assert produto.storage_instructions == instrucao
