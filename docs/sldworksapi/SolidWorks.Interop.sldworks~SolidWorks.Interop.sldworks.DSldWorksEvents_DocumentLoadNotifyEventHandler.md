# DSldWorksEvents_DocumentLoadNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotifyEventHandler`

Obsolete. Superseded by DSldWorksEvetns_DocumentLoadNotify2EventHandler.
Obsolete. Superseded by [DSldWorksEvetns\_DocumentLoadNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotify2EventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_DocumentLoadNotifyEventHandler( _
   ByVal docTitle As System.String, _
   ByVal docPath As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_DocumentLoadNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_DocumentLoadNotifyEventHandler( 
   System.string docTitle,
   System.string docPath
)
```

```

public delegate System.int DSldWorksEvents_DocumentLoadNotifyEventHandler( 
   System.String^ docTitle,
   System.String^ docPath
)
```

#### Parameters

*docTitle*

*docPath*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_DocumentLoadNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DocumentLoadNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
