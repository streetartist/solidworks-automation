# DAssemblyDocEvents_RenamedDocumentNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenamedDocumentNotifyEventHandler`

Fired when saving an assembly document in which a renamed component file is referenced by other assembly documents.
Fired when saving an assembly document in which a renamed component file is referenced by other assembly documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_RenamedDocumentNotifyEventHandler( _
   ByRef RenamedDocumentInterface As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_RenamedDocumentNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_RenamedDocumentNotifyEventHandler( 
   ref System.object RenamedDocumentInterface
)
```

```

public delegate System.int DAssemblyDocEvents_RenamedDocumentNotifyEventHandler( 
   System.Object^% RenamedDocumentInterface
)
```

#### Parameters

*RenamedDocumentInterface*
:   [RenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md) object

Remarks

If developing a C++ application, use [swAssemblyRenamedDocumentNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

| To... | Use... |
| --- | --- |
| Rename a component file | [IModelDocExtension::RenameDocument](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.md) |
| Get whether an assembly document has renamed components | [IModelDocExtension::HasRenamedDocuments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.md) |

Example

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)  
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)  
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_RenamedDocumentNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenamedDocumentNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DPartDocEvents\_RenamedDocumentNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenamedDocumentNotifyEventHandler.md)
