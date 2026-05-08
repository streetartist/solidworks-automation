# CircularProfileDiameter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfileDiameter`

Gets or sets the diameter of the circular profile for this sweep feature.
Gets or sets the diameter of the circular profile for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CircularProfileDiameter As System.Double
```

```

Dim instance As ISweepFeatureData
Dim value As System.Double
 
instance.CircularProfileDiameter = value
 
value = instance.CircularProfileDiameter
```

```

System.double CircularProfileDiameter {get; set;}
```

```

property System.double CircularProfileDiameter {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Diameter of the circular profile

Remarks

This property is valid only if [ISweepFeatureData::CircularProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.md) is set to true.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)
