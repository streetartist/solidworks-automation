# DSldWorksEvents_FileNewNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotifyEventHandler`

Obsolete. Superseded by DSldWorksEvents_FileNewNotify2EventHandler.
Obsolete. Superseded by [DSldWorksEvents\_FileNewNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotify2EventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileNewNotifyEventHandler( _
   ByVal NewDoc As System.Object, _
   ByVal DocType As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileNewNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileNewNotifyEventHandler( 
   System.object NewDoc,
   System.int DocType
)
```

```

public delegate System.int DSldWorksEvents_FileNewNotifyEventHandler( 
   System.Object^ NewDoc,
   System.int DocType
)
```

#### Parameters

*NewDoc*

*DocType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileNewNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileNewNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
