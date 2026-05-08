# FacetingOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption`

Gets or sets how facets are created in this lofted bend feature.
Gets or sets how facets are created in this lofted bend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FacetingOption As System.Integer
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer
 
instance.FacetingOption = value
 
value = instance.FacetingOption
```

```

System.int FacetingOption {get; set;}
```

```

property System.int FacetingOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Faceting option as defined in [swLoftedBendFacetOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLoftedBendFacetOptions_e.html)

Remarks

This property is valid only if [ILoftedBendsFeatureData::FormedMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.md) is false.

After setting this property, set [ILoftedBendsFeatureData::FacetValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetValue.md).

Example

See examples for [ILoftedBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::ReferToEndPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.md)
