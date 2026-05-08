# ICreatePlaneFixed Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePlaneFixed`

Obsolete. Superseded by IModelDoc2::ICreatePlaneFixed.
Obsolete. Superseded by [IModelDoc2::ICreatePlaneFixed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreatePlaneFixed( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal UseGlobal As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim UseGlobal As System.Boolean
 
instance.ICreatePlaneFixed(P1, P2, P3, UseGlobal)
```

```

void ICreatePlaneFixed( 
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.bool UseGlobal
)
```

```

void ICreatePlaneFixed( 
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.bool UseGlobal
) 
```

#### Parameters

*P1*

*P2*

*P3*

*UseGlobal*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
