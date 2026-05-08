# Diameter Property (IAdvancedHoleElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Diameter`

Gets or sets the diameter of this Advanced Hole element.
Gets or sets the diameter of this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Diameter As System.Double
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.Double
 
instance.Diameter = value
 
value = instance.Diameter
```

```

System.double Diameter {get; set;}
```

```

property System.double Diameter {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Diameter of the Advanced Hole

Remarks

This property is valid only if [IAdvancedHoleElementData::DiameterOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~DiameterOverride.md) is set to true.

Example

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)
