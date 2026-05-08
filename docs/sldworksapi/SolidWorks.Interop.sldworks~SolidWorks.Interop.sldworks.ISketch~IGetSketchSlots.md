# IGetSketchSlots Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchSlots`

Gets the sketch slots in this sketch.
Gets the sketch slots in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchSlots( _
   ByVal Count As System.Integer _
) As SketchSlot
```

```

Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchSlot
 
value = instance.IGetSketchSlots(Count)
```

```

SketchSlot IGetSketchSlots( 
   System.int Count
)
```

```

SketchSlot^ IGetSketchSlots( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch slots in this sketch

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch slots](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling htis method, call [ISketch::GetSketchSlotCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlotCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchSlots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlots.md)
