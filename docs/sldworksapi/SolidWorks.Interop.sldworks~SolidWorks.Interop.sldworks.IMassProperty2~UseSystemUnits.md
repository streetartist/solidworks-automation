# UseSystemUnits Property (IMassProperty2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~UseSystemUnits`

Gets or sets whether to use system units or document units when calculating mass properties.
Gets or sets whether to use system units or document units when calculating mass properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseSystemUnits As System.Boolean
```

```

Dim instance As IMassProperty2
Dim value As System.Boolean
 
instance.UseSystemUnits = value
 
value = instance.UseSystemUnits
```

```

System.bool UseSystemUnits {get; set;}
```

```

property System.bool UseSystemUnits {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use system units, false to use document units

Remarks

The default value is true. Thus, system units (meters, radians, and kilograms) are used by default. All properties returning a value are adjusted accordingly.

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)
