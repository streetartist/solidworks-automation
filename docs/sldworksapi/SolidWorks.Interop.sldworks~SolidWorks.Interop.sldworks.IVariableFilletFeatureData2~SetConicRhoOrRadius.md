# SetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius`

Sets the conic rho or radius for the specified fillet item.
Sets the conic rho or radius for the specified fillet item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object, _
   ByVal ConicRhoVal As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim ConicRhoVal As System.Double
 
instance.SetConicRhoOrRadius(PFilletItem, ConicRhoVal)
```

```

void SetConicRhoOrRadius( 
   System.object PFilletItem,
   System.double ConicRhoVal
)
```

```

void SetConicRhoOrRadius( 
   System.Object^ PFilletItem,
   System.double ConicRhoVal
) 
```

#### Parameters

*PFilletItem*
:   Fillet item for which to set ConicRhoVal (see **Remarks**)

*ConicRhoVal*
:   Conic rho or radius (see **Remarks**)

Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetFilletEdgeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.md) to specify PFilletItem.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) is set to [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then specify ConicRhoVal with a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then specify ConicRhoVal with the conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::GetConicRhoOrRadius2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.md)  
[IVariableFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::SetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.md)
