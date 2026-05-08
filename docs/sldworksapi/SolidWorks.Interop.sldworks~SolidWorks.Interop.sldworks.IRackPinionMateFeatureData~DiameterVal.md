# DiameterVal Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterVal`

Gets or sets either the pinion pitch diameter or the rack translation distance per pinion revolution.
Gets or sets either the pinion pitch diameter or the rack translation distance per pinion revolution.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DiameterVal As System.Double
```

```

Dim instance As IRackPinionMateFeatureData
Dim value As System.Double
 
instance.DiameterVal = value
 
value = instance.DiameterVal
```

```

System.double DiameterVal {get; set;}
```

```

property System.double DiameterVal {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Pinion pitch diameter or rack translation distance per pinion revolution (see **Remarks**)

Remarks

For each full rotation of the pinion, the rack translates a distance = (pi \* pinion pitch diameter).

If [IRackPinionMateFeatureData::DiameterType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~DiameterType.md) is set to [swRackPinionMateDistanceOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRackPinionMateDistanceOptions_e.html):

- swPinionPitchDiameter, use this property to specify the pinion pitch diameter.
- swRackTravelPerRevolution, use this property to specify the rack translation distance per revolution of the pinion.

Example

See the [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.md)  
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.md)
