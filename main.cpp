#include "bits/stdc++.h"

using namespace std;

struct Know{
    double n, N, m, M, Na;
};

void solve(Know &a, string want){
    if (want=="Масса"){
        if (a.n == -1)solve(a, "Вещества");
        if (a.M == -1)solve(a, "Частицы");
        a.m = a.n*a.M;
        cout<<"m = n * M = "<<a.n<<" моль * "<<a.M<<" г/моль = "<<a.m<<" г\n";
    }else if(want == "Вещества"){
        if(a.N!=-1){
            a.n = a.N/a.Na;
            cout<<"n = N/Na = "<<a.N<<" частиц / "<<a.Na<<" частиц/моль = "<<a.n<<" моль\n";
        }else{
            if (a.m==-1)solve(a, "Масса");
            a.n = a.m/a.M;
            cout<<"n = m/M = "<<a.m<<" г / "<<a.M<<" г/моль = "<<a.n<<" моль\n";
        }
    }else if (want == "Частицы"){
        if (a.n==-1)solve(a, "Вещества");
        a.N = a.n*a.Na;
        cout<<"N = n*Na = "<<a.n<<" моль * "<<a.Na<<"частиц/моль = "<<a.N<<" частиц\n";
    }else cout<<"Неизвестный запрос попробуйте еще\n";
}

int main(){
    Know Mole = {-1,-1,-1,-1, 6.02e23};
    cout<<"Выберите, что вы знаете для реения хим. задачи:\n";
    cout<<"Введите молярную массу вещества над которым будем работать:\n";
    cin >> Mole.M;
    while(true) {
        cout << "Введите что вы знаете еще или '0' для завершения ввода\n";
        string q;
        cin >> q;
        if (q == "0")break;
        else if (q == "Масса") {
            cin >> Mole.m;
        } else if (q == "Вещества") {
            cin >> Mole.n;
        } else if (q == "Частицы") {
            cin >> Mole.N;
        } else {
            cout << "Повторите попытку\n";
        }
    }
    while(true){
        cout<<"Введите что вы хотите знать или '0' для завершения работы программы\n";
        string q; cin >> q;
        if (q=="0")break;
        solve(Mole, q);
    }

}
