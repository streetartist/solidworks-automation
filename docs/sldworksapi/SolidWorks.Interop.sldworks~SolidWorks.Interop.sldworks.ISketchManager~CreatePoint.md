# CreatePoint Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint`

Creates a sketch point in the active 2D or 3D sketch.
Creates a sketch point in the active 2D or 3D sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As SketchPoint
```

```

Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As SketchPoint
 
value = instance.CreatePoint(X, Y, Z)
```

```

SketchPoint CreatePoint( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

SketchPoint^ CreatePoint( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X location of the point

*Y*
:   Y location of the point

*Z*
:   Z location of the point; ignored for 2D sketches

#### Return Value

Newly created [sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

Remarks

This method creates a point in the active 2D or 3D sketch. If a sketch is not active, the point is not created and NULL is returned. Use [ISketchManager::ActiveSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.md) to check to see if the sketch is active.

[ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) and [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md) increase performance during entity creation by adding entities directly to the SOLIDWORKS database. ISketchManager::AddToDB also avoids inferencing.

Example

[Create Sketch Point (VBA)](Create_Sketch_Point_Example_VB.htm)  
[Create Sketch Point (VB.NET)](Create_Sketch_Point_Example_VBNET.htm)  
[Create Sketch Point (C#)](Create_Sketch_Point_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
