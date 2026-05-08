# StartRecordingUndoObject Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject`

Starts recording the SOLIDWORKS Undo object.
Starts recording the SOLIDWORKS Undo object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub StartRecordingUndoObject() 
```

```

Dim instance As IModelDocExtension
 
instance.StartRecordingUndoObject()
```

```

void StartRecordingUndoObject()
```

```

void StartRecordingUndoObject(); 
```

Remarks

To add an object with the name UndoObjectName to the SOLIDWORKS Undo list, place the SOLIDWORKS API calls between IModelDocExtension::StartRecordingUndoObject and [IModelDocExtension::FinishRecordingUndoObject2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject2.md):

For example, assume that your application creates a complex gear that requires many SOLIDWORKS API calls and you would like your SOLIDWORKS user to be able to undo that gear from the user interface at a later time. Your application can create an Undo object by calling:

1. IModelDocExtension::StartRecordingUndoObject
2. SOLIDWORKS API calls that create the gear
3. IModelDocExtension::FinishRecordingUndoObject2 with MakeHidden = False

Now assume that your application performs many temporary operations that you do not want your users to see in the SOLIDWORKS Undo list, because they are not essential to the modeling and design process. For this case, your application can place the non-essential SOLIDWORKS API calls between IModelDocExtension::StartRecordingUndoObject and IModelDocExtension::FinishRecordingUndoObject2 with MakeHidden = True. The Undo object is still added to the SOLIDWORKS Undo list, but the user does not see it in the list.

****WARNING**:** If your application hides an Undo object in the Undo list by setting MakeHidden = True and the Undo object is the first item in the SOLIDWORKS Undo list, then SOLIDWORKS discards the Undo object from the Undo list. If this happens, the SOLIDWORKS API calls in this Undo object cannot be undone.

Similarly, if the last item to be redone is a hidden API Undo object, then SOLIDWORKS discards it, and the SOLIDWORKS API calls cannot be redone.

Only SOLIDWORKS operations that support Undo are undone. Both SOLIDWORKS API and non-API operations are undone.

Example

[Create Hidden Undo Object (VBA)](Create_Multiple_Undo_Command_Example_VB.htm)  
[Create Hidden Undo Object (VB.NET)](Create_Multiple_Undo_Command_Example_VBNET.htm)  
[Create Hidden Undo Object (C#)](Create_Multiple_Undo_Command_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.md)  
[IModelDoc2::EditRedo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2.md)
