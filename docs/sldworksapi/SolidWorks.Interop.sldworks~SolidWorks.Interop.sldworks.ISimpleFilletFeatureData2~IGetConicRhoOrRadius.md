# IGetConicRhoOrRadius Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetConicRhoOrRadius`

Gets the conic rho, conic radius, or circular radius of this fillet.
Gets the conic rho, conic radius, or circular radius of this fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConicRhoOrRadius( _
   ByVal PFilletItem As System.Object _
) As System.Double
```

```

Dim instance As ISimpleFilletFeatureData2
Dim PFilletItem As System.Object
Dim value As System.Double
 
value = instance.IGetConicRhoOrRadius(PFilletItem)
```

```

System.double IGetConicRhoOrRadius( 
   System.object PFilletItem
)
```

```

System.double IGetConicRhoOrRadius( 
   System.Object^ PFilletItem
) 
```

#### Parameters

*PFilletItem*
:   Fillet item for which to get a value (see **Remarks**)

#### Return Value

Conic rho, conic radius, or circular radius

Remarks

Before calling this method, call [ISimpleFilletFeatureData2::IGetFilletItemAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetFilletItemAtIndex.md) to get the pointer with which to specify PFilletItem.

The type of value returned by this method corresponds to the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.md) setting.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetConicRhoOrRadius.md)  
[ISimpleFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.md)
