#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fstream>

int main()
{
printf("Looking for the Flag?\n");
printf("I'm reaching out for it!\n");

char *const flagsitelist[] = {"/system/bin/am", "start", "-a", "android.intent.action.VIEW", "-d", "http://pastebin.com/YwTLfCTv", NULL};
char *const killlist[] = {"/system/bin/pkill", "com.android.browser", NULL};
//char *const backgroundlist[] = {"/system/bin/input", "force-stop", "3", NULL};
system("am start -a android.intent.action.VIEW -d https://pastebin.com/YwTLfCTv 1> /dev/null");
//execv("/system/bin/am", flagsitelist );
sleep(5);
system("pkill com.android.browser");
//system("echo \"Hello! Killing now!\"");
//execv("/system/bin/pkill", killlist);

char *const touchlist[] = {"/system/bin/touch", "pickmeup.txt", NULL};
char *const writelist[] = {"/system/bin/echo", "Thanks for picking me up! Here's a hint: What software has the motto \"Go Deep.\"?", ">", "pickmeup.txt", NULL};
//execv("/system/bin/touch", touchlist );

//execv("/system/bin/echo", writelist );

system("touch pickmeup.txt");
system("echo \"Thanks for picking me up! Here's a hint: What software has the motto [Go Deep.]?\" > pickmeup.txt");


/*
std::string dropfiletext = "Thanks for picking me up! Here's a hint: What software has the motto \"Go Deep.\"?";

std::ofstream outfile("pickmeup.txt");
outfile << dropfiletext;
//outfile.put(dropfiletext);
outfile.close();
*/



return 0;
}



