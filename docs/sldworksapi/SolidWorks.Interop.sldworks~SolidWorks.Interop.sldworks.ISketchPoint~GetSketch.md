# GetSketch Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetSketch`

Gets the sketch for the current sketch point.
Gets the sketch for the current sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketch() As Sketch
```

```

Dim instance As ISketchPoint
Dim value As Sketch
 
value = instance.GetSketch()
```

```

Sketch GetSketch()
```

```

Sketch^ GetSketch(); 
```

#### Return Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

You can use the [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) interface for extracting information about geometry in the sketch.

Example

[Get Sketch Point's View (VBA)](Get_Sketch_Point_s_View_Example_VB.htm)  
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)  
[Redirect Spotlight (VBA)](Redirect_Spotlight_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)
