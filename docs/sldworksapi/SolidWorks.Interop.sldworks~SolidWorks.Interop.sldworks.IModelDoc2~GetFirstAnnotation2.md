# GetFirstAnnotation2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstAnnotation2`

Gets the first annotation in the model.
Gets the first annotation in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstAnnotation2() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.GetFirstAnnotation2()
```

```

System.object GetFirstAnnotation2()
```

```

System.Object^ GetFirstAnnotation2(); 
```

#### Return Value

First [annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

For parts and assemblies, this method returns the first [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object in the model. For drawings, access the annotations using the [IView::GetFirstAnnotation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstAnnotation3.md) method.

A dimension becomes suppressed or hidden when you specifically select a dimension and hide it, or when you select a feature and you select to hide all dimensions. If you need to filter out these dimensions, use [IAnnotation::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) to check that status.

NOTE: The difference between the obsoleted IModelDoc2::GetFirstAnnotation and this method, IModelDoc2::GetFirstAnnotation2, is that IModelDoc2::GetFirstAnnotation2 retrieves any display dimension, including suppressed, hidden, or dangling dimensions.

To get the next annotation in the model, call [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md).

Example

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)  
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)  
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IGetFirstAnnotation2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstAnnotation2.md)
