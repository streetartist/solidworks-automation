# SketchRectangleAtAnyAngle Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangleAtAnyAngle`

Obsolete. Superseded by ISketchManager::Create3PointCornerRectangle.
Obsolete. Superseded by [ISketchManager::Create3PointCornerRectangle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCornerRectangle.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchRectangleAtAnyAngle( _
   ByVal Val1 As System.Double, _
   ByVal Val2 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal Val3 As System.Double, _
   ByVal Val4 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Val3x As System.Double, _
   ByVal Val3y As System.Double, _
   ByVal Z3 As System.Double, _
   ByVal Val5 As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Val1 As System.Double
Dim Val2 As System.Double
Dim Z1 As System.Double
Dim Val3 As System.Double
Dim Val4 As System.Double
Dim Z2 As System.Double
Dim Val3x As System.Double
Dim Val3y As System.Double
Dim Z3 As System.Double
Dim Val5 As System.Boolean
 
instance.SketchRectangleAtAnyAngle(Val1, Val2, Z1, Val3, Val4, Z2, Val3x, Val3y, Z3, Val5)
```

```

void SketchRectangleAtAnyAngle( 
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val3x,
   System.double Val3y,
   System.double Z3,
   System.bool Val5
)
```

```

void SketchRectangleAtAnyAngle( 
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val3x,
   System.double Val3y,
   System.double Z3,
   System.bool Val5
) 
```

#### Parameters

*Val1*
:   X value of corner 1

*Val2*
:   Y value of corner 1

*Z1*
:   Z value of corner 1

*Val3*
:   X value of corner 2 defining the bottom line from corner 1

*Val4*
:   Y value of corner 2 defining the bottom line from corner 1

*Z2*
:   Z value of corner 2 defining the bottom line from corner 1

*Val3x*
:   X value of corner 3; diagonal to corner 1

*Val3y*
:   Y value of corner 3; diagonal to corner 1

*Z3*
:   Z value of corner 3; diagonal to corner 1

*Val5*
:   True to add automatic constraints to the rectangle geometry, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangle.md)
