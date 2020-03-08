## Comprimento
* comprimento
    - utter_comprimento

## Entender alguma coisa

* explicar_sobre_algum_tema{tema_para_ser_explicado:'grafos'}
	slot{tema_para_ser_explicado:'grafos'}
    - explicando_algo
		- augmentation

## Fluxo de conversa sobre algum tema

* comprimento
    - utter_comprimento
* explicar_sobre_algum_tema{tema_para_ser_explicado:'grafos'}
	slot{tema_para_ser_explicado:'grafos'}
    - explicando_algo
> verifica_se_entendeu

## Conversao de bases
* converter_bases
   - converter_bases_action

## Entendeu sobre o tema
> verifica_se_entendeu
* affirm
  - entendeu_sobre_o_tema

## Nao entendeu sobre o tema
> verifica_se_entendeu
* deny
  - nao_entendeu_sobre_o_tema

## Operação matemática
* operacao_matematica
   - operacao_matematica_action

## Inicio de ensino conversao de bases
* inciar_ensino_conversao_bases
   - inicio_ensino_converter_bases_action
