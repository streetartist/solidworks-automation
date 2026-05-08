# GetSketchSlotCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlotCount`

Gets the number of sketch slots in this sketch.
Gets the number of sketch slots in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSlotCount() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetSketchSlotCount()
```

```

System.int GetSketchSlotCount()
```

```

System.int GetSketchSlotCount(); 
```

#### Return Value

Number of sketch slots in this sketch

Remarks

Call this method before calling [ISketch::IGetSketchSlots](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchSlots.md) to determine the size of the array for that method.

Example

[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchSlots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlots.md)
