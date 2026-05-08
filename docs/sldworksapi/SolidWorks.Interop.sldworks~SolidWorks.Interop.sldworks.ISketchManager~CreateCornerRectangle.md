# CreateCornerRectangle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCornerRectangle`

Creates a corner rectangle.
Creates a corner rectangle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCornerRectangle( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
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
Dim value As System.Object
 
value = instance.CreateCornerRectangle(X1, Y1, Z1, X2, Y2, Z2)
```

```

System.object CreateCornerRectangle( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

```

System.Object^ CreateCornerRectangle( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
) 
```

#### Parameters

*X1*
:   Upper-left X coordinate for point 1

*Y1*
:   Upper-left Y coordinate for point 1

*Z1*
:   Upper-left Z coordinate for point 1

*X2*
:   Lower-right X coordinate for point 2

*Y2*
:   Lower-right Y coordinate for point 2

*Z2*
:   Lower-right Z coordinate for point 2

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) that represent the edges created for this corner rectangle

Example

[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)  
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)  
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::Create3PointCenterRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCenterRectangle.md)  
[ISketchManager::Create3PointCornerRectangle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCornerRectangle.md)
