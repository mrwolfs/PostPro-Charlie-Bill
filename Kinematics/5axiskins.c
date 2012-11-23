/********************************************************************
* Description: 5axiskins.c
*   Trivial kinematics for 3 axis Cartesian machine
*
*   Derived from a work by Fred Proctor & Will Shackleford
*
* Author:
* License: GPL Version 2
* System: Linux
*    
* Copyright (c) 2007 Chris Radek
*
* Last change:
* $Revision: 1.5 $
* $Author: cradek $
* $Date: 2007/11/17 04:41:59 $
********************************************************************/

#include "kinematics.h"		/* these decls */
#include "posemath.h"
#include "hal.h"
#include "rtapi_math.h"

#define d2r(d) ((d)*PM_PI/180.0)
#define r2d(r) ((r)*180.0/PM_PI)

struct haldata {
    hal_float_t *tool_length;
    hal_float_t pivot_length;
} *haldata;

static PmCartesian s2r(double r, double t, double p) {
    PmCartesian c;
    t = d2r(t), p = d2r(p);

    c.x = r * sin(p) * cos(t);
    c.y = r * sin(p) * sin(t);
    c.z = r * cos(p);

    return c;
}

static int fez(double n) {
    // fuzzy equal to zero
    const double small = 0.00001;

    return n<small && n>-small;
}

int kinematicsForward(const double *joints,
		      EmcPose * pos,
		      const KINEMATICS_FORWARD_FLAGS * fflags,
		      KINEMATICS_INVERSE_FLAGS * iflags)
{
    PmCartesian r = s2r(haldata->pivot_length + *haldata->tool_length - joints[8], joints[5], 180.0 - joints[3]);
    int upright = fez(joints[3]) && fez(joints[5]);

    pos->tran.x = joints[0] + r.x;
    pos->tran.y = joints[1] + r.y;
    if(upright)
        pos->tran.z = joints[2] + joints[8];
    else
        pos->tran.z = joints[2] + haldata->pivot_length + r.z + *haldata->tool_length;
    pos->a = joints[3];
    pos->b = joints[4];
    pos->c = joints[5];
    pos->u = joints[6];
    pos->v = joints[7];
    pos->w = joints[8];

    return 0;
}

int kinematicsInverse(const EmcPose * pos,
		      double *joints,
		      const KINEMATICS_INVERSE_FLAGS * iflags,
		      KINEMATICS_FORWARD_FLAGS * fflags)
{

    PmCartesian r = s2r(haldata->pivot_length + *haldata->tool_length - pos->w, pos->c, 180.0 - pos->a);
    int upright = fez(pos->a) && fez(pos->c);

    joints[0] = pos->tran.x - r.x;
    joints[1] = pos->tran.y - r.y;
    if(upright)
        joints[2] = pos->tran.z - pos->w;
    else
        joints[2] = pos->tran.z - haldata->pivot_length - r.z - *haldata->tool_length;
    joints[3] = pos->a;
    joints[4] = pos->b;
    joints[5] = pos->c;
    joints[6] = pos->u;              /* feed y motion into joint 7: v axis) */
    joints[7] = pos->v;   /* was:   joints[7] = pos->v;     tran.y - r.y;     */
    joints[8] = pos->w;

    return 0;
}

/* implemented for these kinematics as giving joints preference */
int kinematicsHome(EmcPose * world,
		   double *joint,
		   KINEMATICS_FORWARD_FLAGS * fflags,
		   KINEMATICS_INVERSE_FLAGS * iflags)
{
    *fflags = 0;
    *iflags = 0;

    return kinematicsForward(joint, world, fflags, iflags);
}

KINEMATICS_TYPE kinematicsType()
{
    return KINEMATICS_BOTH;
}

#ifdef RTAPI
#include "rtapi.h"		/* RTAPI realtime OS API */
#include "rtapi_app.h"		/* RTAPI realtime module decls */
#include "hal.h"

EXPORT_SYMBOL(kinematicsType);
EXPORT_SYMBOL(kinematicsForward);
EXPORT_SYMBOL(kinematicsInverse);
MODULE_LICENSE("GPL");

int comp_id;
int rtapi_app_main(void) {
    int result;
    comp_id = hal_init("5axiskins");
    if(comp_id < 0) return comp_id;

    haldata = hal_malloc(sizeof(struct haldata));

    result = hal_pin_float_new("5axiskins.tooloffset.z", HAL_IN, &(haldata->tool_length), comp_id);
    if(result < 0) goto error;
    result = hal_param_float_new("5axiskins.pivot-length", HAL_RW, &(haldata->pivot_length), comp_id);
    if(result < 0) goto error;

    haldata->pivot_length = 250.0;

    hal_ready(comp_id);
    return 0;

error:
    hal_exit(comp_id);
    return result;
}

void rtapi_app_exit(void) { hal_exit(comp_id); }
#endif
