# DSldWorksEvents_PropertySheetCreateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PropertySheetCreateNotifyEventHandler`

Notifies the user program when an exported ISWPropertySheet is created so that the application can add pages to it.
Notifies the user program when an exported [ISWPropertySheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md) is created so that the application can add pages to it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_PropertySheetCreateNotifyEventHandler( _
   ByVal Sheet As System.Object, _
   ByVal sheetType As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_PropertySheetCreateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_PropertySheetCreateNotifyEventHandler( 
   System.object Sheet,
   System.int sheetType
)
```

```

public delegate System.int DSldWorksEvents_PropertySheetCreateNotifyEventHandler( 
   System.Object^ Sheet,
   System.int sheetType
)
```

#### Parameters

*Sheet*
:   [Property sheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.md)

*sheetType*
:   Type of the property sheet as defined in [swPropSheetType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropSheetType_e.html)

Remarks

If developing a C++ application, use [swAppPropertySheetCreateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_PropertySheetCreateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_PropertySheetCreateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
