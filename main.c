#include <stdio.h>
#include <stdint.h>
#include "cc_cfg.c"

volatile char var_1 = 9;
volatile char var_2 = 99;
volatile char var_3; 
volatile char var_4; 
volatile char var_5; 
volatile char var_6; 

#define it_true 1
#define it_false 0

void main(void)
{
}


void case1(void)
{
    uint8_t a;
#if defined (HEV)
        if(var_1 <10)
        {
        a = it_true; 
        }
#elif defined (BEV) || (CCG)
        if(var_1 <10)
        {
        a = it_false; 
        }
#endif
}

void case2(void)
{
    uint8_t a;
#if defined (CCL_1)
    if(var_1 == 9)
    {
        var_2 = 100;
    }
#endif
#if defined (HEV) || (CCG)
    if(var_1 <10)
    {
    a = it_true; 
    }
#elif defined (BEV) || (HAV)
        if(var_1 >10)
        {
        a = it_false; 
        }
#endif
}
#if (defined(HEV))
int case3(void)
{
    int adc;
#if (defined(CCL_1))
    if(var_1 > 100)
    {
        adc = it_false;
    }
#elif (defined(CCL_2))
    /*do nothing*/
#endif
}

#endif


int case4(void)
{
#if (defined(CCL_2))
    if((var_2 || var_3) 
#elif (defined(CCL_1))
    if((var_1)
#endif
    || (var_4) && ( var_5))
    {
        var_6 = 1;
    }
}