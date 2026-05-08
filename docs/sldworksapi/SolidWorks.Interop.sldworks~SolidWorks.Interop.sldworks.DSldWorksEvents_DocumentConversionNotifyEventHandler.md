# DSldWorksEvents_DocumentConversionNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentConversionNotifyEventHandler`

Post-notifies the user program that a file has been converted from an older version of SOLIDWORKS during the open operation.
Post-notifies the user program that a file has been converted from an older version of SOLIDWORKS during the open operation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_DocumentConversionNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_DocumentConversionNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_DocumentConversionNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_DocumentConversionNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the converted file

Remarks

Any number of these notifications may be sent at the end of an open operation because an open operation of an assembly or drawing may cause multiple files to open. In this scenario, all of the opened files may have been converted.

If developing a C++ application, use [swAppDocumentConversionNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_DocumentConversionNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentConversionNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
