# GetEquationParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters`

Obsolete. Superseded by ISketchSpline::GetEquationParameters2.
Obsolete. Superseded by [ISketchSpline::GetEquationParameters2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEquationParameters( _
   ByRef YExpression As System.String, _
   ByRef RangeStart As System.Double, _
   ByRef RangeEnd As System.Double, _
   ByRef IsAngleRange As System.Boolean, _
   ByRef RotationAngle As System.Double, _
   ByRef XOffset As System.Double, _
   ByRef YOffset As System.Double, _
   ByRef LockStart As System.Boolean, _
   ByRef LockEnd As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchSpline
Dim YExpression As System.String
Dim RangeStart As System.Double
Dim RangeEnd As System.Double
Dim IsAngleRange As System.Boolean
Dim RotationAngle As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim LockStart As System.Boolean
Dim LockEnd As System.Boolean
Dim value As System.Boolean
 
value = instance.GetEquationParameters(YExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

```

System.bool GetEquationParameters( 
   out System.string YExpression,
   out System.double RangeStart,
   out System.double RangeEnd,
   out System.bool IsAngleRange,
   out System.double RotationAngle,
   out System.double XOffset,
   out System.double YOffset,
   out System.bool LockStart,
   out System.bool LockEnd
)
```

```

System.bool GetEquationParameters( 
   [Out] System.String^ YExpression,
   [Out] System.double RangeStart,
   [Out] System.double RangeEnd,
   [Out] System.bool IsAngleRange,
   [Out] System.double RotationAngle,
   [Out] System.double XOffset,
   [Out] System.double YOffset,
   [Out] System.bool LockStart,
   [Out] System.bool LockEnd
) 
```

#### Parameters

*YExpression*
:   Equation for y (see **Remarks**)

*RangeStart*
:   Start value of x (see **Remarks**)

*RangeEnd*
:   End value of x (see **Remarks**)

*IsAngleRange*
:   True if the range and x value represent an angle (in radians), false if not

*RotationAngle*
:   Rotation angle (in radians) for the curve

*XOffset*
:   Offset in x for f(x), where x = 0 (see **Remarks**)

*YOffset*
:   Offset in y for f(x), where x = 0 (see **Remarks**)

*LockStart*
:   True to lock the start point (RangeStart) of the curve, false to not

*LockEnd*
:   True to lock the end point (RangeEnd) of the curve, false to not

#### Return Value

True if the equation-driven curve's parameters are returned, false if not

Remarks

**YExpression:**

  Any function that you can define as a 2D function in the following form:

y-in-the-sketch = f(x-in-the-sketch)

  will appear as a curve in the sketch. For example:

y = sin(x)

**RangeStart** and **RangeEnd**

You cannot specify string values for RangeStart and RangeEnd; you must specify double values.

**XOffset:**

  In the equation:

y = sin(x) [x=0 to 2Pi]

  the start point (0,0) is moved by XOffset in the x direction.

**YOffset:**

In the equation:

y = sin(x) [x=0 to 2Pi]

  the start point (0,0) is moved by YOffset in the y direction.

Example

[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::SetEquationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters.md)  
[ISketchManager::CreateEquationSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline.md)
