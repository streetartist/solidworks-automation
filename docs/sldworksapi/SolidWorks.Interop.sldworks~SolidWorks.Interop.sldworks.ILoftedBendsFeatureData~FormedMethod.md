# FormedMethod Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod`

Gets or sets whether this lofted bend feature is formed.
Gets or sets whether this lofted bend feature is formed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FormedMethod As System.Boolean
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean
 
instance.FormedMethod = value
 
value = instance.FormedMethod
```

```

System.bool FormedMethod {get; set;}
```

```

property System.bool FormedMethod {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this lofted bend feature is formed, false if it is bent

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
[ILoftedBendsFeatureData::ReferToEndPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.md)
