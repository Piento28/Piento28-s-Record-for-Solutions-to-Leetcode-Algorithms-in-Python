#include<stdio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

class TakeBus{
public:
	void TakeBusToSubway(){
		cout<<"TakeBus:TakeBusToSubway"<<endl;
	}
	void TakeBusToStation(){
		cout<<"TakeBus:TakeBusToStation"<<endl;
	}
};

class Bus{
public:
	virtual void TakeBusToSomewhere(TakeBus &tb)=0;
};

class Subway:public Bus{
public:
	virtual void TakeBusToSomewhere(TakeBus &tb){
		tb.TakeBusToSubway();
	}
};

class Station:public Bus{
public:
	virtual void TakeBusToSomewhere(TakeBus &tb){
		tb.TakeBusToStation();
	}
};

int main(){
	TakeBus tb;
	Bus *b = NULL;
	for (int i=1;i<=10;i++){
		if ((rand()%i)&1)
			b = new Subway;
		else
			b = new Station;
		b->TakeBusToSomewhere(tb);
	}
	delete b;
	return 0;
}

