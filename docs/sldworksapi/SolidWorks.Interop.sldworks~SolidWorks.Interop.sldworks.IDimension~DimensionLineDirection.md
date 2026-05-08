# DimensionLineDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DimensionLineDirection`

Gets or sets the direction of this dimension line.
Gets or sets the direction of this dimension line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DimensionLineDirection As MathVector
```

```

Dim instance As IDimension
Dim value As MathVector
 
instance.DimensionLineDirection = value
 
value = instance.DimensionLineDirection
```

```

MathVector DimensionLineDirection {get; set;}
```

```

property MathVector^ DimensionLineDirection {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

#### Property Value

Pointer to the [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) object

Remarks

This method only supports feature dimensions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::ExtensionLineDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ExtensionLineDirection.md)
