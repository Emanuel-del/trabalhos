#include <iostream>
#include <vector>
#include <set>
#include <cstdlib>
#include <ctime>


using namespace std;

// Função para exibir o joguinho de campo minado!!
void mostrarCampo(vector<vector<char>>& campo) {
    cout << "     A   B   C   D   E   F\n";
    for (int i = 0; i < 6; ++i) {
        cout << i + 1 << "  ";
        for (int j = 0; j < 6; ++j) {
            cout << "[" << campo[i][j] << "] ";
        }
        cout << endl;
    }
}

// Função para converter a jogada em índices da matriz
pair<int, int> converterEntrada(string jogada) {
    int coluna = toupper(jogada[0]) - 'A'; // A -> 0, B -> 1, etc.
    int linha = jogada[1] - '1';           // 1 -> 0, 2 -> 1, etc.
    return make_pair(linha, coluna);
}

int main() {
    // Inicializa o campo minado
    vector<vector<char>> campo(6, vector<char>(6, ' '));
    
    // Sorteia aleatoriamente 3 bombas
    set<pair<int, int>> bombas;
    srand(time(0));
    
    while (bombas.size() < 3) {
        int linha_bomba = rand() % 6;
        int coluna_bomba = rand() % 6;
        bombas.insert(make_pair(linha_bomba, coluna_bomba));
    }

    // Contador de Jogadas do jogador
    int jogadas = 5;
    set<pair<int, int>> jogadas_feitas;

    while (jogadas > 0) {
        mostrarCampo(campo);
        
        string jogada;
        bool jogada_valida = false;
        
        while (!jogada_valida) {
            cout << "Escolha uma posição (ex: A1, B2): ";
            cin >> jogada;

            if (jogada.length() == 2 && toupper(jogada[0]) >= 'A' && toupper(jogada[0]) <= 'F' && jogada[1] >= '1' && jogada[1] <= '6') {
                pair<int, int> pos = converterEntrada(jogada);

                // Verifica se a jogada já foi feita
                if (jogadas_feitas.find(pos) == jogadas_feitas.end()) {
                    jogada_valida = true;
                    jogadas_feitas.insert(pos);

                    // Verifica se o usuário acertou a bomba
                    if (bombas.find(pos) != bombas.end()) {
                        campo[pos.first][pos.second] = 'X';
                        mostrarCampo(campo);
                        cout << "Você pisou em uma mina! Game Over." << endl;
                        return 0;
                    } else {
                        campo[pos.first][pos.second] = 'O';
                        --jogadas;
                        cout << "Jogada correta! Restam " << jogadas << " jogadas." << endl;
                    }
                } else {
                    cout << "Você já escolheu essa posição. Tente outra." << endl;
                }
            } else {
                cout << "Entrada inválida. Tente novamente." << endl;
            }
        }
    }

    mostrarCampo(campo);
    cout << "Parabéns! Você venceu o jogo!" << endl;

    return 0;
}
