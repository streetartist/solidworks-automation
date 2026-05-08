# BorderLineWeightCustom Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~BorderLineWeightCustom`

Gets or sets the line weight of the border lines to the specified custom weight for this table.
Gets or sets the line weight of the border lines to the specified custom weight for this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BorderLineWeightCustom As System.Double
```

```

Dim instance As ITableAnnotation
Dim value As System.Double
 
instance.BorderLineWeightCustom = value
 
value = instance.BorderLineWeightCustom
```

```

System.double BorderLineWeightCustom {get; set;}
```

```

property System.double BorderLineWeightCustom {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Custom weight, in millimeters, of border lines for this table

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)
