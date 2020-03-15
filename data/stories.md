## Comprimento
* comprimento
    - utter_comprimento

## Conversao de bases
* converter_bases
   - converter_bases_action

## Inicio de ensino conversao de bases
* inciar_ensino_conversao_bases
    - inicio_ensino_converter_bases_action

## Usuario entendeu
* affirm
    - entendeu_sobre_o_tema
    - slot{"tema_para_ser_explicado": "conversao_bases"}

## Usuario nao entendeu
* deny
  - nao_entendeu_sobre_o_tema
  - slot{"tema_para_ser_explicado": "conversao_bases"}