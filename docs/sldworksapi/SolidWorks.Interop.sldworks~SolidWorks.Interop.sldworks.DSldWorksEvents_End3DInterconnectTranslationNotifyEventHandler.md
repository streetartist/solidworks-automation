# DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler`

Notifies the user program when the SOLIDWORKS application is finished importing or exporting a third-party native CAD file.
Notifies the user program when the SOLIDWORKS application is finished importing or exporting a third-party native CAD file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of imported or exported third-party native CAD file

Remarks

If developing a C++ application, use [swAppEnd3DInterconnectTranslationNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_End3DInterconnectTranslationNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_End3DInterconnectTranslationNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
