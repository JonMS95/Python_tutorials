/******** Include statements **********/

#include <vector>
#include <cmath>
#include <stdexcept>

/**************************************/

/********* Using statements ***********/

using vec_d = std::vector<double>;

/**************************************/

/**** Private function prototypes *****/

static double getMeanValue(const vec_d& vec);

/**************************************/

/******* Function definitions *********/

/// @brief Returns mean value for a given vector.
/// @param vec Target vector.
/// @return Vector's mean value.
static double getMeanValue(const vec_d& vec)
{
    double ret = 0;

    for(double d : vec)
        ret += d;
    
    return (ret / vec.size());
}

/// @brief Performs least squares method over a given dataset.
/// @param x X-axis
/// @param y Y-axis
/// @return Intercept (b) and slope (a) values (f(x) = ax + b).
std::pair<double, double> fitLeastSquares1F(const vec_d& x, const vec_d& y)
{
    if(x.size() != y.size() || x.empty())
        throw std::invalid_argument("Both vectors should be the same non-zero size");

    const double x_mean = getMeanValue(x);
    const double y_mean = getMeanValue(y);

    double covariance   = 0;
    double variance     = 0;
    double dx           = 0;
    double dy           = 0;

    for(std::size_t idx = 0; idx < x.size(); idx++)
    {
        dx = (x[idx] - x_mean);
        dy = (y[idx] - y_mean);
        
        covariance  += (dx * dy);
        variance    += (dx * dx);
    }

    if(variance == 0.0)
        throw std::runtime_error("Variance of X-axis data is zero");

    const double slope      = covariance / variance;
    const double intercept  = y_mean - slope * x_mean;

    return {intercept, slope};
}

/**************************************/
