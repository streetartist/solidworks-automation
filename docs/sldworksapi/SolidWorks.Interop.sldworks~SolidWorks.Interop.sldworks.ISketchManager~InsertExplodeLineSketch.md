# InsertExplodeLineSketch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch`

Inserts or closes an explode line sketch in an exploded view.
Inserts or closes an explode line sketch in an exploded view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertExplodeLineSketch() As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
value = instance.InsertExplodeLineSketch()
```

```

System.bool InsertExplodeLineSketch()
```

```

System.bool InsertExplodeLineSketch(); 
```

#### Return Value

True if the explode line sketch is inserted or closed, false if not

Example

[Insert Explode Line Sketch and Route Line (VB.NET)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm)  
[Insert Explode Line Sketch and Route Line (VBA)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm)  
[Insert Explode Line Sketch and Jog Line (VB.NET)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm)  
[Insert Explode Line Sketch and Jog Line (VBA)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm)  
[Insert Explode Line Sketch and Jog Line (C#)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_CSharp.htm)  
[Insert Explode Line Sketch and Route Line (C#)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[IAssemblyDoc::AutoExplode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.md)  
[ISketch::InsertRouteLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~InsertRouteLine.md)  
[ISketchManager::Insert3DSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.md)
