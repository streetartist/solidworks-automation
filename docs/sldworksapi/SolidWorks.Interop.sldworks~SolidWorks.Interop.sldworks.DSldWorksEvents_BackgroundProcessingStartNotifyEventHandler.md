# DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler`

Notifies the user program when background processing has started.
Notifies the user program when background processing has started.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Drawing file for which background processing has started

Remarks

If developing a C++ application, use [swAppBackgroundProcessingStartNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Fire Notifications for Background Processing Events (VBA)](Fire_Notification_for_Background_Processing_Events_Example_VB.htm)  
[Fire Notifications for Background Processing Events (VB.NET)](Fire_Notification_for_Background_Processing_Events_Example_VBNET.htm)  
[Fire Notifications for Background Processing Events (C#)](Fire_Notification_for_Background_Processing_Events_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_BackgroundProcessingStartNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
