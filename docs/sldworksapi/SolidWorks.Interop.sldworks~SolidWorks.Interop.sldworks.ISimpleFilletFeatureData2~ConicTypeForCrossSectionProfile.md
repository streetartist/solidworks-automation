# ConicTypeForCrossSectionProfile Property (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile`

Gets or sets the cross-sectional profile for this simple fillet.
Gets or sets the cross-sectional profile for this simple fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConicTypeForCrossSectionProfile As System.Integer
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer
 
instance.ConicTypeForCrossSectionProfile = value
 
value = instance.ConicTypeForCrossSectionProfile
```

```

System.int ConicTypeForCrossSectionProfile {get; set;}
```

```

property System.int ConicTypeForCrossSectionProfile {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of cross-sectional profile as defined in [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html)

Remarks

This property is valid only if [ISimpleFilletFeatureData2::CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.md) is set to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md) introductory example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.md)  
[ISimpleFilletFeatureData2::RoundCorners Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RoundCorners.md)
