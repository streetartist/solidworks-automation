# DPartDocEvents_RenamedDocumentNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenamedDocumentNotifyEventHandler`

Fired when saving a document in which a renamed part file is referenced by other documents.
Fired when saving a document in which a renamed part file is referenced by other documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_RenamedDocumentNotifyEventHandler( _
   ByRef RenamedDocumentInterface As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_RenamedDocumentNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_RenamedDocumentNotifyEventHandler( 
   ref System.object RenamedDocumentInterface
)
```

```

public delegate System.int DPartDocEvents_RenamedDocumentNotifyEventHandler( 
   System.Object^% RenamedDocumentInterface
)
```

#### Parameters

*RenamedDocumentInterface*
:   [RenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md) object

Remarks

If developing a C++ application, use [swPartRenamedDocumentNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_RenamedDocumentNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenamedDocumentNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DAssemblyDocEvents\_RenamedDocumentNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenamedDocumentNotifyEventHandler.md)
