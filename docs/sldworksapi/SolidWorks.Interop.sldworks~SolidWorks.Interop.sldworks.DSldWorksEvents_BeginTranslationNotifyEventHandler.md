# DSldWorksEvents_BeginTranslationNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginTranslationNotifyEventHandler`

Notifies the user program when the SOLIDWORKS applications starts to import a file.
Notifies the user program when the SOLIDWORKS applications starts to import a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_BeginTranslationNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_BeginTranslationNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_BeginTranslationNotifyEventHandler( 
   System.string FileName,
   System.int Options
)
```

```

public delegate System.int DSldWorksEvents_BeginTranslationNotifyEventHandler( 
   System.String^ FileName,
   System.int Options
)
```

#### Parameters

*FileName*
:   Name of imported file

*Options*
:   Option as defined in [swTranslationNotifyOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTranslationNotifyOptions_e.html)

Remarks

If developing a C++ application, use [swAppBeginTranslationNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_BeginTranslationNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_BeginTranslationNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
