# ISetXform Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetXform`

Obsolete. Superseded by IComponent2::Transform2.
Obsolete. Superseded by [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetXform( _
   ByRef XformIn As System.Double _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim XformIn As System.Double
Dim value As System.Boolean
 
value = instance.ISetXform(XformIn)
```

```

System.bool ISetXform( 
   ref System.double XformIn
)
```

```

System.bool ISetXform( 
   System.double% XformIn
) 
```

#### Parameters

*XformIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
