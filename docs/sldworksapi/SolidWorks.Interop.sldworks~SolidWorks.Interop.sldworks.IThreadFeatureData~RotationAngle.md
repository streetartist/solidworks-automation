# RotationAngle Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RotationAngle`

Gets or sets the angle of rotation of the thread helix of this thread feature.
Gets or sets the angle of rotation of the thread helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RotationAngle As System.Double
```

```

Dim instance As IThreadFeatureData
Dim value As System.Double
 
instance.RotationAngle = value
 
value = instance.RotationAngle
```

```

System.double RotationAngle {get; set;}
```

```

property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 (default) <= Angle of rotation <= 2\*pi radians

Remarks

Specify either a value or an equation that starts with an equal sign (=).

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
