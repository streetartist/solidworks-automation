# Insert3DSketch Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch`

Inserts a new 3D sketch in a model or closes the active sketch.
Inserts a new 3D sketch in a model or closes the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Insert3DSketch( _
   ByVal UpdateEditRebuild As System.Boolean _
) 
```

```

Dim instance As ISketchManager
Dim UpdateEditRebuild As System.Boolean
 
instance.Insert3DSketch(UpdateEditRebuild)
```

```

void Insert3DSketch( 
   System.bool UpdateEditRebuild
)
```

```

void Insert3DSketch( 
   System.bool UpdateEditRebuild
) 
```

#### Parameters

*UpdateEditRebuild*
:   True if you want to edit and rebuild, false if not

Example

[Insert Explode Line Sketch and Jog Line (VB.NET)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm)  
[Insert Explode Line Sketch and Jog Line (VBA)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm)  
[Insert Explode Line Sketch and Jog Line (C#)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::AddToDB Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md)  
[ISketchManager::CreateSketchPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchPlane.md)  
[ISketchManager::DisplayWhenAdded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md)  
[ISketchManager::InsertExplodeLineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.md)  
[ISketchSegment::JogLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~JogLine.md)
