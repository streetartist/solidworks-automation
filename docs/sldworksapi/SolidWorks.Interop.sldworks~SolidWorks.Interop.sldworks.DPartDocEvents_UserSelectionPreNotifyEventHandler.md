# DPartDocEvents_UserSelectionPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler`

Fired when an interactive user moves the cursor over or clicks a model view in a part document.
Fired when an interactive user moves the cursor over or clicks a model view in a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_UserSelectionPreNotifyEventHandler( _
   ByVal SelType As System.Integer _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_UserSelectionPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_UserSelectionPreNotifyEventHandler( 
   System.int SelType
)
```

```

public delegate System.int DPartDocEvents_UserSelectionPreNotifyEventHandler( 
   System.int SelType
)
```

#### Parameters

*SelType*
:   Type of object to be selected as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Remarks

Only selections made interactively fire this event; selections made programmatically are ignored by this event.

If developing a C++ application, use [swPartUserSelectionPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Disable Selection of Faces and Edges Using a Pre-Notify Event (VBA)](Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VB.htm)  
[Disable Selection of Faces and Edges Using a Pre-Notify Event (VB.NET)](Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VBNET.htm)  
[Disable Selection of Faces and Edges Using a Pre-Notify Event (C#)](Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_CSharp.htm)  
[Get Preselected Object (C#)](Get_Preselected_Object_Example_CSharp.htm)  
[Get Preselected Object (VB.NET)](Get_Preselected_Object_Example_VBNET.htm)  
[Get Preselected Object (VBA)](Get_Preselected_Object_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_UserSelectionPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DAssemblyDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DDrawingDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPreNotifyEventHandler.md)  
[ISelectionMgr::GetPreSelectedObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetPreSelectedObject.md)  
[DPartDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DAssemblyDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DAssemblyDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.md)
