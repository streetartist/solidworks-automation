# SpecificUnitType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~SpecificUnitType`

Gets the specific unit type for this user unit.
Gets the specific unit type for this user unit.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpecificUnitType As System.Integer
```

```

Dim instance As IUserUnit
Dim value As System.Integer
 
instance.SpecificUnitType = value
 
value = instance.SpecificUnitType
```

```

System.int SpecificUnitType {get; set;}
```

```

property System.int SpecificUnitType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

| If [IUserUnit::UnitType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~UnitType.md) is [swUserUnitsType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)... | Then this property is as defined in... |
| --- | --- |
| swLengthUnit | [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) |
| swAngleUnit | [swAngleUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html) |

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)
