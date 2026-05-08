# IEnumSketchSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments`

Gets the sketch segments enumeration in this sketch.
Gets the sketch segments enumeration in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEnumSketchSegments() As EnumSketchSegments
```

```

Dim instance As ISketch
Dim value As EnumSketchSegments
 
value = instance.IEnumSketchSegments()
```

```

EnumSketchSegments IEnumSketchSegments()
```

```

EnumSketchSegments^ IEnumSketchSegments(); 
```

#### Return Value

[Sketch segments enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.md)

Remarks

Sketch segments include line, arc, spline, parabola, and ellipse entities.

Example

[Select All Sketch Segments (C++)](Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md)  
[ISketch::GetSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.md)  
[ISketch::IEnumSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.md)
