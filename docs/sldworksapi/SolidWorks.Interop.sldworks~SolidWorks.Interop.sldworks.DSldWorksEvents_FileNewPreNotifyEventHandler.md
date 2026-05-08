# DSldWorksEvents_FileNewPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewPreNotifyEventHandler`

Fired before a new document is created either using the SOLIDWORKS API or the SOLIDWORKS user-interface.
Fired before a new document is created either using the SOLIDWORKS API or the SOLIDWORKS user-interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileNewPreNotifyEventHandler( _
   ByVal DocType As System.Integer, _
   ByVal TemplateName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileNewPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileNewPreNotifyEventHandler( 
   System.int DocType,
   System.string TemplateName
)
```

```

public delegate System.int DSldWorksEvents_FileNewPreNotifyEventHandler( 
   System.int DocType,
   System.String^ TemplateName
)
```

#### Parameters

*DocType*
:   Document type as defined by [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*TemplateName*
:   Template path name or file extension

Remarks

Creating a new document using the SOLIDWORKS user-interface includes:

- Clicking a document-type button on the New SOLIDWORKS Document dialog.
- inserting a new component (part or assembly).

NOTE: This event is not raised when creating split parts.

You can cancel the creation of a new document by returning S\_FALSE(1) from the event handler.

If developing a C++ application, use [swAppFileNewPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileNewPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISldWorks::SetNewFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetNewFilename.md)
