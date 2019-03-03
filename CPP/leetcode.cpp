#include<iostream>
#include<stdio.h>

using namespace std;

class Box{
public:
	mutable double length;
	mutable double breadth;
	mutable double height;

	// double getVolume(){
	// 	return length*breadth*height;
	// }
	double getVolume(void);
};

double Box::getVolume(void){
	return length*breadth*height;
}

int main(){
	Box Box1;
	Box Box2;
	double volume = 0.0;

	Box1.height = 5.0;
	Box1.length = 6.0;
	Box1.breadth = 7.0;

	Box2.height = 10.0;
	Box2.length = 12.0;
	Box2.breadth = 13.0;

	volume = Box1.height * Box1.breadth * Box1.length;
	printf("Box1's volume:%.0f\n",Box1.getVolume());

	volume = Box2.height*Box2.breadth*Box2.length;
	printf("Box2's volume:%.0f\n",Box2.getVolume());
	return 0;
}

