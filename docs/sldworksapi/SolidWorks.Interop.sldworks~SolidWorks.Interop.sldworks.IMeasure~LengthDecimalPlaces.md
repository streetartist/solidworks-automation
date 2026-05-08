# LengthDecimalPlaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~LengthDecimalPlaces`

Gets or sets the number of decimal places for length measurements.
Gets or sets the number of decimal places for length measurements.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LengthDecimalPlaces As System.Integer
```

```

Dim instance As IMeasure
Dim value As System.Integer
 
instance.LengthDecimalPlaces = value
 
value = instance.LengthDecimalPlaces
```

```

System.int LengthDecimalPlaces {get; set;}
```

```

property System.int LengthDecimalPlaces {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of decimal places for length measurements

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.md)  
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.md)  
[IMeasure::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Length.md)  
[IMeasure::TotalLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalLength.md)
