# IGetRadius Method (IVariableFilletFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~IGetRadius`

Obsolete. Superseded by IVariableFilletFeatureData2::GetRadius2.
Obsolete. Superseded by [IVariableFilletFeatureData2::GetRadius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRadius( _
   ByVal PFilletItem As Vertex _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData
Dim PFilletItem As Vertex
Dim value As System.Double
 
value = instance.IGetRadius(PFilletItem)
```

```

System.double IGetRadius( 
   Vertex PFilletItem
)
```

```

System.double IGetRadius( 
   Vertex^ PFilletItem
) 
```

#### Parameters

*PFilletItem*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.md)  
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.md)
