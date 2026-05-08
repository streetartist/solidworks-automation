# DAssemblyDocEvents_EndInContextEditNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_EndInContextEditNotifyEventHandler`

Notifies the application that the user is done editing an assembly component within the context of the assembly (inside the assembly document window).
Notifies the application that the user is done editing an assembly component within the context of the assembly (inside the assembly document window).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_EndInContextEditNotifyEventHandler( _
   ByVal docBeingEdited As System.Object, _
   ByVal DocType As System.Integer _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_EndInContextEditNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_EndInContextEditNotifyEventHandler( 
   System.object docBeingEdited,
   System.int DocType
)
```

```

public delegate System.int DAssemblyDocEvents_EndInContextEditNotifyEventHandler( 
   System.Object^ docBeingEdited,
   System.int DocType
)
```

#### Parameters

*docBeingEdited*
:   File name of the component document being edited

*DocType*
:   Type of component document as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

Remarks

If developing a C++ application, use [swAssemblyEndInContextEditNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_EndInContextEditNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_EndInContextEditNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
