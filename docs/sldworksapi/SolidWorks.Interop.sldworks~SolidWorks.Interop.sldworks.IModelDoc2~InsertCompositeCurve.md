# InsertCompositeCurve Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCompositeCurve`

Inserts a composite curve based on selections.
Inserts a composite curve based on selections.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCompositeCurve() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.InsertCompositeCurve()
```

```

System.bool InsertCompositeCurve()
```

```

System.bool InsertCompositeCurve(); 
```

Remarks

To use this method, select the entities by calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a mark number of 1.

See the SOLIDWORKS Help for information about which entities are valid for selection.

Example

[Insert a Composite Curve (C#)](Insert_a_Composite_Curve_Example_CSharp.htm)  
[Insert a Composite Curve (VB.NET)](Insert_a_Composite_Curve_Example_VBNET.htm)  
[Insert a Composite Curve (VBA)](Insert_a_Composite_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
