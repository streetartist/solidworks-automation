# IEnumSketchTextSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments`

Gets the sketch segments enumeration for the selected text in this sketch.
Gets the sketch segments enumeration for the selected text in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEnumSketchTextSegments() As EnumSketchSegments
```

```

Dim instance As ISketch
Dim value As EnumSketchSegments
 
value = instance.IEnumSketchTextSegments()
```

```

EnumSketchSegments IEnumSketchTextSegments()
```

```

EnumSketchSegments^ IEnumSketchTextSegments(); 
```

#### Return Value

[Sketch segments enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.md)  
[ISketch::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md)  
[ISketch::IEnumSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md)
