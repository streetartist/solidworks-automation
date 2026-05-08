# Tolerance Property (IDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Tolerance`

Gets the IDimensionTolerance object.
Gets the [IDimensionTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md) object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Tolerance As DimensionTolerance
```

```

Dim instance As IDimension
Dim value As DimensionTolerance
 
value = instance.Tolerance
```

```

DimensionTolerance Tolerance {get;}
```

```

property DimensionTolerance^ Tolerance {
   DimensionTolerance^ get();
}
```

#### Property Value

Pointer to the [IDimensionTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md) object

Example

[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)  
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)  
[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
