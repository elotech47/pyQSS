#pragma once

#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

using std::abs;

typedef std::vector<double> dvec;

namespace mathUtils
{
    // Sign function
    inline int sign(double x) {
        return (x > 0) - (x < 0);
    }

    // Check if vector contains NaN
    inline bool notnan(const dvec& v) {
        for (size_t i = 0; i < v.size(); i++) {
            if (!(v[i] > 0) && !(v[i] <= 0)) {
                return false;
            }
        }
        return true;
    }

    // Check if double is not NaN
    inline bool notnan(double v) {
        return (v > 0 || v <= 0);
    }
}