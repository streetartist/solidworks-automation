# ISetRadius Method (IVariableFilletFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~ISetRadius`

Obsolete. Superseded by IVariableFilletFeatureData2::ISetRadius.
Obsolete. Superseded by [IVariableFilletFeatureData2::ISetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetRadius( _
   ByVal PFilletItem As Vertex, _
   ByVal Radius As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData
Dim PFilletItem As Vertex
Dim Radius As System.Double
 
instance.ISetRadius(PFilletItem, Radius)
```

```

void ISetRadius( 
   Vertex PFilletItem,
   System.double Radius
)
```

```

void ISetRadius( 
   Vertex^ PFilletItem,
   System.double Radius
) 
```

#### Parameters

*PFilletItem*

*Radius*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.md)  
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.md)
