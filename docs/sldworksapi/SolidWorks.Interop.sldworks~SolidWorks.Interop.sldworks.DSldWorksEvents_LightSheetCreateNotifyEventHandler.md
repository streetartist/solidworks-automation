# DSldWorksEvents_LightSheetCreateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_LightSheetCreateNotifyEventHandler`

Fired when a lighting sheet has been created.
Fired when a lighting sheet has been created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_LightSheetCreateNotifyEventHandler( _
   ByVal NewSheet As System.Object, _
   ByVal sheetType As System.Integer, _
   ByVal LightId As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_LightSheetCreateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_LightSheetCreateNotifyEventHandler( 
   System.object NewSheet,
   System.int sheetType,
   System.int LightId
)
```

```

public delegate System.int DSldWorksEvents_LightSheetCreateNotifyEventHandler( 
   System.Object^ NewSheet,
   System.int sheetType,
   System.int LightId
)
```

#### Parameters

*NewSheet*
:   New lighting sheet

*sheetType*
:   Type of the new lighting sheet

*LightId*
:   Light sheet ID

Remarks

If developing a C++ application, use [swAppLightSheetCreateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_LightSheetCreateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_LightSheetCreateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
