# ActiveSketch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch`

Gets the active sketch.
Gets the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ActiveSketch As Sketch
```

```

Dim instance As ISketchManager
Dim value As Sketch
 
value = instance.ActiveSketch
```

```

Sketch ActiveSketch {get;}
```

```

property Sketch^ ActiveSketch {
   Sketch^ get();
}
```

#### Property Value

Active [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Example

[Constrain Sketch (VBA)](Constrain_Sketch_Example_VB.htm)  
[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)  
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)  
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)  
[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
