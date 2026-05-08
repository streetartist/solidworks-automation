# Angle Property (ICountersinkElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~Angle`

Gets or sets the angle of this countersink hole element.
Gets or sets the angle of this countersink hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Angle As System.Double
```

```

Dim instance As ICountersinkElementData
Dim value As System.Double
 
instance.Angle = value
 
value = instance.Angle
```

```

System.double Angle {get; set;}
```

```

property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle in radians

Remarks

This property is valid only if [ICountersinkElementData::AngleOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~AngleOverride.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICountersinkElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.md)  
[ICountersinkElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData_members.md)
