# EditRedo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2`

Repeats the specified number of actions in this SOLIDWORKS session.
Repeats the specified number of actions in this SOLIDWORKS session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditRedo2( _
   ByVal Steps As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Steps As System.Integer
 
instance.EditRedo2(Steps)
```

```

void EditRedo2( 
   System.int Steps
)
```

```

void EditRedo2( 
   System.int Steps
) 
```

#### Parameters

*Steps*
:   Number of actions to repeat

Example

[Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm)  
[Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)](Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VBNET.htm)  
[Fire Undo and Redo Pre- and Post-notifications in Part Document (VBA)](Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VB6.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.md)  
[IModelDoc2::SketchUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchUndo.md)  
[IModelDocExtension::FinishRecordingUndoObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject.md)  
[IModelDocExtension::StartRecordingUndoObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject.md)  
[IModelDoc2::EditUndo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUndo2.md)
