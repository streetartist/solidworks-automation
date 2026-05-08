# IRestore Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore`

Obsolete. Superseded by IModeler::IRestore2.
Obsolete. Superseded by [IModeler::IRestore2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRestore( _
   ByVal StreamIn As System.Object _
) As Body
```

```

Dim instance As IModeler
Dim StreamIn As System.Object
Dim value As Body
 
value = instance.IRestore(StreamIn)
```

```

Body IRestore( 
   System.object StreamIn
)
```

```

Body^ IRestore( 
   System.Object^ StreamIn
) 
```

#### Parameters

*StreamIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
