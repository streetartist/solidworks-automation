# SetProperties2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties2`

Sets the properties for this sheet.
Sets the properties for this sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetProperties2( _
   ByVal PaperSz As System.Integer, _
   ByVal Templ As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal FirstAngle As System.Boolean, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double, _
   ByVal SameCustomPropAsSheetInDocProp As System.Boolean _
) 
```

```

Dim instance As ISheet
Dim PaperSz As System.Integer
Dim Templ As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim FirstAngle As System.Boolean
Dim Width As System.Double
Dim Height As System.Double
Dim SameCustomPropAsSheetInDocProp As System.Boolean
 
instance.SetProperties2(PaperSz, Templ, Scale1, Scale2, FirstAngle, Width, Height, SameCustomPropAsSheetInDocProp)
```

```

void SetProperties2( 
   System.int PaperSz,
   System.int Templ,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.double Width,
   System.double Height,
   System.bool SameCustomPropAsSheetInDocProp
)
```

```

void SetProperties2( 
   System.int PaperSz,
   System.int Templ,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.double Width,
   System.double Height,
   System.bool SameCustomPropAsSheetInDocProp
) 
```

#### Parameters

*PaperSz*
:   Paper size as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html) (see **Remarks**)

*Templ*
:   Template as defined in [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html) (see **Remarks**)

*Scale1*
:   Scale numerator (see **Remarks**)

*Scale2*
:   Scale denominator (see **Remarks**)

*FirstAngle*
:   True if you want first angle projection, false if not

*Width*
:   Custom paper width if PaperSz = swDwgPaperSizes\_e.swDwgPaperUserDefined (see **Remarks**)

*Height*
:   Custom paper height if PaperSz = swDwgPaperSizes\_e.swDwgPaperUserDefined (see **Remarks**)

*SameCustomPropAsSheetInDocProp*
:   True to select the **Same as sheet specified in Document Properties** check box in the Sheet Properties dialog, false to not (see **Remarks**)

Remarks

| If you... | Then... |
| --- | --- |
| Specify a custom template | The current custom template is used by this sheet until you call [ISheet::SetTemplateName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md) and pass in a different custom template name. |
| Specify a value for Templ that does not match PaperSz | The template does not fit the paper size. Templ does not override the PaperSz setting. |
| Change the scale of the sheet using Scale1 and Scale2 | Any drawing view that is set to use the sheet's scale takes the new scale setting. |
| Set SameCustomPropAsSheetInDocProp to true | The **Tools > Options > Document Properties > Drawing Sheets > Use custom property values from the sheet** check box must be preselected. |

**NOTE:** You can also use [ISheet::SetSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.md) to set the size of the sheet and the standard sheet size.

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
[ISheet::GetProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties2.md)  
[ISheet::GetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::SetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)  
[ISheet::GetSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md)  
[ISheet::PageSetup Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md)
