# DPartDocEvents_ConvertToBodiesPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ConvertToBodiesPostNotifyEventHandler`

Fired after the Convert to Bodies dialog closes.
Fired after the Convert to Bodies dialog closes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_ConvertToBodiesPostNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal SaveOption As System.Integer, _
   ByVal PreserveGeometryAndSketches As System.Boolean _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_ConvertToBodiesPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_ConvertToBodiesPostNotifyEventHandler( 
   System.string FileName,
   System.int SaveOption,
   System.bool PreserveGeometryAndSketches
)
```

```

public delegate System.int DPartDocEvents_ConvertToBodiesPostNotifyEventHandler( 
   System.String^ FileName,
   System.int SaveOption,
   System.bool PreserveGeometryAndSketches
)
```

#### Parameters

*FileName*
:   File name of the part to convert to a body

*SaveOption*
:   Save option as defined in [swFileSaveTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveTypes_e.html):

    - swFileSaveAs
    - swFileSaveAsCopy
    - swFileSaveAsCopyAndOpen

*PreserveGeometryAndSketches*
:   True to preserve geometry and sketches, false to not

Remarks

This event is triggered after the user clicks **OK** or **Cancel** in the Convert to Bodies dialog and before user interface validation. FileName, SaveOption and PreserveGeometryAndSketches contain the values selected in the dialog.

If developing a C++ application, use [swPartConvertToBodiesPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_ConvertToBodiesPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ConvertToBodiesPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
