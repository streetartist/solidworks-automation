# FixedReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~FixedReference`

Gets or sets the fixed face or edge for this sheet metal feature.
Gets or sets the fixed face or edge for this sheet metal feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedReference As System.Object
```

```

Dim instance As ISheetMetalFeatureData
Dim value As System.Object
 
instance.FixedReference = value
 
value = instance.FixedReference
```

```

System.object FixedReference {get; set;}
```

```

property System.Object^ FixedReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Fixed reference entity (edge or face)

Remarks

To access the fixed reference of a sheet metal feature in sheet metal models created in SOLIDWORKS 2013 or later, follow the examples of [IModelDocExtension::GetTemplateSheetMetal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTemplateSheetMetal.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Get Fixed Face of Sheet Metal Part (VBA)](Get_Fixed_Face_of_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)
