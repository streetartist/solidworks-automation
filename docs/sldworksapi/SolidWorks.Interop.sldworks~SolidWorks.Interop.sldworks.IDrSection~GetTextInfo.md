# GetTextInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextInfo`

Gets the location of the section line text.
Gets the location of the section line text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextInfo() As System.Object
```

```

Dim instance As IDrSection
Dim value As System.Object
 
value = instance.GetTextInfo()
```

```

System.object GetTextInfo()
```

```

System.Object^ GetTextInfo(); 
```

#### Return Value

Array (see **Remarks**)

Remarks

The section line in a drawing view usually has a piece of text near each end of the line, typically the section view label ([IDrSection::GetLabel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLabel.md)). The array returned by this method consists of 6 doubles, the (X, Y, Z) origin of one text followed by the (X, Y, Z) origin of the other text. The origin is the upper-left corner of the text.

These values are the same as some of the information in the array returned by [IView::GetSectionLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md). The text information in that array also contains the text height. This method returns an array that does not include that information, but you can get it using [IDrSection::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextFormat.md) and [ITextFormat::CharHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeight.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::IGetTextInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextInfo.md)
