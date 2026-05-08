# JogAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~JogAngle`

Gets or sets the jog angle for this jog feature.
Gets or sets the jog angle for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property JogAngle As System.Double
```

```

Dim instance As IJogFeatureData
Dim value As System.Double
 
instance.JogAngle = value
 
value = instance.JogAngle
```

```

System.double JogAngle {get; set;}
```

```

property System.double JogAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Jog angle

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)
