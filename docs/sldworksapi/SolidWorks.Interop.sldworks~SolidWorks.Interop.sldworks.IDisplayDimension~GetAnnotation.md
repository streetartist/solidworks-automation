# GetAnnotation Method (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAnnotation`

Gets the IAnnotation object for this specific annotation.
Gets the IAnnotation object for this specific annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAnnotation() As System.Object
```

```

Dim instance As IDisplayDimension
Dim value As System.Object
 
value = instance.GetAnnotation()
```

```

System.object GetAnnotation()
```

```

System.Object^ GetAnnotation(); 
```

#### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Remarks

The IAnnotation object is a higher-level object that contains methods that are available to all types of annotations.

Example

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)  
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)  
[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)  
[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)  
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)  
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)  
[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)  
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)  
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetAnnotation.md)
