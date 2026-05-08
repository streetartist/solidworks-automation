# GetTableAnnotationCount Method (IGeneralTableFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotationCount`

Gets the number of table annotations for this general table feature.
Gets the number of table annotations for this general table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTableAnnotationCount() As System.Integer
```

```

Dim instance As IGeneralTableFeature
Dim value As System.Integer
 
value = instance.GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount()
```

```

System.int GetTableAnnotationCount(); 
```

#### Return Value

Number of table annotations

Remarks

Call this method before calling [IGeneralTableFeature::IGetTableAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~IGetTableAnnotations.md) to get the size of the array.

Example

[Hide and Show Row (VBA)](Hide_and_Show_Row_Example_VB.htm)  
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)  
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)  
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.md)  
[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.md)  
[IGeneralTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotations.md)
