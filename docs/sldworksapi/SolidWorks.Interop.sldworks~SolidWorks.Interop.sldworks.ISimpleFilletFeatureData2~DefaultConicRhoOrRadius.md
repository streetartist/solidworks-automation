# DefaultConicRhoOrRadius Property (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultConicRhoOrRadius`

Gets or sets the default conic rho or radius.
Gets or sets the default conic rho or radius.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DefaultConicRhoOrRadius As System.Double
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Double
 
instance.DefaultConicRhoOrRadius = value
 
value = instance.DefaultConicRhoOrRadius
```

```

System.double DefaultConicRhoOrRadius {get; set;}
```

```

property System.double DefaultConicRhoOrRadius {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Default conic rho or conic radius (see **Remarks**)

Remarks

The type of value of this property must match the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.md) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md) introductory example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::DefaultRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.md)
