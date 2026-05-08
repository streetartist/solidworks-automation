# DSldWorksEvents_DocumentLoadNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotify2EventHandler`

Post-notifies the user program when a SOLIDWORKS document is loaded.
Post-notifies the user program when a SOLIDWORKS document is loaded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_DocumentLoadNotify2EventHandler( _
   ByVal docTitle As System.String, _
   ByVal docPath As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_DocumentLoadNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_DocumentLoadNotify2EventHandler( 
   System.string docTitle,
   System.string docPath
)
```

```

public delegate System.int DSldWorksEvents_DocumentLoadNotify2EventHandler( 
   System.String^ docTitle,
   System.String^ docPath
)
```

#### Parameters

*docTitle*
:   Document title

*docPath*
:   Document path

Remarks

This event is fired for documents referenced by assemblies and drawings. Client code should expect multiple calls to this event handler when an assembly or drawing is loaded.

If developing a C++ application, use [swAppDocumentLoadNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_DocumentLoadNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
