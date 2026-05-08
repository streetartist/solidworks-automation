# SetProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties`

Obsolete. Superseded by ISheet::SetProperties2.
Obsolete. Superseded by [ISheet::SetProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetProperties( _
   ByVal PaperSz As System.Integer, _
   ByVal Templ As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal FirstAngle As System.Boolean, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
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
 
instance.SetProperties(PaperSz, Templ, Scale1, Scale2, FirstAngle, Width, Height)
```

```

void SetProperties( 
   System.int PaperSz,
   System.int Templ,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.double Width,
   System.double Height
)
```

```

void SetProperties( 
   System.int PaperSz,
   System.int Templ,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*PaperSz*
:   Paper size as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Templ*
:   Template as defined in [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)

*Scale1*
:   Scale numerator

*Scale2*
:   Scale denominator

*FirstAngle*
:   True if you want first angle projection, false if not

*Width*
:   Custom paper width if PaperSz = swDwgPaperSizes\_e.swDwgPapersUserDefined

*Height*
:   Custom paper height if PaperSz = swDwgPaperSizes\_e.swDwgPapersUserDefined

Remarks

If you specify a custom template, then the current custom template is used by this sheet until you call [ISheet::SetTemplateName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md) and pass in a different custom template name.

NOTE: If Templ does not match the PaperSz specification, then you get a template that does not fit the paper size. This parameter does not override the PaperSz setting. Also, if you change the scale of the sheet using Scale1 and Scale2, then any drawing view that is set to use the sheet's scale takes the new scale setting.

You can also use [ISheet::SetSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize.md) to set the size of the sheet and the standard sheet size.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.md)  
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md)  
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md)  
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.md)  
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md)  
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)
