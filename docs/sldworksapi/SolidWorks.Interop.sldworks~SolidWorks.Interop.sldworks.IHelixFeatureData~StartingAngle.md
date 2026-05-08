# StartingAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~StartingAngle`

Gets or sets the angle for the first turn of this helix feature.
Gets or sets the angle for the first turn of this helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartingAngle As System.Double
```

```

Dim instance As IHelixFeatureData
Dim value As System.Double
 
instance.StartingAngle = value
 
value = instance.StartingAngle
```

```

System.double StartingAngle {get; set;}
```

```

property System.double StartingAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle for the first turn

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
