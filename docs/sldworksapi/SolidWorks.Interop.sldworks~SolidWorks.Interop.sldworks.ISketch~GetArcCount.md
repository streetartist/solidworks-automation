# GetArcCount Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetArcCount`

Gets the number of arcs in the sketch.
Gets the number of arcs in the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcCount() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetArcCount()
```

```

System.int GetArcCount()
```

```

System.int GetArcCount(); 
```

#### Return Value

Number of arcs in the sketch

Remarks

Call this method before [ISketch::IGetArcs2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetArcs2.md) to determine the size of the array for that method.

Example

[Get Arcs in Sketch (VBA)](Get_Arcs_in_Sketch_Example_VB.htm)  
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetArcs2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetArcs2.md)  
[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)
