# IsReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsReference`

Gets whether the dimension is a reference dimension.
Gets whether the dimension is a reference dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsReference() As System.Boolean
```

```

Dim instance As IDimension
Dim value As System.Boolean
 
value = instance.IsReference()
```

```

System.bool IsReference()
```

```

System.bool IsReference(); 
```

#### Return Value

True if the dimension is a reference dimension, false if not

Remarks

This method returns false for dimensions in 3D sketches.

Example

[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDrawingDoc::InsertRefDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.md)  
[IDisplayDimension::IsReferenceDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsReferenceDim.md)
