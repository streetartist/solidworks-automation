# DDrawingDocEvents_ActivateSheetPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActivateSheetPreNotifyEventHandler`

Notifies the user program before activating the drawing sheet.
Notifies the user program before activating the drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_ActivateSheetPreNotifyEventHandler( _
   ByVal SheetName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_ActivateSheetPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_ActivateSheetPreNotifyEventHandler( 
   System.string SheetName
)
```

```

public delegate System.int DDrawingDocEvents_ActivateSheetPreNotifyEventHandler( 
   System.String^ SheetName
)
```

#### Parameters

*SheetName*
:   Name of the drawing sheet

Remarks

If developing a C++ application, use [swDrawingActivateSheetPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Example

[Fire Notification When Activating a Sheet (VBA)](Fire_Notification_When_Sheet_is_Activated_Example_VB.htm)  
[Fire Notification When Activating a Sheet (VB.NET)](Fire_Notification_When_Sheet_Is_Activated_Example_VBNET.htm)  
[Fire Notification When Activating a Sheet (C#)](Fire_Notification_When_Sheet_Is_Activated_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_ActivateSheetPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActivateSheetPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
