# GetEquationParameters2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters2`

Gets an equation-driven curve's parameters.
Gets an equation-driven curve's parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEquationParameters2( _
   ByRef XExpression As System.String, _
   ByRef YExpression As System.String, _
   ByRef ZExpression As System.String, _
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
Dim XExpression As System.String
Dim YExpression As System.String
Dim ZExpression As System.String
Dim RangeStart As System.Double
Dim RangeEnd As System.Double
Dim IsAngleRange As System.Boolean
Dim RotationAngle As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim LockStart As System.Boolean
Dim LockEnd As System.Boolean
Dim value As System.Boolean
 
value = instance.GetEquationParameters2(XExpression, YExpression, ZExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

```

System.bool GetEquationParameters2( 
   out System.string XExpression,
   out System.string YExpression,
   out System.string ZExpression,
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

System.bool GetEquationParameters2( 
   [Out] System.String^ XExpression,
   [Out] System.String^ YExpression,
   [Out] System.String^ ZExpression,
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

*XExpression*
:   Equation for x

*YExpression*
:   Equation for y

*ZExpression*
:   Equation for z

*RangeStart*
:   Start value of x

*RangeEnd*
:   Start value of y

*IsAngleRange*
:   True if the range and x value represent an angle (in radians), false if not

*RotationAngle*
:   Rotation angle (in radians) for the curve

*XOffset*
:   Offset in x for f(x), where x = 0

*YOffset*
:   Offset in y for f(x), where x = 0

*LockStart*
:   True to lock the start point (RangeStart) of the curve, false to not

*LockEnd*
:   True to lock the end point (RangeEnd) of the curve, false to not

#### Return Value

True if the equation-driven curve's parameters are returned, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[SketchManager::CreateEquationSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline2.md)  
[ISketchSpline::SetEquationParameters2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters2.md)
