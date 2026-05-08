# JogPositionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~JogPositionType`

Gets or sets the jog position type for this jog feature.
Gets or sets the jog position type for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property JogPositionType As System.Integer
```

```

Dim instance As IJogFeatureData
Dim value As System.Integer
 
instance.JogPositionType = value
 
value = instance.JogPositionType
```

```

System.int JogPositionType {get; set;}
```

```

property System.int JogPositionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Position type as defined in [swJogPositionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogPositionType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)
