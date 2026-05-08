# DSldWorksEvents_FileNewNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler`

Post-notifies the user program when a new file is created.
Post-notifies the user program when a new file is created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileNewNotify2EventHandler( _
   ByVal NewDoc As System.Object, _
   ByVal DocType As System.Integer, _
   ByVal TemplateName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileNewNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileNewNotify2EventHandler( 
   System.object NewDoc,
   System.int DocType,
   System.string TemplateName
)
```

```

public delegate System.int DSldWorksEvents_FileNewNotify2EventHandler( 
   System.Object^ NewDoc,
   System.int DocType,
   System.String^ TemplateName
)
```

#### Parameters

*NewDoc*
:   New document

*DocType*
:   Type of document as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*TemplateName*
:   Template name of the new document

Remarks

If your add-in wants to use the Dispatch pointer to the new document, then your add-in must increment the reference count using AddRef. When your add-in is done with the new document, it must decrement the reference count using Release.

If developing a C++ application, use [swAppFileNewNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileNewNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
