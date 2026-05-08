# GetSketchTextSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments`

Gets the sketch segments that represent the selected text in the sketch.
Gets the sketch segments that represent the selected text in the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchTextSegments() As System.Object
```

```

Dim instance As ISketch
Dim value As System.Object
 
value = instance.GetSketchTextSegments()
```

```

System.object GetSketchTextSegments()
```

```

System.Object^ GetSketchTextSegments(); 
```

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the selected text in this sketch

Example

[Get Sketch Entities (VBA)](Get_Sketch_Entities_Example_VB.htm)  
[Replace Sketch Text (VBA)](Replace_Sketch_Text_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IEnumSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.md)  
[ISketch::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md)  
[ISketch::IEnumSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md)
