# DSWPropertySheetEvents_CreateControlNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_CreateControlNotifyEventHandler`

Fired when the ActiveX control is created on the property page.
Fired when the ActiveX control is created on the property page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSWPropertySheetEvents_CreateControlNotifyEventHandler( _
   ByVal PageIndex As System.Integer, _
   ByVal ControlDispatch As System.Object _
) As System.Integer
```

```

Dim instance As New DSWPropertySheetEvents_CreateControlNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSWPropertySheetEvents_CreateControlNotifyEventHandler( 
   System.int PageIndex,
   System.object ControlDispatch
)
```

```

public delegate System.int DSWPropertySheetEvents_CreateControlNotifyEventHandler( 
   System.int PageIndex,
   System.Object^ ControlDispatch
)
```

#### Parameters

*PageIndex*
:   Index of property page within the property sheet for the add-in (see **Remarks**)

*ControlDispatch*
:   ActiveX control

#### Return Value

ActiveX control

Remarks

If PageIndex is the same index as returned by [ISWPropertySheet::AddActivePage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddActivePage.md), then ControlDispatch will contain the Dispatch pointer of the ActiveX control.

If developing a C++ application, use [swPropertySheetCreateControlNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSWPropertySheetEvents\_CreateControlNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_CreateControlNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
