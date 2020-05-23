## cumprimento
* cumprimento
    - utter_cumprimento

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

## Generated Story -4719567070127116474
* cumprimento
    - utter_cumprimento
* inciar_ensino_conversao_bases
    - inicio_ensino_converter_bases_action
    - slot{"tema_para_ser_explicado": "conversao_bases"}

## Generated Story 7384271428355971255
* cumprimento
    - utter_cumprimento
* inciar_ensino_conversao_bases
    - inicio_ensino_converter_bases_action
    - slot{"tema_para_ser_explicado": "conversao_bases"}
* stop
    - rewind
* stop
