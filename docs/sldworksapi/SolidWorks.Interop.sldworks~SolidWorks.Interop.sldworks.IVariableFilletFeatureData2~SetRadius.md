# SetRadius Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius`

Sets the value of the Distance 1 radius at the specified vertex.
Sets the value of the Distance 1 radius at the specified vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal Radius As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim Radius As System.Double
 
instance.SetRadius(PFilletItem, Radius)
```

```

void SetRadius( 
   System.object PFilletItem,
   System.double Radius
)
```

```

void SetRadius( 
   System.Object^ PFilletItem,
   System.double Radius
) 
```

#### Parameters

*PFilletItem*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) at which to set the radius

*Radius*
:   Radius of the symmetric fillet at the vertex specified by PFilletItem; Distance 1 radius of the asymmetric fillet at the vertex

Remarks

Call [IVariableFilletFeatureData2::SetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetDistance.md) to set the Distance 2 radius at the vertex for the asymmetric fillet.

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::DefaultRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.md)  
[IVariableFilletFeatureData2::GetRadius2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md)  
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.md)
