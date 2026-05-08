# Profile Property (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile`

Gets and sets the sketch profile or tool body for this sweep feature.
Gets and sets the sketch profile or tool body for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Profile As System.Object
```

```

Dim instance As ISweepFeatureData
Dim value As System.Object
 
instance.Profile = value
 
value = instance.Profile
```

```

System.object Profile {get; set;}
```

```

property System.Object^ Profile {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Sketch profile or tool body for this sweep feature (see **Remarks**)

Remarks

| If a... | Then the type of object is a... |
| --- | --- |
| Sketch profile | [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) |
| Tool body (see **NOTE**) | [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that is convex, not merged with the main body and consists of one of the following:   - A revolved feature that consist of analytical geometry only, such as lines and arcs - A cylindrical extruded feature |

**NOTE:** Tool bodies are supported in swept-cut features in SOLIDWORKS API 2017 FCS and later.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::CircularProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.md)  
[ISweepFeatureData::GetProfileType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetProfileType.md)  
[ISweepFeatureData::Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.md)
