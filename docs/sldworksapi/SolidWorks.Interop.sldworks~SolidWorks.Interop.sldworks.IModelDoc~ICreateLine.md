# ICreateLine Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateLine`

Obsolete. Superseded by IModelDoc2::ICreateLine.
Obsolete. Superseded by [IModelDoc2::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateLine.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateLine( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim P1 As System.Double
Dim P2 As System.Double
 
instance.ICreateLine(P1, P2)
```

```

void ICreateLine( 
   ref System.double P1,
   ref System.double P2
)
```

```

void ICreateLine( 
   System.double% P1,
   System.double% P2
) 
```

#### Parameters

*P1*

*P2*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
