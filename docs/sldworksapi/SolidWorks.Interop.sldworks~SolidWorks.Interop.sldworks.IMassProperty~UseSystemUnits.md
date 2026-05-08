# UseSystemUnits Property (IMassProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UseSystemUnits`

Gets and sets whether to use system units or document units when calculating mass properties for this model.
Gets and sets whether to use system units or document units when calculating mass properties for this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseSystemUnits As System.Boolean
```

```

Dim instance As IMassProperty
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

The default value is True. Thus, system units (meters, radians, and kilograms) are used. All properties returning a value are adjusted accordingly.

Example

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)  
[Get and Override Mass Propeties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)  
[Get and Override Mass Propeties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)
