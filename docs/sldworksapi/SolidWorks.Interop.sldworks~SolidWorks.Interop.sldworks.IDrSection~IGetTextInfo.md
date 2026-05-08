# IGetTextInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextInfo`

Gets the location of the section line text.
Gets the location of the section line text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTextInfo() As System.Double
```

```

Dim instance As IDrSection
Dim value As System.Double
 
value = instance.IGetTextInfo()
```

```

System.double IGetTextInfo()
```

```

System.double IGetTextInfo(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The section line in a drawing view usually has a piece of text near each end of the line, typically the section view label ([IDrSection::GetLabel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLabel.md)). The array returned by this method consists of 6 doubles, the (X, Y, Z) origin of one text followed by the (X, Y, Z) origin of the other text. The origin is the upper-left corner of the text.

These values are the same as some of the information in the array returned by [IView::IGetSectionLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.md). The text information in that array also contains the text height. This method returns an array that does not include that information, but you can get it using [IDrSection::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextFormat.md) and [ITextFormat::CharHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeight.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetTextInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextInfo.md)
