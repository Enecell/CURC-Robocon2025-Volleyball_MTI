#include <stdio.h>
#include <math.h>

//本代码在https://github.com/Enecell/CURC-Robocon2025-Volleyball_FJUT开源
//在闲鱼购买请联系原作者LL3323126216@163.com+

/////////////////////////////////////////////
//直接在此处设定你的机械数据，然后运行
//示例数据
double R=20;//静平面半径
double r=30;//动平面半径
double L=180;//主臂长度
double La=200;//从臂长度

/////////////////////////////////////////////


////////////////////////////////////////////
//中间变量声明部分，无需修改
//输入
double x=0;
double y=0;
double z=0;
//输出角度
double theta_1__=0;//西塔角1（主臂和静平面夹角）
double theta_2__=0;//西塔角2
double theta_3__=0;//西塔角3
//转换弧度
double theta_1=0;//西塔角1（主臂和静平面夹角）
double theta_2=0;//西塔角2
double theta_3=0;//西塔角3
//一些中间变量
double A1=0;
double A2=0;
double A3=0;

double B1=0;
double B2=0;
double B3=0;

double C1=0;
double C2=0;
double C3=0;

double K1=0;
double K2=0;
double K3=0;

double U1=0;
double U2=0;
double U3=0;

double V1=0;
double V2=0;
double V3=0;
///////////////////////////////////////

int main(){
	
	
	printf("请输入x,y,z值，分别用空格隔开，计算后将会输出该坐标下的三个theta角\n");
	scanf("%lf %lf %lf",&x,&y,&z);
	
	A1=(x*x+y*y+z*z+L*L-La*La+(R-r)*(R-r)-2*x*(R-r))/(2*L);
	B1=-(R-r-x);
	C1=z;
	   
	A2=(x*x+y*y+z*z+L*L-La*La+(R-r)*(R-r)+(x-sqrt(3)*y)*(R-r))/L;
	B2=-2*(R-r)-(x-sqrt(3)*y);
	C2=2*z;
	   
	A3=(x*x+y*y+z*z+L*L-La*La+(R-r)*(R-r)+(x+sqrt(3)*y)*(R-r))/L;
	B3=-2*(R-r)-(x+sqrt(3)*y);
	C3=2*z;
	
	K1=A1+B1;
	U1=2*C1;
	V1=A1-B1;
	
	K2=A2+B2;
	U2=2*C2;
	V2=A2-B2;
	
	K3=A3+B3;
	U3=2*C3;
	V3=A3-B3;
	
	theta_1=atan((-U1-sqrt(U1*U1-4*K1*V1))/(2*K1));
	theta_2=atan((-U2-sqrt(U2*U2-4*K2*V2))/(2*K2));
	theta_3=atan((-U3-sqrt(U3*U3-4*K3*V3))/(2*K3));
	
	theta_1__=2*theta_1*(180.0/M_PI);//弧度转角度
	theta_2__=2*theta_2*(180.0/M_PI);
	theta_3__=2*theta_3*(180.0/M_PI);
	
	printf("X=%lf,Y=%lf,Z=%lf\n",x,y,z);
	printf("验证：theta_1=%lf,theta_2=%lf,theta_3=%lf\n",theta_1__,theta_2__,theta_3__);
	
	
	
	return 0;
}



//本代码在https://github.com/Enecell/CURC-Robocon2025-Volleyball_FJUT开源
//在闲鱼购买请联系原作者LL3323126216@163.com+
