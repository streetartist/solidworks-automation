# ICreateBodyFromCyl Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl`

Obsolete. Superseded by IModeler::ICreateBodyFromCyl2.
Obsolete. Superseded by [IModeler::ICreateBodyFromCyl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodyFromCyl( _
   ByRef CylDimArray As System.Double _
) As Body
```

```

Dim instance As IModeler
Dim CylDimArray As System.Double
Dim value As Body
 
value = instance.ICreateBodyFromCyl(CylDimArray)
```

```

Body ICreateBodyFromCyl( 
   ref System.double CylDimArray
)
```

```

Body^ ICreateBodyFromCyl( 
   System.double% CylDimArray
) 
```

#### Parameters

*CylDimArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
