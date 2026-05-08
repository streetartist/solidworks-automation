# Type Property (ITableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Type`

Gets the type of table.
Gets the type of table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Type As System.Integer
```

```

Dim instance As ITableAnnotation
Dim value As System.Integer
 
value = instance.Type
```

```

System.int Type {get;}
```

```

property System.int Type {
   System.int get();
}
```

#### Property Value

Type of table as defined in [swTableAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

Example

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)  
[Insert Column in BOM Table (C#)](Insert_Column_in_BOM_Table_Example_CSharp.htm)  
[Insert Column in BOM Table (VB.NET)](Insert_Column_in_BOM_Table_Example_VBNET.htm)  
[Insert Column in BOM Table (VBA)](Insert_Column_in_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)
