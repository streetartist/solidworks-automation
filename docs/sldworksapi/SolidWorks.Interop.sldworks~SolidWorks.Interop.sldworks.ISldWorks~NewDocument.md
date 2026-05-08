# NewDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument`

Creates a new document based on the specified template.
Creates a new document based on the specified template.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function NewDocument( _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Object
```

```

Dim instance As ISldWorks
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Object
 
value = instance.NewDocument(TemplateName, PaperSize, Width, Height)
```

```

System.object NewDocument( 
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

```

System.Object^ NewDocument( 
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*TemplateName*
:   Fully qualified path and name of the template to use for creating the new document

*PaperSize*
:   Size of paper as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Width*
:   Width of paper; used only when PaperSize is swDwgPapersUserDefined

*Height*
:   Height of paper; used only when PaperSize is swDwgPapersUserDefined

#### Return Value

Newly created [document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) or NULL if the operation fails

Remarks

To get the default template filename, use [ISldWorks::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.md).

Example

[Combine Assembly Components Into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)  
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Insert Conic Curve (C#)](Insert_Conic_Curve_Example_CSharp.htm)  
[Insert Conic Curve (VB.NET)](Insert_Conic_Curve_Example_VBNET.htm)  
[Insert Conic Curve (VBA)](Insert_Conic_Curve_Example_VB.htm)  
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)  
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)  
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)  
[Process Body (C#)](Process_Body_Example_CSharp.htm)  
[Process Body (VB.NET)](Process_Body_Example_VBNET.htm)  
[Process Body (VBA)](Process_Body_Example_VB.htm)  
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)  
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)  
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.md)  
[ISldWorks::INewDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2.md)
