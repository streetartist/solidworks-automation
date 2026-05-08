# DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler`

Notifies the user program when the display title changes for an item in the FeatureManager design tree.
Notifies the user program when the display title changes for an item in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler( _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler( 
   System.string oldName,
   System.string NewName
)
```

```

public delegate System.int DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler( 
   System.String^ oldName,
   System.String^ NewName
)
```

#### Parameters

*oldName*
:   Previous display title

*NewName*
:   New display title

Remarks

Change the display title by using [IModelDocExtension::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle.md).

If developing a C++ application, use [swDrawingRenamedDisplayTitleNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_RenameDisplayTitleNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
