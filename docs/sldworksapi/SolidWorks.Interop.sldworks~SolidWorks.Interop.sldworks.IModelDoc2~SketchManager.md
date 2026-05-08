# SketchManager Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchManager`

Gets the sketch manager, which allows access to sketch-creation routines.
Gets the sketch manager, which allows access to sketch-creation routines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SketchManager As SketchManager
```

```

Dim instance As IModelDoc2
Dim value As SketchManager
 
value = instance.SketchManager
```

```

SketchManager SketchManager {get;}
```

```

property SketchManager^ SketchManager {
   SketchManager^ get();
}
```

#### Property Value

[Sketch manager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)

Example

[Dynamically Mirror Sketch Entities (VBA)](Dynamically_Mirror_Sketch_Entities_Example_VB.htm)  
[Get Sketch Entities (VBA)](Get_Sketch_Entities_Example_VB.htm)  
[Offset Selected Edges in Active Sketch (VBA)](Offset_Selected_Edges_in_Active_Sketch_Example_VB.htm)  
[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)  
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)  
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
