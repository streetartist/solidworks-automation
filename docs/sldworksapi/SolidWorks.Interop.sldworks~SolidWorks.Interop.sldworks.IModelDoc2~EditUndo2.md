# EditUndo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUndo2`

Undoes the specified number of actions in the active SOLIDWORKS session.
Undoes the specified number of actions in the active SOLIDWORKS session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditUndo2( _
   ByVal Steps As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Steps As System.Integer
 
instance.EditUndo2(Steps)
```

```

void EditUndo2( 
   System.int Steps
)
```

```

void EditUndo2( 
   System.int Steps
) 
```

#### Parameters

*Steps*
:   Number of actions to undo

Example

[Undo Feature and Fire Undo Post-Notify Event (VBA)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Undo Feature and Fire Undo Post-Notify Event (VB.NET)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Feature and Fire Undo Post-Notify Event (C#)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.md)  
[IModelDoc2::EditRedo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2.md)  
[IModelDoc2::SketchUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchUndo.md)  
[IModelDocExtension::FinishRecordingUndoObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject.md)  
[IModelDocExtension::StartRecordingUndoObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject.md)  
[IModelDoc2::SketchUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchUndo.md)  
[DAssemblyDocEvents\_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UndoPostNotifyEventHandler.md)  
[DDrawingDocEvents\_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UndoPostNotifyEventHandler.md)  
[DPartDocEvents\_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UndoPostNotifyEventHandler.md)
