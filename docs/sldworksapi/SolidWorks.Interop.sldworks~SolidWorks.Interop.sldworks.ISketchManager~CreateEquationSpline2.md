# CreateEquationSpline2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline2`

Creates an equation-driven 2D explicit or parametric curve or a 3D parametric curve.
Creates an equation-driven 2D explicit or parametric curve or a 3D parametric curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEquationSpline2( _
   ByVal XExpression As System.String, _
   ByVal YExpression As System.String, _
   ByVal ZExpression As System.String, _
   ByVal RangeStart As System.String, _
   ByVal RangeEnd As System.String, _
   ByVal IsAngleRange As System.Boolean, _
   ByVal RotationAngle As System.Double, _
   ByVal XOffset As System.Double, _
   ByVal YOffset As System.Double, _
   ByVal LockStart As System.Boolean, _
   ByVal LockEnd As System.Boolean _
) As SketchSpline
```

```

Dim instance As ISketchManager
Dim XExpression As System.String
Dim YExpression As System.String
Dim ZExpression As System.String
Dim RangeStart As System.String
Dim RangeEnd As System.String
Dim IsAngleRange As System.Boolean
Dim RotationAngle As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim LockStart As System.Boolean
Dim LockEnd As System.Boolean
Dim value As SketchSpline
 
value = instance.CreateEquationSpline2(XExpression, YExpression, ZExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

```

SketchSpline CreateEquationSpline2( 
   System.string XExpression,
   System.string YExpression,
   System.string ZExpression,
   System.string RangeStart,
   System.string RangeEnd,
   System.bool IsAngleRange,
   System.double RotationAngle,
   System.double XOffset,
   System.double YOffset,
   System.bool LockStart,
   System.bool LockEnd
)
```

```

SketchSpline^ CreateEquationSpline2( 
   System.String^ XExpression,
   System.String^ YExpression,
   System.String^ ZExpression,
   System.String^ RangeStart,
   System.String^ RangeEnd,
   System.bool IsAngleRange,
   System.double RotationAngle,
   System.double XOffset,
   System.double YOffset,
   System.bool LockStart,
   System.bool LockEnd
) 
```

#### Parameters

*XExpression*
:   For a parametric curve, equation for x in terms of t; for an explicit curve, an empty string (see **Remarks**)

*YExpression*
:   For a parametric curve, equation for y in terms of t; for an explicit curve, equation for y in terms of x (see **Remarks**)

*ZExpression*
:   Equation for z in terms of t (see **Remarks**)

*RangeStart*
:   Start value for x, if explicit; start value for t, if parametric (see **Remarks**)

*RangeEnd*
:   End value for x, if explicit; start value for t, if parametric (see **Remarks**)

*IsAngleRange*
:   :   True if the range and x value represent an angle (in radians), false if not (see **Remarks**)

*RotationAngle*
:   Rotation angle (in radians) for the curve (see **Remarks**)

*XOffset*
:   Translation in the x direction of the curve  (see **Remarks**)

*YOffset*
:   Translation in the y direction of the curve (see **Remarks**)

*LockStart*
:   True to lock the start point (RangeStart) of the curve, false to not

*LockEnd*
:   True to lock the end point (RangeEnd) of the curve, false to not

#### Return Value

[Equation-driven curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)

Remarks

**XExpression**

If you want:

- an explicit curve (only in 2D) of the form y=f(x), then this input should be "".
- a parametric curve given in terms of the parameter t, then this input is the value of x given in terms of the parameter. For example:  
    
  x=sin(t)

**YExpression**

If you want:

- an explicit curve (only in 2D) of the form y=f(x), then this input should be a function in terms of x to use to compute the value of y. For example:  
    
  y=exp(x)
- a parametric curve given in terms of the parameter t, then this input is the value of y given in terms of the parameter. For example:  
    
  y=cos(t)

**ZExpression**

For 3D parametric curves, this input is the value of z given in terms of parameter t. For example:

> z = t

**RangeStart** and **RangeEnd**

Strings so that you can input dimension names or pi; for example, "10\* width\_dimension1" or "-pi/2".

**XOffset**, **YOffset**, **IsAngleRange**, and **RotationAngle**

In general, these parameters are not needed. They are for legacy support only. There are no equivalent 3D variables for positioning in 3D.

Example

2D explicit curve:

     A parabola    y = x^2

     CreateEquationSpline2("", "x^2", "", "-5", "5", False, 0, 0, 0, True, True)

2D parametric curve:

     A spiral   x = t\*sin(t); y = t\*cos(t)

     CreateEquationSpline2("t\*sin(t)", "t\*cos(t)", "", "0", "4\*pi", False, 0, 0, 0, True, True)

3D parametric curve:

     A helix   x = sin(t); y = cos(t); z = t/5

     CreateEquationSpline2("sin(t), "cos(t)", "t/5", "0", "30", False, 0, 0, 0, True, True)

Example

[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchSpline::GetEquationParameters2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters2.md)  
[ISketchSpline::SetEquationParameters2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters2.md)
