# KFactor Property (ICustomBendAllowance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~KFactor`

Gets or sets the K-factor.
Gets or sets the K-factor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KFactor As System.Double
```

```

Dim instance As ICustomBendAllowance
Dim value As System.Double
 
instance.KFactor = value
 
value = instance.KFactor
```

```

System.double KFactor {get; set;}
```

```

property System.double KFactor {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

K-factor value

Remarks

When using this property to set a value for K-factor, then the [type of custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.md) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

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
