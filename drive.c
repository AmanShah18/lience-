# include<stdio.h>

int main(){
    int a;
    printf("enter your age\n");
    scanf("%d",&a);
    if (a>100){
        printf("you are dead\n");
        return 0;
    }
    
    else if(a<7){
        printf("you are a child\n");
        return 0;
    }
    
    if(a>18){
        printf("you can drive\n");
    }
    else if(a==18){
        printf("you have to give the trial");
    }
    else{
        printf("you cannot drive go to home");
    }
    return 0;
}