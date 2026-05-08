# ExtensionLineDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ExtensionLineDirection`

Gets or sets the direction of the extension line.
Gets or sets the direction of the extension line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExtensionLineDirection As MathVector
```

```

Dim instance As IDimension
Dim value As MathVector
 
instance.ExtensionLineDirection = value
 
value = instance.ExtensionLineDirection
```

```

MathVector ExtensionLineDirection {get; set;}
```

```

property MathVector^ ExtensionLineDirection {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

#### Property Value

Pointer to the [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object

Remarks

This method only supports feature dimensions. Additionally, it returns non-0 vector for feature dimensions ([IDimension::GetFeatureOwner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetFeatureOwner.md)) and 0 vector for radial and chamfer dimensions.

Example

[Get Extension Line Direction (VBA)](Get_Extension_Line_Direction_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::DimensionLineDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DimensionLineDirection.md)
