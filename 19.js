var isLeap = false;

var y = 1900;

var monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

var thisMonth = 0;

var date = 1;

var days = ["m","t","w","h","f","s","u"];

var dayOfWeek = 0;

var sundayFirsts = 0;

while(y<2001){
		
	if(((dayOfWeek == 6) && (date == 1))&&y > 1900){
		sundayFirsts++;
	}
	date++;
	dayOfWeek = (dayOfWeek+1)%7;
	if(date > monthDays[thisMonth]){
		thisMonth++;
		date = 1;
	}
	if(thisMonth>11){
		y++;
		thisMonth = 0;
		if(y%4==0){
			if(y%100==0){
				if(y%400==0){
					isLeap = true;
				}else{
					isLeap = false;
				}
			}else{
				isLeap = true;
			}
		}else{
			isLeap = false;
		}

		monthDays = [31,isLeap?29:28,31,30,31,30,31,31,30,31,30,31];
	}

}

console.log(sundayFirsts);
