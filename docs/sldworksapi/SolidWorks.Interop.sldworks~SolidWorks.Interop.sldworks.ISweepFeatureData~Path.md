# Path Property (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path`

Gets or sets the sweep path for this sweep feature.
Gets or sets the sweep path for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Path As System.Object
```

```

Dim instance As ISweepFeatureData
Dim value As System.Object
 
instance.Path = value
 
value = instance.Path
```

```

System.object Path {get; set;}
```

```

property System.Object^ Path {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

A set of sketched [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) contained in one sketch, a curve, or a set of model [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

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
[ISweepFeatureData::GetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.md)  
[ISweepFeatureData::SetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.md)  
[ISweepFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndTangencyType.md)  
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.md)  
[ISweepFeatureData::PathAlignmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.md)  
[ISweepFeatureData::Direction Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.md)
