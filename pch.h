#ifndef PCH_H
#define PCH_H

#include "framework.h"

extern "C" __declspec(dllexport) int Poweroff_Server();
extern "C" __declspec(dllexport) int Startup_Server();

#endif //PCH_H
