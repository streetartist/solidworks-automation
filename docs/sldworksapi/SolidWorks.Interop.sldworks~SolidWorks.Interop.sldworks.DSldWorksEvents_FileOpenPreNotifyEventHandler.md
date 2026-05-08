# DSldWorksEvents_FileOpenPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenPreNotifyEventHandler`

Pre-notifies the user program of a FileOpenNotify2 event.
Pre-notifies the user program of a [FileOpenNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md) event.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileOpenPreNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileOpenPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileOpenPreNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_FileOpenPreNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Full path and name of file to open

Remarks

This event is only fired when opening these SOLIDWORKS files: parts, drawings, and assemblies. It is not fired when opening files like templates, translator files, and so on.

This event is fired before SOLIDWORKS begins loading the file. A SOLIDWORKS file can be opened in many ways; for example, File, Open in the user interface, [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) in the API, Load Model from a Detached drawing, Lightweight component being resolved, and so on. This event is fired in all of these cases.

If you want to allow SOLIDWORKS to open the file, return S\_OK (or 0) from the handler. If you do not want to allow SOLIDWORKS to open the file, return S\_false (or any code other than S\_OK) from the handler.

The event that occurs after this event is [DocumentLoadNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotifyEventHandler.md).

If developing a C++ application, use [swAppFileOpenPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileOpenPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
