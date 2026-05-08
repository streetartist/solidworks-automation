# GetConicRhoOrRadius Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius`

Gets the conic rho, conic radius, or circular radius of this fillet.
Gets the conic rho, conic radius, or circular radius of this fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double
 
value = instance.GetConicRhoOrRadius(PFilletItem)
```

```

System.double GetConicRhoOrRadius( 
   System.object PFilletItem
)
```

```

System.double GetConicRhoOrRadius( 
   System.Object^ PFilletItem
) 
```

#### Parameters

*PFilletItem*
:   Fillet edge for which to get a value (see **Remarks**)

#### Return Value

Conic rho or radius of this fillet

Remarks

Before calling this method, call [IVariableFilletFeatureData2::GetFilletEdgeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.md) to specify PFilletItem.

The type of value returned by this method corresponds to the [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) setting.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::SetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::IGetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.md)
