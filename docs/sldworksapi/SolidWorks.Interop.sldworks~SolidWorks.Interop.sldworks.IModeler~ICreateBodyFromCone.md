# ICreateBodyFromCone Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone`

Obsolete. Superseded by IModeler::ICreateBodyFromCone2.
Obsolete. Superseded by [IModeler::ICreateBodyFromCone2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodyFromCone( _
   ByRef ConeDimArray As System.Double _
) As Body
```

```

Dim instance As IModeler
Dim ConeDimArray As System.Double
Dim value As Body
 
value = instance.ICreateBodyFromCone(ConeDimArray)
```

```

Body ICreateBodyFromCone( 
   ref System.double ConeDimArray
)
```

```

Body^ ICreateBodyFromCone( 
   System.double% ConeDimArray
) 
```

#### Parameters

*ConeDimArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
