# FacetValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetValue`

Gets or sets the value corresponding to ILoftedBendsFeatureData::FacetingOption.
Gets or sets the value corresponding to [ILoftedBendsFeatureData::FacetingOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FacetValue As System.Double
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Double
 
instance.FacetValue = value
 
value = instance.FacetValue
```

```

System.double FacetValue {get; set;}
```

```

property System.double FacetValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Faceting option value

Remarks

This property is valid only if [ILoftedBendsFeatureData::FormedMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.md) is false.

Example

See examples for [ILoftedBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::ReferToEndPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.md)
