# BomFeature Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~BomFeature`

Gets the BOM for this table annotation.
Gets the BOM for this table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property BomFeature As BomFeature
```

```

Dim instance As IBomTableAnnotation
Dim value As BomFeature
 
value = instance.BomFeature
```

```

BomFeature BomFeature {get;}
```

```

property BomFeature^ BomFeature {
   BomFeature^ get();
}
```

#### Property Value

Pointer to the [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) object for this table annotation

Example

[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)  
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)  
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)
