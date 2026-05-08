# CreatePlaneFixed Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed`

Obsolete. Superseded by IModelDoc2::CreatePlaneFixed2.
Obsolete. Superseded by [IModelDoc2::CreatePlaneFixed2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePlaneFixed( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal UseGlobal As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim UseGlobal As System.Boolean
Dim value As System.Boolean
 
value = instance.CreatePlaneFixed(P1, P2, P3, UseGlobal)
```

```

System.bool CreatePlaneFixed( 
   System.object P1,
   System.object P2,
   System.object P3,
   System.bool UseGlobal
)
```

```

System.bool CreatePlaneFixed( 
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
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

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
