#include <Servo.h>
#include <math.h>

Servo gripper;
Servo lower_motor;
Servo upper_motor;

void setup() {
  gripper.attach(9);
  gripper.write(90);
  upper_motor.attach(10);
  lower_motor.attach(11);
}


double AT1[2], AT2[2], AT3[2], T1[2], T2[2], T3[2], H[2];

double positions[][2] = {AT1, AT2, AT3, T1, T2, T3, H};


double l1 = 8.5;
double l2 = 20.8;
// double l3 = 
// double l4 = 
// double l5 = 

double theta(double x, double y) {
    double numerator = x * x + pow(9.5 - y, 2) - a * a - b * b;
    double denominator = -2 * a * b;
    
    double angle = 180 - asin((b * sin(acos(numerator / denominator))) / sqrt(a*a + b*b - 2*a*b*(numerator/denominator))) - atan(x / (9.5 - y));
    
    double offset = 45;
    return offset + angle;
}


// double phi(double x, double y){
//   double angle = 0;
//   double offset = 0;
//   return angle;
// }


 void moveto({

 })
 
void loop() {
  //double approach1[] = {theta,phi}
  // gripper.write(95); 
  // delay(2000);       
  // upper_motor.write(45);
  // delay(2000); 
  // gripper.write(0); 
  // delay(2000);
  
 
  
  upper_motor.write(135);
  lower_motor.write(90);
}
