# AddAlongXDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongXDimension`

Projects and displays along the x axis a dimension between selected points in a 3D sketch.
Projects and displays along the x axis a dimension between selected points in a 3D sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddAlongXDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

```

Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension
 
value = instance.AddAlongXDimension(X, Y, Z)
```

```

DisplayDimension AddAlongXDimension( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

DisplayDimension^ AddAlongXDimension( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate of dimension text placement

*Y*
:   Y coordinate of dimension text placement

*Z*
:   Z coordinate of dimension text placement

#### Return Value

[IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

This method works only for 3D sketches in edit mode, and the display dimension is visible only when the sketch is in edit mode.

Example

[Add Along X Dimension to 3D Sketch (VBA)](Add_Along_X_Dimension_To_3D_Sketch_Example_VB.htm)  
[Add Along X Dimension to 3D Sketch (VB.NET)](Add_Along_X_Dimension_To_3D_Sketch_Example_VBNET.htm)  
[Add Along X Dimension to 3D Sketch (C#)](Add_Along_X_Dimension_To_3D_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::FullyDefineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~FullyDefineSketch.md)  
[ISketchManager::AddAlongYDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongYDimension.md)  
[ISketchManager::AddAlongZDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongZDimension.md)
