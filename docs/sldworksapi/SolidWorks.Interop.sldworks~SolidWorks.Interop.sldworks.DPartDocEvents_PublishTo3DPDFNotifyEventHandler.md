# DPartDocEvents_PublishTo3DPDFNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PublishTo3DPDFNotifyEventHandler`

Fired when publishing a part document to SOLIDWORKS MBD 3D PDF.
Fired when publishing a part document to SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_PublishTo3DPDFNotifyEventHandler( _
   ByVal Path As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_PublishTo3DPDFNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_PublishTo3DPDFNotifyEventHandler( 
   System.string Path
)
```

```

public delegate System.int DPartDocEvents_PublishTo3DPDFNotifyEventHandler( 
   System.String^ Path
)
```

#### Parameters

*Path*
:   Path where SOLIDWORKS MBD 3D PDF is saved

Remarks

If developing a C++ application, use [swPartPublishTo3DPDFNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Notification When Publishing Part to MBD 3D PDF (C#)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_CSharp.htm)  
[Fire Notification When Publishing Part to MBD 3D PDF (VB.NET)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VBNET.htm)  
[Fire Notification When Publishing Part to MBD 3D PDF (VBA)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_PublishTo3DPDFNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PublishTo3DPDFNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
