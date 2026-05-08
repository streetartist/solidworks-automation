# ISetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius`

Sets the conic rho, conic radius, or circular radius of this fillet.
Sets the conic rho, conic radius, or circular radius of this fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetConicRhoOrRadius( _
   ByVal PFilletItem As Vertex, _
   ByVal ConicRhoVal As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As Vertex
Dim ConicRhoVal As System.Double
 
instance.ISetConicRhoOrRadius(PFilletItem, ConicRhoVal)
```

```

void ISetConicRhoOrRadius( 
   Vertex PFilletItem,
   System.double ConicRhoVal
)
```

```

void ISetConicRhoOrRadius( 
   Vertex^ PFilletItem,
   System.double ConicRhoVal
) 
```

#### Parameters

*PFilletItem*
:   Fillet edge for which to set ConicRhoVal (see **Remarks**)

*ConicRhoVal*
:   Conic rho, conic radius, or circular radius (see **Remarks**)

Remarks

Before calling this method, call [IVariableFilletFeatureData2::IGetFilletEdgeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.md) to specify PFilletItem.

The type of ConicRhoVal must match the [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::ISetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.md)
