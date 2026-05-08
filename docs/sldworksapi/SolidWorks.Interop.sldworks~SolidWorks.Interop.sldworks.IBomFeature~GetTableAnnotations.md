# GetTableAnnotations Method (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotations`

Gets the BOM table annotations for this BOM table feature.
Gets the BOM table annotations for this BOM table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotations() As System.Object
```

```

Dim instance As IBomFeature
Dim value As System.Object
 
value = instance.GetTableAnnotations()
```

```

System.object GetTableAnnotations()
```

```

System.Object^ GetTableAnnotations(); 
```

#### Return Value

Array of [IBOMTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md) objects

Example

[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)  
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)  
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)  
[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)  
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)  
[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotationCount.md)  
[IBomFeature::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetTableAnnotations.md)
