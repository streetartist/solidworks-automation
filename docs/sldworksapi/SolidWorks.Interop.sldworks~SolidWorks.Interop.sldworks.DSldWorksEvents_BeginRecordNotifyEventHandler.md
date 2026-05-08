# DSldWorksEvents_BeginRecordNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginRecordNotifyEventHandler`

Notifies the user program when a macro recording has started.
Notifies the user program when a macro recording has started.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_BeginRecordNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSldWorksEvents_BeginRecordNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_BeginRecordNotifyEventHandler()
```

```

public delegate System.int DSldWorksEvents_BeginRecordNotifyEventHandler();
```

Remarks

This event informs the user program when a macro recording has started so that the add-in can add its own initialization code to a macro using [ISldWorks::RecordLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.md), [ISldWorks::RecordLineCSharp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineCSharp.md), or [ISldWorks::RecordLineVBnet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineVBnet.md). This is useful if the add-in is recording its own lines of code to the macro and needs to declare and initialize variables.  

The SOLIDWORKS event [EndRecordNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_EndRecordNotifyEventHandler.md) is sent when the macro recording is stopping.

These events are not sent when the macro is paused and restarted. ISldWorks::RecordLine, ISldWorks::RecordLineCSharp, or ISldWorks::RecordLineVBnet can be used at any time, regardless of whether a macro is currently recording or not. Even if no macro is running, writing to the SOLIDWORKS journal file occurs.

If developing a C++ application, use [swAppBeginRecordNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Record Macros (C#)](Record_Macros_Example_CSharp.htm)  
[Record Macros (VB.NET)](Record_Macros_Example_VBNET.htm)  
[Record Macros (VBA)](Record_Macros_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_BeginRecordNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginRecordNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
