# CircularProfile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile`

Gets or sets whether to use a circular profile for this sweep feature.
Gets or sets whether to use a circular profile for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CircularProfile As System.Boolean
```

```

Dim instance As ISweepFeatureData
Dim value As System.Boolean
 
instance.CircularProfile = value
 
value = instance.CircularProfile
```

```

System.bool CircularProfile {get; set;}
```

```

property System.bool CircularProfile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a circular profile, false to use a [sketch profile or tool body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.md)

Remarks

If this property is set to false, call [ISweepFeatureData::GetCutSweepOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetCutSweepOption.md) to determine the type of profile.

To get or set the diameter of a circular profile, use [ISweepFeatureData::CircularProfileDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfileDiameter.md).

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::GetProfileType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetProfileType.md)
