# DSldWorksEvents_FileOpenNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler`

Post-notifies the user program when an existing file has been opened.
Post-notifies the user program when an existing file has been opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileOpenNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileOpenNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileOpenNotify2EventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_FileOpenNotify2EventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the opened file

Remarks

You can use [ISldWorks::GetOpenDocumentByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md) or [ISldWorks::IGetOpenDocumentByName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md) with FileName to get a pointer to the newly opened document. Because it is possible to have a NULL active document when an add-in is notified by swAppFileOpenNotify2, use [ISldWorks::IGetOpenDocumentByName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md) instead of [ISldWorks::IActiveDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md).

This event is very similar to the now obsolete SldWorks events [FileOpenNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotifyEventHandler.md) event. The difference is that the SOLIDWORKS event FileOpenNotify2 is fired later in the process than the SOLIDWORKS event FileOpenNotify, so that if end-users respond to the event by opening a new part, then NewDocument, NewPart, NewAssembly, or NewDrawing2 is successful.

This event is sent to any application when a file is opened programmatically using [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md). Your application can detect the newly opened document by watching the the SOLIDWORKS events [ActiveModelDocChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.md) event.

With the exception of Parasolid files (that is, \*.x\_t, \*.x\_b), this event is not sent for the opening of non-native SOLIDWORKS files (that is, \*.igs, \*.dxf, and so on).  Opening non-native files is typically handled with the creation of a new SOLIDWORKS file (that is, \*.sldprt, \*.sldasm, \*.slddrw) and the subsequent construction of the foreign geometry within that file.

If developing a C++ application, use [swAppFileOpenNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileOpenNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
