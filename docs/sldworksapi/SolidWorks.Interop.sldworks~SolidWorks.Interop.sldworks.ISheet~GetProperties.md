# GetProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties`

Obsolete. Superseded by ISheet::GetProperties2.
Obsolete. Superseded by [ISheet::GetProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProperties() As System.Object
```

```

Dim instance As ISheet
Dim value As System.Object
 
value = instance.GetProperties()
```

```

System.object GetProperties()
```

```

System.Object^ GetProperties(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of seven doubles:

[ paperSize, templateIn, scale1, scale2, firstAngle, width, height, sameCustomPrp ]

where:

paperSize = Paper size; this value is a long or integer packed into a double and is represented by the [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html) enumeration

templateIn = Template index; this value is a long or integer packed into a double and is represented by the [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html) enumeration

scale1 = Scale numerator

scale2 = Scale denominator

firstAngle = Value is a boolean packed into a double and returns true if the sheet is using first angle projection and false if not

width = Paper width

height = Paper height

NOTE: To ensure a correct return value, open the document as read-write or read-only. Insufficient information is available if you open the document as view-only.

You can also use [ISheet::GetSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md) to get the size of the sheet and the standard sheet size.

Example

[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)  
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)  
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.md)  
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md)  
[ISheet::SetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.md)  
[ISheet::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetScale.md)  
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md)  
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.md)  
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)  
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md)  
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)
