# DiameterType Property (IRackPinionMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterType`

Gets or sets the type of diameter to set.
Gets or sets the type of diameter to set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DiameterType As System.Integer
```

```

Dim instance As IRackPinionMateFeatureData
Dim value As System.Integer
 
instance.DiameterType = value
 
value = instance.DiameterType
```

```

System.int DiameterType {get; set;}
```

```

property System.int DiameterType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of diameter to set as defined in [swRackPinionMateDistanceOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateDistanceOptions_e.html)

Remarks

For each full rotation of the pinion, the rack translates a distance = (pi \* pinion pitch diameter). Use this property to set either the pinion pitch diameter or the rack translation distance per pinion revolution.

If this property is set to swRackPinionMateDistanceOptions\_e:

- swPinionPitchDiameter, then set [IRackPinionMateFeatureData::DiameterVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterVal.md) with the pinion pitch diameter.
- swRackTravelPerRevolution, then set IRackPinionMateFeatureData::DiameterVal with the rack translation distance per revolution of the pinion.

Example

See the [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md)  
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.md)
