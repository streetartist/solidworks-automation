# DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler`

Post-notifies the user program when the weldment cut list in this part is updated.
Post-notifies the user program when the weldment cut list in this part is updated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swPartWeldmentCutListUpdatePostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Update Weldment Cut List and Fire Post-Notify Event (VBA)](Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VB.htm)  
[Update Weldment Cut List and Fire Post-Notify Event (VB.NET)](Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VBNET.htm)  
[Update Weldment Cut List and Fire Post-Notify Event (C#)](Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_WeldmentCutListUpdatePostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
