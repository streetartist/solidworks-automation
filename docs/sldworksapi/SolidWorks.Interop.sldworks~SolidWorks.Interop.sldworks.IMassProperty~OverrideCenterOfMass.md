# OverrideCenterOfMass Property (IMassProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass`

Gets or sets whether to override the calculated center of mass value for the model.
Gets or sets whether to override the calculated center of mass value for the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideCenterOfMass As System.Boolean
```

```

Dim instance As IMassProperty
Dim value As System.Boolean
 
instance.OverrideCenterOfMass = value
 
value = instance.OverrideCenterOfMass
```

```

System.bool OverrideCenterOfMass {get; set;}
```

```

property System.bool OverrideCenterOfMass {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the center of mass value, false to use the calculated value

Example

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)  
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)  
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::ISetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue.md)  
[IMassProperty::SetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue.md)  
[IMassProperty::CenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.md)
