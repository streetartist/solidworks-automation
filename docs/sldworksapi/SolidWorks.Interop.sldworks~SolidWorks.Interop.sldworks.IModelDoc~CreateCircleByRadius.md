# CreateCircleByRadius Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircleByRadius`

Obsolete. Superseded by IModelDoc2::CreateCircleByRadius.
Obsolete. Superseded by [IModelDoc2::CreateCircleByRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircleByRadius.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCircleByRadius( _
   ByVal P1 As System.Object, _
   ByVal Radius As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim P1 As System.Object
Dim Radius As System.Double
Dim value As System.Boolean
 
value = instance.CreateCircleByRadius(P1, Radius)
```

```

System.bool CreateCircleByRadius( 
   System.object P1,
   System.double Radius
)
```

```

System.bool CreateCircleByRadius( 
   System.Object^ P1,
   System.double Radius
) 
```

#### Parameters

*P1*

*Radius*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
