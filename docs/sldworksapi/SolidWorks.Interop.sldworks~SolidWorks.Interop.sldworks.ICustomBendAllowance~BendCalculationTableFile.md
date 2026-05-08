# BendCalculationTableFile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendCalculationTableFile`

Gets or sets the bend calculation table file path name.
Gets or sets the bend calculation table file path name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendCalculationTableFile As System.String
```

```

Dim instance As ICustomBendAllowance
Dim value As System.String
 
instance.BendCalculationTableFile = value
 
value = instance.BendCalculationTableFile
```

```

System.string BendCalculationTableFile {get; set;}
```

```

property System.String^ BendCalculationTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Bend calculation table file path name

Remarks

If using this property to set a value for the bend deduction, then the [type of custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.md) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

See the ICustomBendAllowance Remarks.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)  
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.md)
