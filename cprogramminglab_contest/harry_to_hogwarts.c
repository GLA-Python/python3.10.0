#include <stdio.h>
int main()
{int n,n1,a[100],min=0,b,max=0,i,k=0,d=4,count=0;
scanf("%d",&n);
while(n!=6174)
{
for (int i = d-1; i >= 0; i--)
{
    a[i] = n%10;
    n=n/10;
}
for (int i = 0; i < d; i++)
{
    for (int j = i+1; j < d; j++)
    {
        if (a[i]>a[j])  
        {
            b = a[i];
            a[i] = a[j];
            a[j] = b;
        }
    }
}
for (int i = 0; i < d; i++)
{
    min = min*10 + a[i];
}
for (int i = 0; i < d; i++)
{
    for (int j = i+1; j < d; j++)
    {
        if (a[i]<a[j])  
        {
            b = a[i];
            a[i] = a[j];
            a[j] = b;
        }
    }
}
for (int i = 0; i < d; i++)
{
    max = max*10 + a[i];
}
n = max - min;
max=0;
min=0;
count++;
}
printf("%d",count);

return 0;
}