# MaterialIdName Property (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName`

Gets or sets the material name.
Gets or sets the material name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaterialIdName As System.String
```

```

Dim instance As IPartDoc
Dim value As System.String
 
instance.MaterialIdName = value
 
value = instance.MaterialIdName
```

```

System.string MaterialIdName {get; set;}
```

```

property System.String^ MaterialIdName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Material name (see **Remarks**)

Remarks

This property returns a string that contains three pieces of information separated by a pipe "|":

- Database name
- Material name
- Database ID of material

Example:

MY MATERIALS|1.0038 (S235JR)|277

Example

[Get Material Property Names (VBA)](Get_Material_Property_Names_Example_VB.htm)  
[Set Material Property Name (VBA)](Set_Material_Property_Name_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.md)  
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.md)  
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.md)  
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.md)  
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.md)  
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.md)  
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.md)
