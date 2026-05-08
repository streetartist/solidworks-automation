# SingleDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SingleDirection`

Gets or sets whether the projection split line is in a single direction.
Gets or sets whether the projection split line is in a single direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SingleDirection As System.Boolean
```

```

Dim instance As ISplitLineFeatureData
Dim value As System.Boolean
 
instance.SingleDirection = value
 
value = instance.SingleDirection
```

```

System.bool SingleDirection {get; set;}
```

```

property System.bool SingleDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if single direction, false if not

Remarks

This property is valid only if [ISplitLineFeatureData::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetType.md) is set to [swSplitLineFeatureType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitLineFeatureType_e.html).swSplitLineFeatureType\_Projection.

Example

See the [ISplitLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::PullDirectionBase Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionBase.md)  
[ISplitLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionType.md)  
[ISplitLineFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ReverseDirection.md)  
[ISplitLineFeatureData::SplitType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitType.md)
