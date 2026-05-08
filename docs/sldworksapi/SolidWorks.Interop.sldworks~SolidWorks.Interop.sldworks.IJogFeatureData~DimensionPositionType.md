# DimensionPositionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~DimensionPositionType`

Gets or sets the dimension position type for this jog feature.
Gets or sets the dimension position type for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DimensionPositionType As System.Integer
```

```

Dim instance As IJogFeatureData
Dim value As System.Integer
 
instance.DimensionPositionType = value
 
value = instance.DimensionPositionType
```

```

System.int DimensionPositionType {get; set;}
```

```

property System.int DimensionPositionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Dimension position type as defined in [swJogDimensionPositionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogDimensionPositionType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)
