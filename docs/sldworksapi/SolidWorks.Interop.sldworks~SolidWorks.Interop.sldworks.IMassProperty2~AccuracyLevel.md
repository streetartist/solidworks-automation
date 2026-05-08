# AccuracyLevel Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~AccuracyLevel`

Gets or sets the accuracy level used to calculate mass properties.
Gets or sets the accuracy level used to calculate mass properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AccuracyLevel As System.Integer
```

```

Dim instance As IMassProperty2
Dim value As System.Integer
 
instance.AccuracyLevel = value
 
value = instance.AccuracyLevel
```

```

System.int AccuracyLevel {get; set;}
```

```

property System.int AccuracyLevel {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Accuracy level as defined in [swMassPropertyAccuracyLevel\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMassPropertyAccuracyLevel_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)
