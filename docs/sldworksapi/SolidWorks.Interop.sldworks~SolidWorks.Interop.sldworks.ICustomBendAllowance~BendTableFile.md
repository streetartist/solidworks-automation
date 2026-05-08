# BendTableFile Property (ICustomBendAllowance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendTableFile`

Gets or sets the path and file name for the bend table.
Gets or sets the path and file name for the bend table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendTableFile As System.String
```

```

Dim instance As ICustomBendAllowance
Dim value As System.String
 
instance.BendTableFile = value
 
value = instance.BendTableFile
```

```

System.string BendTableFile {get; set;}
```

```

property System.String^ BendTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and file name for the bend table

Remarks

When using this property to set the path and file name for a bend table, then the [type of custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.md) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

See the ICustomBendAllowance Remarks.

Example

See [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) examples.

Example

[Change Bend Radius of Sketch Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)  
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.md)
