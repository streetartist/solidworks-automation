# IGetMassProperties2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetMassProperties2`

Obsolete. Superseded by IModelDoc2::IGetMassProperties2.
Obsolete. Superseded by [IModelDoc2::IGetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetMassProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMassProperties2( _
   ByRef Status As System.Integer _
) As System.Double
```

```

Dim instance As IModelDoc
Dim Status As System.Integer
Dim value As System.Double
 
value = instance.IGetMassProperties2(Status)
```

```

System.double IGetMassProperties2( 
   out System.int Status
)
```

```

System.double IGetMassProperties2( 
   [Out] System.int Status
) 
```

#### Parameters

*Status*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
