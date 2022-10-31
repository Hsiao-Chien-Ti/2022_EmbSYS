/*
 * Copyright (c) 2014-2020 Arm Limited and affiliates.
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include <cstdio>

// Adjust pin name to your board specification.
// You can use LED1/LED2/LED3/LED4 if any is connected to PWM capable pin,
// or use any PWM capable pin, and see generated signal on logical analyzer.
PwmOut r(PA_2);
void mode1(int);
void mode2(int);

int main()
{
    while(1)
    {
        printf("mode 1\n");
        mode1(8);
        printf("mode 2\n");    
        mode2(8);        
    }

}
void mode1(int t)
{
    r.period(0.5f);
    while(t>0)
    {
        r.write(0.7f);
        ThisThread::sleep_for(500);
        r.write(0.1f);
        ThisThread::sleep_for(500);
        r.write(0.7f);
        ThisThread::sleep_for(500);
        r.write(0.0f);
        ThisThread::sleep_for(500);
        t-=2;
    }
}
void mode2(int t)
{
    r.period(0.005f);
    while(t>0)
    {
        for(int i=1;i<=10;i++)
        {
            r.write(0.1f*i);
            ThisThread::sleep_for(100);
        }
        for(int i=0;i<=9;i++)
        {
            r.write(1-0.1f*i);
            ThisThread::sleep_for(100);
        }
        t-=2;
    }
}