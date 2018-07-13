#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <windows.h>
using namespace std;

		// Pembuatan class untuk menampung fungsi-fungsi yang ada
class tugas1{
public:

		// Fungsi Mencari Faktorial
	long int faktorial(int n){
		
		if(n == 0 || n == 1){
				return 1;
		}else{
			return n*faktorial(n-1);
		}
	};
		
		// Fungsi Mencari Hanoi
	void hanoi(int n, char a, char b, char c){
		if(n == 1){
			printf("\n Pindahan piring dari %c ke %c",a,c);
		}else{
			hanoi(n-1,a,c,b);
			hanoi(1,a,b,c);
			hanoi(n-1,b,a,c);
		}
	};
	
		// Fungsi Fibonacci
	void fibonacci(int n){
		int a, b, c;
		a = 0; b = 1;
		cout << a << " " <<b;
		for(int i=1; i<= n-2; i++){
			c = a + b;
			cout << " " << c;
			a = b;
			b = c;
		}
	};
	
		// Fungsi Search Algoritma Array
	int linear_search(int key){
		int list[] = {1,2,3,4,5,6,7,8,9,0};
		for(int i = 0; i < 10; i++){
			if(key == list[i]){
				return i;
			}
		}
	};
};
												// Fungsi Utama
int main(){
	
	int angka;									// init variabel
	int input;
	
	tugas1 t1;									// Pembuatan Object atau Instance dari class tugas1
	
	system("cls");
	
	printf("\n\n\t == Fakhrizal Asshiddiq ==\n\n");
	printf("[1] Faktorial");
	printf("\n[2] Segitiga Hanoi");
	printf("\n[3] Fibonacci");
	printf("\n[4] Search Array");
	printf("\n\n   [?] Masukkan Angka : ");
	cin >> input;									// masukkan nilai ke variabel input
	
	if(input == 1){
		system("cls");
		printf("\n\n\t == FAKTORIAL ==\n\n");
		printf("\n\n   [?] Masukkan Angka : ");
		cin >> angka;	// masukkan nilai ke variabel angka		
		printf("\n\t[+] Hasil dari faktorial %d! = %ld",angka,t1.faktorial(angka));
		printf("\n\n\n[-] Tunggu 2 detik ...");Sleep(2 * 1000);main();
	}else if(input == 2){
		system("cls");
		printf("\n\n\t == HANOI ==\n\n");
		printf("\n\n   [?] Masukkan Jumlah Piring : ");
		cin >> angka;								// masukkan nilai ke variabel angka
		t1.hanoi(angka,'A','B','C');
		printf("\n\n\n[-] Tunggu 2 detik ...");Sleep(2 * 1000);main();
	}else if(input == 3){
		system("cls");
		printf("\n\n\t == FIBONACCI ==\n\n");
		printf("\n\n   [?] Masukkan Angka : ");
		cin >> angka;	// masukkan nilai ke variabel angka		
		printf("\n[+] ");t1.fibonacci(angka);
		printf("\n\n\n[-] Tunggu 2 detik ...");Sleep(2 * 1000);main();
	}else if(input == 4){
		system("cls");
		printf("\n\n\t == SEARCHING ==\n\n");
		printf("\n\n   [?] Masukkan key : ");
		cin >> angka;	// masukkan nilai ke variabel angka		
		printf("\n\t[+] Kunci[%d] terdapat pada index array ke = %d",angka,t1.linear_search(angka));
		printf("\n\n\n[-] Tunggu 2 detik ...");Sleep(2 * 1000);main();
	}else{
		main();
	}	
}				// end of main fungsi
