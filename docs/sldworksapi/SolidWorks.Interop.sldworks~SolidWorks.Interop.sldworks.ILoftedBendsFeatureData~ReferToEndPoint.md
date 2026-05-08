# ReferToEndPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint`

Gets or sets whether to calculate facet transitions using theoretical vertexes.
Gets or sets whether to calculate facet transitions using theoretical vertexes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferToEndPoint As System.Boolean
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean
 
instance.ReferToEndPoint = value
 
value = instance.ReferToEndPoint
```

```

System.bool ReferToEndPoint {get; set;}
```

```

property System.bool ReferToEndPoint {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to calculate facet transitions using theoretical vertexes, false to calculate them using the smallest possible arcs that avoid interference between bend areas

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
[ILoftedBendsFeatureData::FacetingOption Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption.md)  
[ILoftedBendsFeatureData::FacetValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetValue.md)  
[ILoftedBendsFeatureData::FormedMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.md)
