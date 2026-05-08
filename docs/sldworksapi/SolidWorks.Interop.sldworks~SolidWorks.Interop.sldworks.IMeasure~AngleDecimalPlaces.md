# AngleDecimalPlaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~AngleDecimalPlaces`

Gets or sets the number of decimal places for angle measurements.
Gets or sets the number of decimal places for angle measurements.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AngleDecimalPlaces As System.Integer
```

```

Dim instance As IMeasure
Dim value As System.Integer
 
instance.AngleDecimalPlaces = value
 
value = instance.AngleDecimalPlaces
```

```

System.int AngleDecimalPlaces {get; set;}
```

```

property System.int AngleDecimalPlaces {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of decimal places for angle measurements

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.md)  
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.md)  
[IMeasure::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Angle.md)
