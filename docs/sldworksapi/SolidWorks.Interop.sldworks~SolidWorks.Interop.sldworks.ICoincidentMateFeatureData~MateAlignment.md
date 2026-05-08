# MateAlignment Property (ICoincidentMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~MateAlignment`

Gets or sets the mate alignment of this coincident mate.
Gets or sets the mate alignment of this coincident mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MateAlignment As System.Integer
```

```

Dim instance As ICoincidentMateFeatureData
Dim value As System.Integer
 
instance.MateAlignment = value
 
value = instance.MateAlignment
```

```

System.int MateAlignment {get; set;}
```

```

property System.int MateAlignment {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Mate alignment as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.html)

Example

See the [ICoincidentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoincidentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md)  
[ICoincidentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData_members.md)
