# Projeto-Water
1. Diagrama em blocos:
  ![alt text](https://github.com/AdrianoBusson/Projeto-Water/blob/main/Projeto%20Final%20blocos.jpg?raw=true)

Proposta de monitoramento via IoT da qualidade de água e registro computacional a partir de modelo Machine Learning em blockchain, utilizando Cartesi Machine.

2.	Visão do Projeto

O acesso à água potável é essencial para a saúde, um direito humano básico e um componente de uma política eficaz de proteção da saúde e desenvolvimento a nível nacional, regional e local.
O Brasil ainda apresenta números preocupantes relacionados ao saneamento básico. Milhões de pessoas vivem sem água tratada e sem acesso à coleta de esgoto resultando em doenças que poderiam ser evitadas e que podem levar à morte por contaminação.
Em algumas regiões, foi demonstrado que os investimentos no abastecimento de água e no saneamento podem produzir um benefício econômico líquido, uma vez que as reduções nos efeitos adversos para a saúde e nos custos dos cuidados de saúde superam os custos da realização das intervenções.
A proposta do nosso projeto é desenvolver um sistema IoT para auxiliar no monitoramento da qualidade da água dentro de uma Estação de Tratamento de água (ETA), ou em locais onde a qualidade das águas é fundamental para um determinado uso (especialmente para consumo humano) ou em locais críticos associados ao uso da água. 
Os locais de monitoramento serão equipados de sensores para envio dos dados às equipes de operação facilitando, assim a análise dos dados. Através da coleta de amostras da água, o controle e monitoramento seguirá o método de vigilância permitindo identificar alterações específicas, exigindo ou não a tomada de providências.
O sistema, através de sensores realizará a medição de diversos parâmetros, classificará em tempo real a qualidade da água como potável (própria para o consumo) ou não potável (imprópria para o consumo). 

Parâmetros de medição:

a.	Valor de pH:
O pH é um parâmetro importante na avaliação do equilíbrio ácido-base da água. É também o indicador da condição ácida ou alcalina do estado da água. A OMS recomendou o limite máximo permitido de pH de 6,5 a 8,5. 

b.	Dureza:
A dureza é causada principalmente por sais de cálcio e magnésio. Esses sais são dissolvidos em depósitos geológicos através dos quais a água viaja. O período de tempo que a água fica em contato com o material produtor de dureza ajuda a determinar quanta dureza existe na água bruta. A dureza foi originalmente definida como a capacidade da água de precipitar sabão causada pelo Cálcio e pelo Magnésio.

c.	Sólidos (Total de Sólidos Dissolvidos - TDS):
A água tem a capacidade de dissolver uma ampla gama de minerais ou sais inorgânicos e alguns orgânicos, como potássio, cálcio, sódio, bicarbonatos, cloretos, magnésio, sulfatos, etc. Esses minerais produziam sabor indesejado e cor diluída na aparência da água. Este é o parâmetro importante para o uso da água. A água com alto valor de TDS indica que a água é altamente mineralizada. O limite desejável para TDS é 500 mg/le o limite máximo é 1000 mg/l, prescrito para beber.

d.	Cloraminas:
O cloro e a cloramina são os principais desinfetantes utilizados nos sistemas públicos de água. As cloraminas são mais comumente formadas quando a amônia é adicionada ao cloro para tratar a água potável. Níveis de cloro de até 4 miligramas por litro (mg/L ou 4 partes por milhão (ppm)) são considerados seguros na água potável.

e.	Sulfato:
Os sulfatos são substâncias naturais encontradas em minerais, solo e rochas. Eles estão presentes no ar ambiente, nas águas subterrâneas, nas plantas e nos alimentos. O principal uso comercial do sulfato é na indústria química. A concentração de sulfato na água do mar é de cerca de 2.700 miligramas por litro (mg/L). Varia de 3 a 30 mg/L na maioria das fontes de água doce, embora concentrações muito mais altas (1000 mg/L) sejam encontradas em algumas localizações geográficas.

f.	Condutividade:
A água pura não é um bom condutor de corrente elétrica, mas sim um bom isolante. O aumento na concentração de íons aumenta a condutividade elétrica da água. Geralmente, a quantidade de sólidos dissolvidos na água determina a condutividade elétrica. A condutividade elétrica (CE), na verdade, mede o processo iônico de uma solução que lhe permite transmitir corrente. De acordo com os padrões da OMS, o valor CE não deve exceder 400 μS/cm.

g.	Carbono_orgânico:
O carbono orgânico total (COT) nas águas de origem provém da matéria orgânica natural em decomposição (MON), bem como de fontes sintéticas. TOC é uma medida da quantidade total de carbono em compostos orgânicos em água pura. De acordo com a EPA dos EUA, < 2 mg/L como TOC em água tratada/potável e < 4 mg/Lit em água de origem usada para tratamento.

h.	Trihalometanos:
THMs são produtos químicos que podem ser encontrados na água tratada com cloro. A concentração de THMs na água potável varia de acordo com o nível de matéria orgânica na água, a quantidade de cloro necessária para tratar a água e a temperatura da água que está sendo tratada. Níveis de THM de até 80 ppm são considerados seguros na água potável.

i.	Turbidez:
A turbidez da água depende da quantidade de matéria sólida presente no estado suspenso. É uma medida das propriedades de emissão de luz da água e o teste é usado para indicar a qualidade da descarga de resíduos em relação à matéria coloidal. O valor médio de turbidez obtido para Wondo Genet Campus (0,98 NTU) é inferior ao valor recomendado pela OMS de 5,00 NTU

Para elaboração do trabalho usaremos as seguintes faixas de valores de referência para cada um dos parâmetros. 
Os valores compreendidos entre cada faixa de referência contribuem para que a classificação da água seja ‘Potável”, ou seja aceitável para o consumo humano.
 Se pelo menos um dos parâmetros apresentar valores fora da faixa de referência, a classificação da água passa a ser “não potável” (imprópria para o consumo humano). 
 
