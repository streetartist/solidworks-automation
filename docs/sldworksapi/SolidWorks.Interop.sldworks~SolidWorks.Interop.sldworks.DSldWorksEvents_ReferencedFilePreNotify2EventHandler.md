# DSldWorksEvents_ReferencedFilePreNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotify2EventHandler`

Notifies the user program before SOLIDWORKS opens the specified file with the specified status.
Notifies the user program before SOLIDWORKS opens the specified file with the specified status.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_ReferencedFilePreNotify2EventHandler( _
   ByVal FileName As System.String, _
   ByVal FileStatus As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_ReferencedFilePreNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_ReferencedFilePreNotify2EventHandler( 
   System.string FileName,
   System.int FileStatus
)
```

```

public delegate System.int DSldWorksEvents_ReferencedFilePreNotify2EventHandler( 
   System.String^ FileName,
   System.int FileStatus
)
```

#### Parameters

*FileName*
:   Path and filename of file to open

*FileStatus*
:   Open status as defined in [swReferencedFileStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReferencedFileStatus_e.html)

Remarks

If developing a C++ application, use [swAppReferencedFilePreNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_ReferencedFilePreNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
