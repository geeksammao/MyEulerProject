public class Test {
    public static void main(String[] args) {
        int [] a = new int[200];
        int j,k,ans,answer,l,end;
        for(int n=0;n<200;n++)
        {
            a[n] = 0;
        }
        for(int i=1;;i++)
        {
            k = 0;
            answer = i*(i+1)/2;
            ans = i*(i+1)/2;


            for(j=2;j<=ans;j++)
            {
                if(ans%j == 0)
                {
                    while(ans%j==0)
                    {
                        a[k]++;
                        ans = ans / j;
                    }
                    k++;
                }
            }
            end = 1;
            for(l=0;l<k;l++)
            {
                end = (a[l]+1)*end;
            }
            if(end >= 500)
            {
                System.out.print(answer);
                break;
            }
            for(int n=0;n<200;n++)
            {
                a[n] = 0;
            }
        }
    }
}
