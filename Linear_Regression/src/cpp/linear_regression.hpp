#ifndef LINEAR_REGRESSION
#define LINEAR_REGRESSION

/******** Include statements **********/

#include <vector>

/**************************************/

/********* Using statements ***********/

using vec_d = std::vector<double>;

/**************************************/

/******** Function prototypes *********/

std::pair<double, double> fitLeastSquares2D(const vec_d& x, const vec_d& y);

/**************************************/

#endif
