### 버즈니 점심뽑기 봇
* 점심시간에 팀을 나누어 주는 봇. cron으로 돌림
* 필요한 설정파일
	* sender_account.secret
		* 이메일을 보내주는 gmail계정
		* format : email,passwd
	* members.secret
		* csv형식으로 된 멤버들의 정보
		* format : email,name,status,gender,commander
