# FinishRecordingUndoObject Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject`

Obsolete. Superseded by IModelDocExtension::FinishRecordingUndoObject2.
Obsolete. Superseded by [IModelDocExtension::FinishRecordingUndoObject2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FinishRecordingUndoObject( _
   ByVal UndoObjectName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim UndoObjectName As System.String
Dim value As System.Boolean
 
value = instance.FinishRecordingUndoObject(UndoObjectName)
```

```

System.bool FinishRecordingUndoObject( 
   System.string UndoObjectName
)
```

```

System.bool FinishRecordingUndoObject( 
   System.String^ UndoObjectName
) 
```

#### Parameters

*UndoObjectName*
:   String to appear in SOLIDWORKS Undo list

#### Return Value

True if recording of the SOLIDWORKS Undo object ends, false if not

Remarks

Place [IModelDocExtension::StartRecordingUndoObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject.md) at the beginning and this method at the end of any SOLIDWORKS API calls in your application that you want your user to undo as a group.

For example, if your application creates a complex gear that requires many SOLIDWORKS API calls, place IModelDocExtension::StartRecordingUndoObject and this method around the SOLIDWORKS API calls that create that gear. Then your user need only select the string specified for UndoObjectName in the SOLIDWORKS Undo list to undo all of the SOLIDWORKS API calls that created the gear.

NOTE: Only SOLIDWORKS operations that support Undo will be undone. Both SOLIDWORKS API and non-API operations are undone.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.md)  
[IModelDoc2::EditUndo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUndo2.md)  
[IModelDoc2::EditRedo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2.md)
