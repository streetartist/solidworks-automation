# SetEquationParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters`

Obsolete. Superseded by ISketchSpline::SetEquationParameters2.
Obsolete. Superseded by [ISketchSpline::SetEquationParameters2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetEquationParameters( _
   ByVal YExpression As System.String, _
   ByVal RangeStart As System.Double, _
   ByVal RangeEnd As System.Double, _
   ByVal IsAngleRange As System.Boolean, _
   ByVal RotationAngle As System.Double, _
   ByVal XOffset As System.Double, _
   ByVal YOffset As System.Double, _
   ByVal LockStart As System.Boolean, _
   ByVal LockEnd As System.Boolean _
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
 
value = instance.SetEquationParameters(YExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

```

System.bool SetEquationParameters( 
   System.string YExpression,
   System.double RangeStart,
   System.double RangeEnd,
   System.bool IsAngleRange,
   System.double RotationAngle,
   System.double XOffset,
   System.double YOffset,
   System.bool LockStart,
   System.bool LockEnd
)
```

```

System.bool SetEquationParameters( 
   System.String^ YExpression,
   System.double RangeStart,
   System.double RangeEnd,
   System.bool IsAngleRange,
   System.double RotationAngle,
   System.double XOffset,
   System.double YOffset,
   System.bool LockStart,
   System.bool LockEnd
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

True if the equation-driven curve's parameters are set, false if not

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
[ISketchManager::CreateEquationSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline.md)  
[ISketchSpline::GetEquationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters.md)
