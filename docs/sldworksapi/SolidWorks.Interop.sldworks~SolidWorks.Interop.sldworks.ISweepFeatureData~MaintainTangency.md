# MaintainTangency Property (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MaintainTangency`

Gets or sets whether to merge tangent faces in this sweep feature.
Gets or sets whether to merge tangent faces in this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaintainTangency As System.Boolean
```

```

Dim instance As ISweepFeatureData
Dim value As System.Boolean
 
instance.MaintainTangency = value
 
value = instance.MaintainTangency
```

```

System.bool MaintainTangency {get; set;}
```

```

property System.bool MaintainTangency {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge tangent faces, false to not (see **Remarks**)

Remarks

If the sweep profile has tangent segments, true causes the corresponding surfaces in the resulting sweep to be tangent. Faces that can be represented as a plane, cylinder, or cone are maintained. Other adjacent faces are merged, and the profiles are approximated. Sketch arcs may be converted to splines.

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
