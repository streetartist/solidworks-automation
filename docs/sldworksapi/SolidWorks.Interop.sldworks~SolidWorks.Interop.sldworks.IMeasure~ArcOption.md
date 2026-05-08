# ArcOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ArcOption`

Gets or sets how to measure an arc or circle.
Gets or sets how to measure an arc or circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ArcOption As System.Integer
```

```

Dim instance As IMeasure
Dim value As System.Integer
 
instance.ArcOption = value
 
value = instance.ArcOption
```

```

System.int ArcOption {get; set;}
```

```

property System.int ArcOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

How to measure an arc or circle as defined by [swMeasureArcCircleOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMeasureArcCircleOption_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.md)  
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.md)  
[IMeasure::ArcLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ArcLength.md)
