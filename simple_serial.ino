char x[11];
bool variable = true;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
  while (!Serial.available());

  for(int i=0; i<6;i++){
    x[i]=Serial.read();
    if(x[i]== ','){
      Serial.print("found a comma");
      }
    
    
  }
  
  int y = String(x).toInt();

  Serial.print(y);

   
  


 
  //x = Serial.read();
  //Serial.print(x);
  //Serial.flush();
}