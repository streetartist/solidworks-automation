# ICreateBodyFromBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox`

Obsolete. Superseded by IModeler::ICreateBodyFromBox2.
Obsolete. Superseded by [IModeler::ICreateBodyFromBox2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodyFromBox( _
   ByRef BoxDimArray As System.Double _
) As Body
```

```

Dim instance As IModeler
Dim BoxDimArray As System.Double
Dim value As Body
 
value = instance.ICreateBodyFromBox(BoxDimArray)
```

```

Body ICreateBodyFromBox( 
   ref System.double BoxDimArray
)
```

```

Body^ ICreateBodyFromBox( 
   System.double% BoxDimArray
) 
```

#### Parameters

*BoxDimArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
