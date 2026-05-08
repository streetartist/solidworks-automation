# GetProperties2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties2`

Gets the properties for this sheet.
Gets the properties for this sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProperties2() As System.Object
```

```

Dim instance As ISheet
Dim value As System.Object
 
value = instance.GetProperties2()
```

```

System.object GetProperties2()
```

```

System.Object^ GetProperties2(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of eight doubles:

[ paperSize, templateIn, scale1, scale2, firstAngle, width, height, sameCustomProp ]

where:

paperSize = Paper size; this value is a long or integer packed into a double and is represented by the [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html) enumeration

templateIn = Template index; this value is a long or integer packed into a double and is represented by the [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html) enumeration

scale1 = Scale numerator

scale2 = Scale denominator

firstAngle = Value is a boolean packed into a double and returns true if the sheet is using first angle projection; false if not

width = Paper width

height = Paper height

*sameCustomProp* = Value is a boolean packed into a double and returns true if the **Same as sheet specified in Document Properties** in the Sheet Properties dialog is selected, false if not

NOTES:

- To ensure a correct return value, open the document as read-write or read-only. Insufficient information is available if you open the document as view-only.
- You can also use [ISheet::GetSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md) to get the size of the sheet and the standard sheet size.

Example

[Set Drawing Sheet Properties (C#)](Set_Drawing_Sheet_Properties_Example_CSharp.htm)  
[Set Drawing Sheet Properties (VB.NET)](Set_Drawing_Sheet_Properties_Example_VBNET.htm)  
[Set Drawing Sheet Properties (VBA)](Set_Drawing_Sheet_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::SetProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties2.md)  
[ISheet::PageSetup Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md)  
[ISheet::GetSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md)  
[ISheet::SetSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.md)  
[ISheet::GetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::SetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)
