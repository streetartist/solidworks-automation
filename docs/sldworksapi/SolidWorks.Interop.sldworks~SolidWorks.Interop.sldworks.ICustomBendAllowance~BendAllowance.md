# BendAllowance Property (ICustomBendAllowance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendAllowance`

Gets or sets the value of the bend allowance.
Gets or sets the value of the bend allowance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendAllowance As System.Double
```

```

Dim instance As ICustomBendAllowance
Dim value As System.Double
 
instance.BendAllowance = value
 
value = instance.BendAllowance
```

```

System.double BendAllowance {get; set;}
```

```

property System.double BendAllowance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value (m) of the bend allowance

Remarks

If using this property to set a value for the bend allowance, then the [type of custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.md) is set to this type. However, the last ICustomBendAllowance property set also re-sets the type of bend allowance to its type.

See the ICustomBendAllowance Remarks.

Example

See the [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) examples.

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Example

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)  
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.md)
