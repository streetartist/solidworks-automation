# Create3PointCornerRectangle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCornerRectangle`

Creates a 3-point corner rectangle at any angle.
Creates a 3-point corner rectangle at any angle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Create3PointCornerRectangle( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double, _
   ByVal Z3 As System.Double _
) As System.Object
```

```

Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim Z3 As System.Double
Dim value As System.Object
 
value = instance.Create3PointCornerRectangle(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
```

```

System.object Create3PointCornerRectangle( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3
)
```

```

System.Object^ Create3PointCornerRectangle( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3
) 
```

#### Parameters

*X1*
:   X coordinate of point 1

*Y1*
:   Y coordinate of point 1

*Z1*
:   Z coordinate of point 1

*X2*
:   X coordinate of point 2

*Y2*
:   Y coordinate of point 2

*Z2*
:   Z coordinate of point 2

*X3*
:   X coordinate of point 3

*Y3*
:   Y coordinate of point 3

*Z3*
:   Z coordinate of point 3

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) that represent the edges created for this corner rectangle

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::Create3PointCenterRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCenterRectangle.md)  
[ISketchManager::CreateCenterRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCenterRectangle.md)
