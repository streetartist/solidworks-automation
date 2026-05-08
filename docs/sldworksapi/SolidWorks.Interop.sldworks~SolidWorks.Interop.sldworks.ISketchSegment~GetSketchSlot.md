# GetSketchSlot Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchSlot`

Gets sketch slot with which this sketch segment is associated.
Gets sketch slot with which this sketch segment is associated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSlot() As SketchSlot
```

```

Dim instance As ISketchSegment
Dim value As SketchSlot
 
value = instance.GetSketchSlot()
```

```

SketchSlot GetSketchSlot()
```

```

SketchSlot^ GetSketchSlot(); 
```

#### Return Value

[Sketch slot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md) if the sketch segment is associated with a sketch slot, or null if the sketch segment is not associated with a sketch slot

Example

[Get Sketch Slot Using Sketch Point and Segment (C#)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_CSharp.htm)  
[Get Sketch Slot Using Sketch Point and Segment (VB.NET)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VBNET.htm)  
[Get Sketch Slot Using Sketch Point and Segment (VBA)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
