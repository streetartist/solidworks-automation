# SetConicRhoOrRadius Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetConicRhoOrRadius`

Sets the conic rho or radius of this fillet/chamfer.
Sets the conic rho or radius of this fillet/chamfer.

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

Dim instance As ISimpleFilletFeatureData2
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

Before calling this method, call [ISimpleFilletFeatureData2::GetFilletItemAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFilletItemAtIndex.md) to get the pointer with which to specify PFilletItem.

The value specified in ConicRhoVal must match the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.md) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::ISetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetConicRhoOrRadius.md)  
[ISimpleFilletFeatureData2::GetConicRhoOrRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetConicRhoOrRadius.md)
