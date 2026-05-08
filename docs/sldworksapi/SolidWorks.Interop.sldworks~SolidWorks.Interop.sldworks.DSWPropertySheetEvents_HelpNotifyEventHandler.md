# DSWPropertySheetEvents_HelpNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_HelpNotifyEventHandler`

Fired when the Help button is clicked on a property sheet.
Fired when the Help button is clicked on a property sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSWPropertySheetEvents_HelpNotifyEventHandler( _
   ByVal PageIndex As System.Integer _
) As System.Integer
```

```

Dim instance As New DSWPropertySheetEvents_HelpNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSWPropertySheetEvents_HelpNotifyEventHandler( 
   System.int PageIndex
)
```

```

public delegate System.int DSWPropertySheetEvents_HelpNotifyEventHandler( 
   System.int PageIndex
)
```

#### Parameters

*PageIndex*
:   Page index of the add-in's Help

Remarks

Your application should only display Help if you have added a Help page.

For add-ins, if PageIndex is the same as the value returned by [ISWPropertySheet::AddActivePage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddActivePage.md), then the add-in can display its Help.

If developing a C++ application, use [swPropertySheetHelpNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSWPropertySheetEvents\_HelpNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_HelpNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
