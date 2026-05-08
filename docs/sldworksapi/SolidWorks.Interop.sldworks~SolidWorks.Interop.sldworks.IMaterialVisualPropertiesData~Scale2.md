# Scale2 Property (IMaterialVisualPropertiesData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~Scale2`

Gets or sets the scale factor for the standard texture.
Gets or sets the scale factor for the standard texture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Scale2 As System.Double
```

```

Dim instance As IMaterialVisualPropertiesData
Dim value As System.Double
 
instance.Scale2 = value
 
value = instance.Scale2
```

```

System.double Scale2 {get; set;}
```

```

property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value by which to scale the texture

Remarks

This property only applies to SOLIDWORKS standard textures.

Example

See [IMaterialVisualPropertiesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)  
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.md)
