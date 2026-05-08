# ISetRadius Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius`

Sets the radius value for specified fillet item.
Sets the radius value for specified fillet item.

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

Dim instance As IVariableFilletFeatureData2
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
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) whose radius to set

*Radius*
:   Radius

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.md)  
[IVariableFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.md)  
[IVariableFilletFeatureData2::GetRadius2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md)  
[IVariableFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.md)
