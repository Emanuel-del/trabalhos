#include <iostream>

int main(int argc, char** argv) {

	// Criar parte das poltronas
	char reserva[10][6] = {
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '},
		{' ', ' ', ' ', ' ', ' ', ' '}
	};

	// Declaração de variáveis
	int fileira = -1, acento = -1;
	char poltrona = ' ';
	char continua = ' ';
	int passagem = 0;

	// Estrutura de do loop
	while (true) {

		// Leitura de variáveis
		printf("\nDigite a fileira (1-10): ");
		scanf("%d", &fileira);
		printf("\nDigite a poltrona [A][B][C][D][E][F]: ");
		scanf(" %c", &poltrona);
		printf("\nQual o tipo de passagem? (1-Executivo, 2-Econômico): ");
		scanf("%d", &passagem);

		// Validação de tipo de passagem
		// Caso executivo, libera todas as poltronas para serem escolhidas
		// Se não, somente da poltrona B a E
		if(passagem == 1) {
			switch(poltrona) {
			case 'A':
				acento = 0;
				break;
			case 'B':
				acento = 1;
				break;
			case 'C':
				acento = 2;
				break;
			case 'D':
				acento = 3;
				break;
			case 'E':
				acento = 4;
				break;
			case 'F':
				acento = 5;
				break;
			default:
				printf("\nPoltrona inválida");
				continue;
			}

			// Verificando se assento já se encontra reservado, caso disponível reservando
			if(reserva[fileira-1][acento] == 'x') {
				printf("\nEsse assento já está reservado. Por favor, escolha outro.");
			} else {
				reserva[fileira-1][acento] = 'x';
			}
		}
		else {
			switch(poltrona) {
			case 'B':
				acento = 1;
				break;
			case 'C':
				acento = 2;
				break;
			case 'D':
				acento = 3;
				break;
			case 'E':
				acento = 4;
				break;
			default:
				printf("\nNão é permitido reservar assentos nas janelas para passagens econômicas.");
				continue;
			}

			// Verificando se assento já se encontra reservado, caso disponível reservando
			if(reserva[fileira-1][acento] == 'x') {
				printf("\nEsse assento já está reservado. Por favor, escolha outro.");
			} else {
				reserva[fileira-1][acento] = 'x';
			}

		}

		// Impressão do mapa de assentos
		printf("\n\t\t[A] [B] [C]\t[D] [E] [F]\n");

		for (int x = 0; x < 10; x++) {

			if (x < 9)	printf("\n\t0%d\t", x + 1);
			else		printf("\n\t%d\t", x + 1);

			for (int y = 0; y < 6; y++) {
				printf("[%c] ", reserva[x][y]);
				if (y == 2) {
					printf("\t");
				}
			}
		}
		printf("\n");

		// Validando se deseja nova reserva
		printf("\nDeseja reservar outra passagem? (s/n): ");
		scanf(" %c", &continua);
		if(continua == 'N' || continua == 'n') {
			printf("\nEncerrando o sistema de reservas...");
			break;
		}

	}

	return 0;
}
