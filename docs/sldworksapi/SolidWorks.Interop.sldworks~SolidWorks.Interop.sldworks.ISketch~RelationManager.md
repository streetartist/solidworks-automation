# RelationManager Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~RelationManager`

Gets the sketch relation manager.
Gets the sketch relation manager.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property RelationManager As SketchRelationManager
```

```

Dim instance As ISketch
Dim value As SketchRelationManager
 
value = instance.RelationManager
```

```

SketchRelationManager RelationManager {get;}
```

```

property SketchRelationManager^ RelationManager {
   SketchRelationManager^ get();
}
```

#### Property Value

[Sketch relation manager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)

Example

[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)  
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)  
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
