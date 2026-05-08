# SetCoords Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~SetCoords`

Sets the location of this sketch point.
Sets the location of this sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCoords( _
   ByVal Xx As System.Double, _
   ByVal Yy As System.Double, _
   ByVal Zz As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchPoint
Dim Xx As System.Double
Dim Yy As System.Double
Dim Zz As System.Double
Dim value As System.Boolean
 
value = instance.SetCoords(Xx, Yy, Zz)
```

```

System.bool SetCoords( 
   System.double Xx,
   System.double Yy,
   System.double Zz
)
```

```

System.bool SetCoords( 
   System.double Xx,
   System.double Yy,
   System.double Zz
) 
```

#### Parameters

*Xx*
:   X component of the direction vector

*Yy*
:   Y component of the direction vector

*Zz*
:   Z component of the direction vector

#### Return Value

True if the coordinates are successfully set, false if not

Remarks

When setting new coordinate values to a sketch point, this method adheres to any constraints that are active in the sketch. If the sketch point is an end point of a sketch line that is constrained to be horizontal, then the values are adjusted according to that constraint.

To set the coordinates of a sketch point on a spline, the location of the sketch point must already exist on the spline. You cannot use this method to create a new sketch point that is not on the spline.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::GetCoords Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetCoords.md)  
[ISketchPoint::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~X.md)  
[ISketchPoint::Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Y.md)  
[ISketchPoint::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Z.md)
