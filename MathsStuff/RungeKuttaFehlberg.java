import static java.lang.Math.*;

/**
 * Numerical Analysis
 public class RungeKuttaFehlberg
{

    /**
     * The function f that defines the first-order ODE.
     */
    static double f(double x, double y)
    {
        double val = 2*x*x - Math.tanh(4.2*x*y);
        return val;
    }

    /**
     * The Runge-Kutta fourth order method for the ODE on the interval [a,b] with start value y0, using n steps.
     */
    static double rungeKutta4(double a, double b, double y0, int n)
    {
        double h = (b-a)/n;
        double y = y0;
        double x = a;        

        for (int i = 0; i < n; i++) 
        {            
            double k1 = h * f(x, y);
            double k2 = h * f(x + h/2, y + k1/2);
            double k3 = h * f(x + h/2, y + k2/2);
            double k4 = h * f(x + h, y + k3);
            y = y + (k1 + 2*k2 + 2*k3 + k4)/6;
            x = x + h;
        }

        return y;

    }
    
    
    
    
    
    
    static double rungeKuttaC(double a, double b, double y0, int n)
    {
        double h = (b-a)/n;
        double y = y0;
        double x = a;

        for (int i = 0; i < n; i++) 
        {            
            double k1 = h*f(x, y); 
            double k2 = h*f(x + h/2.0, y + k1/2.0);
            double k3 = h*f(x + 3.0/4.0*h, y + 0*k1+3.0/4.0*k2);
            double k4 = h*f(x + h, y + 2.0/9.0*k1 + 1.0/3.0*k2 + 4.0/9.0*k3);

            y = y + 7.0/24.0*k1 + 1.0/4.0*k2 + 1.0/3.0*k3 + 1.0/8.0*k4;
            x = x + h;
        }

        return y;

    }
    
    
    
    
    
    
    /**
     * The Runge-Kutta method "A",
     * on the interval [a,b] with start value y0, using n steps.
     */
    static double rungeKuttaA(double a, double b, double y0, int n)
    {
        double h = (b-a)/n;
        double y = y0;
        double x = a;

        for (int i = 0; i < n; i++) 
        {            
            double k1 = h*f(x, y); 
            double k2 = h*f(x + h/4.0, y + k1/4.0);
            double k3 = h*f(x + 3.0/8.0*h, y + 3.0/32.0*k1+9.0/32.0*k2);
            double k4 = h*f(x + 12.0/13.0*h, y + 1932.0/2197.0*k1 - 7200.0/2197.0*k2 + 7296.0/2197.0*k3);
            double k5 = h*f(x + h, y + 439.0/216.0*k1 - 8.0*k2 + 3680.0/513.0*k3 - 845.0/4104.0*k4);

            y = y + 25.0/216.0*k1 + 1408.0/2565.0*k3 + 2197.0/4104.0*k4 - 1.0/5.0*k5;
            x = x + h;
        }

        return y;

    }

    /**
     * The Runge-Kutta method "B",
     * on the interval [a,b] with start value y0, using n steps.
     */
    static double rungeKuttaB(double a, double b, double y0, int n)
    {
        double h = (b-a)/n;
        double y = y0;
        double x = a;

        for (int i = 0; i < n; i++) 
        {            
            double k1 = h*f(x, y); 
            double k2 = h*f(x + h/4.0, y + k1/4.0);
            double k3 = h*f(x + 3.0/8.0*h, y + 3.0/32.0*k1+9.0/32.0*k2);
            double k4 = h*f(x + 12.0/13.0*h, y + 1932.0/2197.0*k1 - 7200.0/2197.0*k2 + 7296.0/2197.0*k3);
            double k5 = h*f(x + h, y + 439.0/216.0*k1 - 8.0*k2 + 3680.0/513.0*k3 - 845.0/4104.0*k4);
            double k6 = h*f(x+ 1.0/2.0*h, y - 8.0/27.0*k1 + 2.0*k2 - 3544.0/2565.0*k3 + 1859.0/4104.0*k4 - 11.0/40.0*k5);
            
            y = y + 16.0/135.0*k1 + 6656.0/12825.0*k3 + 28561.0/56430.0*k4 - 9.0/50.0*k5 + 2.0/55.0*k6;
            x = x + h;
        }

        return y;

    }

    /**
     * The adaptive Runge-Kutta-Fehlberg method. Its parameters are:
     * 
     * a, b - the interval bounds
     * y0 - the initial value of the ODE
     * tol - the tolerance
     * hmin, hmax - the minimal and maximal stepsize
     */
    static double rungeKuttaCombined(double a, double b, double y0, double tol, double hmin, double hmax)
    {
        double h = hmax;
        double x = a; 
        double y = y0;
        double counter = 0;
        
        while (x < b) 
        {
            double k1 = h*f(x, y); 
            double k2 = h*f(x + h/4.0, y + k1/4.0);
            double k3 = h*f(x + 3.0/8.0*h, y + 3.0/32.0*k1+9.0/32.0*k2);
            double k4 = h*f(x + 12.0/13.0*h, y + 1932.0/2197.0*k1 - 7200.0/2197.0*k2 + 7296.0/2197.0*k3);
            double k5 = h*f(x + h, y + 439.0/216.0*k1 - 8.0*k2 + 3680.0/513.0*k3 - 845.0/4104.0*k4);
            double k6 = h*f(x+ 1.0/2.0*h, y - 8.0/27.0*k1 + 2.0*k2 - 3544.0/2565.0*k3 + 1859.0/4104.0*k4 - 11.0/40.0*k5);
            
            double yA = y + 25.0/216.0*k1 + 1408.0/2565.0*k3 + 2197.0/4104.0*k4 - 1.0/5.0*k5;
            double yB = y + 16.0/135.0*k1 + 6656.0/12825.0*k3 + 28561.0/56430.0*k4 - 9.0/50.0*k5 + 2.0/55.0*k6;
            
            double r = abs(yA-yB)/h;
         
            if (r <= tol) 
            {
                x = x + h;
                y = yA;
                counter = counter + 1;
            }
            double q = pow(tol/(2.0*r), 0.25);
            if (q <= 0.1) 
            {
                h = 0.1*h;
            }
            else if (q >= 4.0)
            {
                h = 4.0*h;
            }
            else 
            {
                h = q*h;
            }
            
            if (h > hmax) 
            {
                h = hmax;
            }
            if (x+h > b) 
            {
                h = b-x;
            }
            else if (h < hmin) 
            {
                throw new ArithmeticException("minimum step size exceeded");
            }

        }
        System.out.println(counter);
        return y; 
    }


}
