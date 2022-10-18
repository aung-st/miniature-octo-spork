import java.lang.Math;

public class fixed_point_iteration {
    //initial input into approximation function
    static double x = 1.0;
    //lambda value
    static float y = 1/12;

    //p(x) function
    public static double p(double x){
        return x*((Math.pow(x,2)-5));
    }

    //g(x) approximation function
    public static double g(double x){
        return x+((y*p(x))*(Math.pow(x,2)-3));
    }
    public static void main(String[] args){    
    
    //initialize functions
    double px = p(x);
    double gx = g(x);

    //chooose n iterations (0 index)
    int max_iter = 10;

    //store following values into array to print later
    double[] approximations = new double[max_iter];
    double[] errors = new double[max_iter];
    double[] alphas = new double[max_iter];
    
    System.out.println("balls "+gx);

    //iterate to converge to sqrt(3)
    for (int i=0;i<max_iter;i++){
        approximations[i] = gx;
        errors[i] = Math.abs(gx - Math.sqrt(3));

        x = gx;
        px = p(x);
        gx = x+((y*px)*(Math.pow(x,2)-3));
    }

    System.out.println("approximation of "+Math.sqrt(3));
    System.out.println();
    
    //First and last index have no alpha values due to the nature of the formula for order of convergence
    alphas[0] = -1;
    alphas[max_iter-1]=-1;

    //calculate order of convergence
    for (int j=1;j<max_iter-1;j++){
        alphas[j] = Math.log(errors[j+1]/errors[j])/Math.log(errors[j]/errors[j-1]);
        }
    
    for (int k =0;k<max_iter;k++){
        System.out.println(k+" "+approximations[k]+" "+errors[k]+" "+alphas[k]);     
        }
    }
}

