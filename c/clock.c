/* Terminal clock */

#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main(){
	while (1){
		time_t now;
		time(&now);
		struct tm*local = localtime (&now);

		printf("\033[H\033[J");

		printf("Hora actual: %02d:%02d:%02d\n",
			local->tm_hour,
			local->tm_min,
			local->tm_sec);
		sleep(1);
	}
	return 0;
}
