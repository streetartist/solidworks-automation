# GetSketchSlot Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetSketchSlot`

Gets sketch slot with which this sketch point is associated.
Gets sketch slot with which this sketch point is associated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSlot() As SketchSlot
```

```

Dim instance As ISketchPoint
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

[Sketch slot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md) if the sketch point is associated with a sketch slot, or null if the sketch point is not associated with a sketch slot

Remarks

Sketch slot information is independent of the sketch point type.

A sketch slot is returned if it is associated with the sketch point regardless if the sketch point is an internal point or a user point.

Example

[Get Sketch Slot Using Sketch Point and Segment (C#)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_CSharp.htm)  
[Get Sketch Slot Using Sketch Point and Segment (VB.NET)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VBNET.htm)  
[Get Sketch Slot Using Sketch Point and Segment (VBA)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)
