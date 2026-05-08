# GetTemplateSheetMetal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTemplateSheetMetal`

Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later.
Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTemplateSheetMetal() As System.Object
```

```

Dim instance As IModelDocExtension
Dim value As System.Object
 
value = instance.GetTemplateSheetMetal()
```

```

System.object GetTemplateSheetMetal()
```

```

System.Object^ GetTemplateSheetMetal(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md); Null if this model was created with SOLIDWORKS 2012 or earlier

Remarks

This method works only on sheet metal models created with SOLIDWORKS 2013 or later. To obtain sheet metal feature data for earlier models, follow the examples of [ISheetMetalFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md).

Example

[Get Sheet Metal Feature Data (VBA)](Get_Template_Sheet_Metal_Feature_Data_Example_VB.htm)  
[Get Sheet Metal Feature Data (VB.NET)](Get_Template_Sheet_Metal_Feature_Data_Example_VBNET.htm)  
[Get Sheet Metal Feature Data (C#)](Get_Template_Sheet_Metal_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
