//Calculadora

#include <stdio.h>

int main(void)
{

	int a, b, op;
	float r;

	printf("Digite dois numeros inteiros e apos isso escolha uma operacao: \n 1 - adicao \n 2 - subtracao \n 3 - multiplicacao \n 4 - divisao inteira\n");
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &op);

	switch (op)
	{
		case 1:
		r = a+b;
		printf("A soma dos numeros digitados é %0.3f \n", r);
		break;

		case 2:
		r = a-b;
		printf("A subtracao dos numeros digitados é %0.3f \n", r);
		break;
	
		case 3:
		r = a*b;
		printf("A multiplicacao dos numeros digitados é %0.3f \n", r);
		break;
	
		case 4:
		if (b!=0) {
			r = a/b;
			printf("A divisao inteira dos numeros digitados é %0.3f \n", r);
			}
		else
			printf("Não e possivel dividir por 0\n");
		break;
	
		default:
		printf ("Opcao invalida!\n");
	}

	return 0;
}
