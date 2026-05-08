# DSldWorksEvents_EndRecordNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_EndRecordNotifyEventHandler`

Notifies the user program when a macro recording has ended, including if the user cancels the recording (i.e., the user cancels out of the Save As dialog and says No to the SOLIDWORKS Continue recording? dialog).
Notifies the user program when a macro recording has ended, including if the user cancels the recording (i.e., the user cancels out of the Save As dialog and says No to the SOLIDWORKS Continue recording? dialog).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_EndRecordNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSldWorksEvents_EndRecordNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_EndRecordNotifyEventHandler()
```

```

public delegate System.int DSldWorksEvents_EndRecordNotifyEventHandler();
```

Remarks

This event informs the user program when a macro recording has stopped so that the add-in can add its own cleanup code to a macro using [ISldWorks::RecordLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.md), [ISldWorks::RecordLineCSharp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineCSharp.md), or [ISldWorks::RecordLineVBnet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineVBnet.md). This is useful if the add-in has been recording its own lines of code to the macro and needs to clean up variables that have been used.

The SOLIDWORKS event [BeginRecordNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginRecordNotifyEventHandler.md) is sent when the macro recording is starting.

These events are not sent when the macro is paused and restarted. SldWorks::RecordLine, ISldWorks::RecordLineCSharp, or ISldWorks::RecordLineVBnet can be used at any time, regardless of whether a macro is currently recording or not. Even if no macro is running, writing to the journal file occurs.

If developing a C++ application, use [swAppEndRecordNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Record Macros (C#)](Record_Macros_Example_CSharp.htm)  
[Record Macros (VB.NET)](Record_Macros_Example_VBNET.htm)  
[Record Macros (VBA)](Record_Macros_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_EndRecordNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_EndRecordNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
