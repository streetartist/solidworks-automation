# ICreateArc Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc`

Obsolete. Superseded by IModelDoc2::ICreateArc2.
Obsolete. Superseded by [IModelDoc2::ICreateArc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateArc( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal Dir As System.Short _
) 
```

```

Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim Dir As System.Short
 
instance.ICreateArc(P1, P2, P3, Dir)
```

```

void ICreateArc( 
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.short Dir
)
```

```

void ICreateArc( 
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.short Dir
) 
```

#### Parameters

*P1*

*P2*

*P3*

*Dir*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
