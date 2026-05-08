# TangentPropagation Property (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TangentPropagation`

Gets or sets whether to propagate the sweep to the next tangent edge for this sweep feature.
Gets or sets whether to propagate the sweep to the next tangent edge for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TangentPropagation As System.Boolean
```

```

Dim instance As ISweepFeatureData
Dim value As System.Boolean
 
instance.TangentPropagation = value
 
value = instance.TangentPropagation
```

```

System.bool TangentPropagation {get; set;}
```

```

property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate the sweep to the next tangent edge, false to cause the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndTangencyType.md)  
[ISweepFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartTangencyType.md)  
[ISweepFeatureData::MaintainTangency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MaintainTangency.md)
